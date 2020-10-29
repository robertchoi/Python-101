import numpy as np
import cv2
import random
import os
 
# 이미지 읽기

dirPath = os.path.dirname(os.path.realpath(__file__)) 
folderList = os.listdir(dirPath)

for i in range(38*50):
    dst = '\\'+'1_ (' + str((i%38)+1) + ').jpg'
#    dst = '\\'+'1_ (' + '%04d' % (i+1) + ').jpg'
#img = cv2.imread('image_black/1_ (1).jpg', 1)
    img = cv2.imread(dirPath + dst, 1)

    dx = random.randint(230, 1600/2)
    dy = random.randint(36, 450)
    dw = random.randint(20, 280)
    dh = random.randint(20, 280)
    img = cv2.rectangle(img, (dx, dy), (dx+dw, dy+dh), (202,245,228), -1)
    dst = '\\'+'2_ (' + str(i+1) + ').jpg'
    cv2.imwrite('d:\\github\\Python-101\\img\\' + dst, img)
    filepath = 'd:\\github\\Python-101\\img\\' + dst
    s = os.path.splitext(filepath)
    f = open(s[0]+'.txt', 'a')
    f.write("0 0.500000 0.500000 0.700000 0.900000\n")
 #   print("%d %d %d %d" % (dx, dy, dw, dh))
    f.write("2 %.6f %.6f %.6f %.6f\n" % ((dx+(dw/2))/1600, (dy+(dh/2))/464, dw/1600, dh/464))