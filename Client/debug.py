from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QMovie,QImage,QPixmap
import cv2 as cv
import threading
import source
from glob import glob
import show
import copy
# cap = cv.VideoCapture("rtsp://admin:Supcon1304@172.20.1.126:554/h264/ch1/main/av_stream")
# w,h=1280,720
# img=cv.imread('bgr.jpg')
# img=cv.resize(img,(w,h))
# debug_image = copy.deepcopy(img)
# print(debug_image.shape)
# debug_image=show.draw_debug_image(debug_image,5)
# print(debug_image.shape)
# cv.imshow('a',debug_image)
# cv.waitKey()

# newbgr=[]
# print(newbgrpath_list)
# for i in newbgrpath_list:
#     print(i)
#     newimg=cv.imread(i)
#     newimg=cv.resize(newimg,(w,h))
#     newbgr.append(cv.cvtColor(newimg,cv.COLOR_BGR2RGB))
# import itchat
# itchat.auto_login()
# # 请确保该程序目录下存在：demo.mp4
# itchat.send_file('bgr.jpg')
import pygame
# 音乐的路径
file=r'D:\CloudMusic\aa.mp3'
# 初始化
pygame.mixer.init()
# 加载音乐文件
track = pygame.mixer.music.load(file)
# 开始播放音乐流
pygame.mixer.music.play()
