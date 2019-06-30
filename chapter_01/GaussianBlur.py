#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision/lena.jpg"
image = cv2.imread(file_full_path)

#对图像做高斯平滑处理并显示
imageGauss = cv2.GaussianBlur(image, (5, 5), 0)
#对图像使用resize和pyrDown缩小一半，再一半，显示各图像
image1 = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[1]/2)))
image2 = cv2.pyrDown(image1)
#彩色转灰度并做阈值化，显示
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

__,imageGray1 = cv2.threshold(imageGray, 120, 0xff, cv2.THRESH_BINARY)

cv2.imshow("Source Image", image)
cv2.imshow("Gauss Filtered  Image", imageGauss)
cv2.imshow("Half Size Image", image1)
cv2.imshow("Quarter Size Image", image2)
cv2.imshow("Gray Image", imageGray)
cv2.imshow("threshold Image", imageGray1)

cv2.waitKey()
cv2.destroyAllWindows()