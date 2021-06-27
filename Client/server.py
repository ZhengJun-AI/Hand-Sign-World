import cv2
import numpy as np
import socket
import os
import time


def load_model():
    model = None
    return model

# the input img is an np.array(uint8)
# maybe you need to change img from 0-255 to 0-1
def get_label(model, img):
    # label = model(img)
    label = 1
    return str(label)


def recv_img(sock, count):
    buf = b''
    while count:
        newbuf=sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class Wire:
    def __init__(self, ipconf=('', 7878)):
        self.model = load_model()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(ipconf)
        self.sock.listen(100)
        print('waiting...')
        self.conn, _ = self.sock.accept()
        self.conn.send(str.encode('Connencted Sucessfully').ljust(32))

    def process(self):
        try:
            l = self.conn.recv(16).decode('utf-8')
        except:
            print('Connected Fail')
            return
            
        stringData = recv_img(self.conn, int(l))
        print('receive an image')
        img = np.frombuffer(stringData, np.uint8)
        decimg = cv2.imdecode(img, cv2.IMREAD_COLOR)
        label = get_label(self.model, decimg)
        self.conn.send(label.encode('utf-8').ljust(16))

if __name__ == '__main__':
    wire = Wire()
    while 1:
        wire.process()
