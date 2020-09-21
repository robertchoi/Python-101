import numpy as np
import cv2
import random
 
# 이미지 읽기


for i in range(4992):
    dst = '/1_ (' + str(i+1) + ').jpg'
#img = cv2.imread('image_black/1_ (1).jpg', 1)
    img = cv2.imread('image_black'+ dst, 1)

    dx = random.randint(230, 820)
    dy = random.randint(360, 570)
    dw = random.randint(20, 80)
    dh = random.randint(20, 80)
    img = cv2.rectangle(img, (dx, dy), (dx+dw, dy+dh), (0,0,0), -1)
# 이미지 화면에 표시
#cv2.imshow('Test Image', img)
# 이미지 다른 파일로 저장
#cv2.imwrite('image_black_out/1_ (1).jpg', img)
    if i>2500 :
        dx = random.randint(230, 820)
        dy = random.randint(360, 570)
        dw = random.randint(20, 80)
        dh = random.randint(20, 80)
        img = cv2.rectangle(img, (dx, dy), (dx+dw, dy+dh), (0,0,0), -1)        

    cv2.imwrite('image_black_out'+ dst, img)