#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
file_full_path = "/home/tianyu/software/IDEAProjects/computer_vision/lena.jpg"
image = cv2.imread(file_full_path)

#彩色转灰度并做阈值化，显示
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow("Source Image", image)

cv2.imshow("Gray Image", imageGray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Hue", hsv[:,:, 0])
cv2.imshow("Saturation", hsv[:,:, 1])
cv2.imshow("Value", hsv[:,:, 2])
cv2.waitKey()

cv2.imshow("Blue", image[:,:, 0])
cv2.imshow("Green", image[:,:, 1])
cv2.imshow("Red", image[:,:, 2])
cv2.waitKey()
cv2.destroyAllWindows()