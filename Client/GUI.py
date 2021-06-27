from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QInputDialog
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QMutex
from PyQt5.QtGui import QMovie, QImage, QPixmap, QIcon
from PyQt5 import QtGui, QtCore
import cv2 as cv
import source
import os
from MainWindow import Ui_MainWindow as MainWindow_UI
from display import Ui_MainWindow as display_UI
from members import Ui_MainWindow as members_UI
from matting import load_model, matting
import numpy as np
from client import Wire
import threading
import time
from glob import glob
import show

camera_qmut = QMutex()
ipconf = 'http://172.18.242.221:7878/predict'
VideoCaptureip = 0
savevideofps = 8
w, h = 1280, 720


class Camerathread(QThread):
    def __init__(self, MainWindow, savevideo=False, t=15, videoname=None):
        super().__init__()
        # self.w,self.h=1280,720
        self.mattingmodel, self.prec = load_model('torchscript_mobilenetv2_fp16.pth', '720p')
        self.MainWindow = MainWindow
        self.vc = cv.VideoCapture(VideoCaptureip)
        self.savevideo = savevideo
        self.t = t
        self.videoname = videoname
        self.bgr = cv.imread('bgr.jpg')
        self.bgr = cv.resize(self.bgr, (w, h))
        self.bgr = cv.cvtColor(self.bgr, cv.COLOR_BGR2RGB)
        self.index = 0

    def run(self):
        if self.vc.isOpened():  # VideoCaputre对象是否成功打开
            print('打开摄像头成功')
        else:
            print('打开摄像头或者视频失败')
            return
        wire = Wire(ipconf)
        camera_qmut.lock()
        threads = []
        cot = 0
        if self.savevideo:
            videoWriter = cv.VideoWriter(self.videoname, cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), savevideofps,
                                         (w, h))
        while self.MainWindow.isdisplay:
            success, videoframe = self.vc.read()
            assert success, 'Not get frame'

            frame = cv.cvtColor(videoframe, cv.COLOR_BGR2RGB)
            frame = cv.resize(frame, (w, h))

            cot += 1
            if cot % 10 == 0:
                try:
                    threads.append(threading.Thread(target=wire.process, args=(frame,)))
                    # threads.append(threading.Thread(target=wire.recv_label))
                    threads[0].start()
                    # threads[1].start()
                except:
                    print('can not build threads!')
            if threads:
                threads[0].join()
                # threads[1].join()
                threads = []
                if int(wire.Q) not in [0, 14, 15]:
                    self.index = int(wire.Q)
            #     print(wire.Q)
            # print(type(mat_img),type(frame))
            a = time.time() / 2
            # if int(a%15) not in [0,1,2,3,4]:
            #     self.index=int(a%15)
            mat_img = matting(self.mattingmodel, self.prec, frame, self.bgr, self.MainWindow.newbgr[self.index])
            mat_img = cv.flip(mat_img, 1)
            if self.index < 14 and self.index != 0:
                mat_img = show.draw_debug_image(mat_img, self.index)
            img = QImage(mat_img.data.tobytes(), mat_img.shape[1], mat_img.shape[0], QImage.Format_RGB888)
            self.MainWindow.displaylabel.setPixmap(QPixmap.fromImage(img))
            cv.waitKey(1)
            if self.savevideo:
                writeimg = cv.cvtColor(mat_img, cv.COLOR_RGB2BGR)
                videoWriter.write(writeimg)
                if (cot >= (self.t * savevideofps)):
                    self.MainWindow.saveButton.setEnabled(True)
                    self.MainWindow.closeButton.setEnabled(False)
                    break
        self.MainWindow.displaylabel.setPixmap(QPixmap(""))
        if self.savevideo:
            videoWriter.release()
        self.vc.release()
        camera_qmut.unlock()


class MainWindow(QMainWindow, MainWindow_UI):
    switchdisplay = pyqtSignal()
    switchmembers = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./imgs/icon.png'))

        self.beginButton.clicked.connect(self.godisplay)
        self.membersButton.clicked.connect(self.gomembers)
        self.exitButton.clicked.connect(self.close)

    def godisplay(self):
        self.switchdisplay.emit()

    def gomembers(self):
        self.switchmembers.emit()


class DisplayGUI(QMainWindow, display_UI):
    switchmainwindow = pyqtSignal()

    def __init__(self):
        super(DisplayGUI, self).__init__()
        self.setupUi(self)
        self.displaylabel.setScaledContents(True)
        self.cwd = os.getcwd()

        self.openButton.setEnabled(True)
        self.closeButton.setEnabled(False)
        self.backButton.clicked.connect(self.goMainWindow)
        self.openButton.clicked.connect(self.opencamera)
        self.closeButton.clicked.connect(self.closecamera)
        self.saveButton.clicked.connect(self.savevideo)
        self.getbgrButton.clicked.connect(self.getbgr)
        self.isdisplay = False
        # self.w,self.h=1280,720
        self.newbgr = []
        newbgrpath_list = glob('newbgr/*.jpg')
        for i in newbgrpath_list:
            newimg = cv.imread(i)
            newimg = cv.resize(newimg, (w, h))
            self.newbgr.append(cv.cvtColor(newimg, cv.COLOR_BGR2RGB))
        # self.videoWriter = cv.VideoWriter('video4.avi', cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

    def goMainWindow(self):
        self.switchmainwindow.emit()

    def opencamera(self):
        # ipconf = 'http://192.168.137.224:4747/mjpegfeed?1920x1080'
        self.openButton.setEnabled(False)
        self.closeButton.setEnabled(True)
        self.isdisplay = True
        # try:
        self.camerath = Camerathread(self)
        self.camerath.start()
        # except Exception as e:
        # print(e.args)
        # print(str(e))
        # print(repr(e))

    def closecamera(self):
        self.isdisplay = False
        self.openButton.setEnabled(True)
        self.closeButton.setEnabled(False)

    def savevideo(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "文件保存",
                                                                self.cwd,  # 起始路径
                                                                "Video Files (*.avi)")

        if fileName_choose == "":
            print("\n取消选择")
            return
        else:
            print("\n你选择要保存的文件为:")
            print(fileName_choose)
            text, ok = QInputDialog.getText(self, '解印世界-录制', '录制时间(/s)：')
            if ok and text:
                savet = int(text)
                self.saveButton.setEnabled(False)
                self.closeButton.setEnabled(True)
                self.isdisplay = True
                try:
                    self.camerath = Camerathread(self, savevideo=True, t=savet, videoname=fileName_choose)
                    self.camerath.start()
                except Exception as e:
                    print(e.args)
                    print(str(e))
                    print(repr(e))

    def getbgr(self):

        cap = cv.VideoCapture(VideoCaptureip)
        time.sleep(1)
        ret, frame = cap.read()
        cv.imwrite('bgr.jpg', frame)
        cap.release()


class MembersGUI(QMainWindow, members_UI):
    switchmainwindow = pyqtSignal()

    def __init__(self):
        super(MembersGUI, self).__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.goMainWindow)

    def goMainWindow(self):
        self.switchmainwindow.emit()


class SignetGUI():
    def __init__(self):
        self.mainwindow = MainWindow()
        # self.mainwindow.resize(1980,1024)
        self.displaygui = DisplayGUI()
        self.membersgui = MembersGUI()

        self.displaywidget = self.displaygui.centralwidget
        self.mainwidget = self.mainwindow.centralwidget
        self.memberswidget = self.membersgui.centralwidget

        self.mainwindow.switchdisplay.connect(self.showdisplay)
        self.mainwindow.switchmembers.connect(self.showmembers)

        self.displaygui.switchmainwindow.connect(self.showmainwindow)

        self.membersgui.switchmainwindow.connect(self.showmainwindow)

    def showmainwindow(self):
        self.mainwindow.takeCentralWidget()
        self.mainwindow.setCentralWidget(self.mainwidget)

    def showdisplay(self):
        self.mainwindow.takeCentralWidget()
        self.mainwindow.setCentralWidget(self.displaywidget)

    def showmembers(self):
        self.mainwindow.takeCentralWidget()
        self.mainwindow.setCentralWidget(self.memberswidget)


def main():
    app = QApplication([])
    signetgui = SignetGUI()
    signetgui.mainwindow.show()
    # signetgui.mainwindow.showFullScreen()
    app.exec_()


if __name__ == '__main__':
    main()
