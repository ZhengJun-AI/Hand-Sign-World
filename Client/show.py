#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import argparse
import csv
import time
import copy


import cv2 as cv
import numpy as np

from utils import CvFpsCalc
from utils import CvDrawText

with open('setting/labels.csv','r', encoding='utf8') as f:  # 印
        labels = csv.reader(f)
        labels = [row for row in labels]
font_path = './utils/font/衡山毛筆フォント.ttf'

def draw_debug_image(
    debug_image,
    class_id,
    labels=labels,
    font_path = './utils/font/衡山毛筆フォント.ttf'
):
    frame_width, frame_height = debug_image.shape[1], debug_image.shape[0]

    # 印の種類
    square_len=400
    font_size = int(square_len / 2)
    debug_image = CvDrawText.puttext(
        debug_image, labels[class_id][1],
        (1080,0), font_path,#640,360
        font_size,(0, 0, 185))

    # # ヘッダー作成：FPS #########################################################
    # header_image = np.zeros((int(frame_height / 18), frame_width, 3), np.uint8)

    # # フッター作成：印の履歴、および、術名表示 ####################################
    # footer_image = np.zeros((int(frame_height / 10), frame_width, 3), np.uint8)

    # # ヘッダーとフッターをデバッグ画像へ結合 ######################################
    # debug_image = cv.vconcat([header_image, debug_image])
    # debug_image = cv.vconcat([debug_image, footer_image])

    return debug_image

if __name__ == '__main__':
    debug_image = copy.deepcopy(frame)
    debug_image = draw_debug_image(
                debug_image,
                font_path,
                labels,
                class_id,
            )