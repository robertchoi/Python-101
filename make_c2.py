import numpy as np
import cv2
import random
 
# 이미지 읽기


for i in range(4992):
    dst = '/2_ (' + str(i+1) + ').jpg'
    img = cv2.imread('image_mixed'+ dst, 1)

    dx = random.randint(230, 820)
    dy = random.randint(360, 570)
    dw = random.randint(20, 80)
    dh = random.randint(20, 80)
    img = cv2.rectangle(img, (dx, dy), (dx+dw, dy+dh), (202,245,228), -1)
    if i>2500 :
        dx = random.randint(230, 820)
        dy = random.randint(360, 570)
        dw = random.randint(20, 80)
        dh = random.randint(20, 80)
        img = cv2.rectangle(img, (dx, dy), (dx+dw, dy+dh), (202,245,228), -1)        

    cv2.imwrite('image_mixed_out'+ dst, img)