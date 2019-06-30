#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

image = cv2.imread("/home/tianyu/software/IDEAProjects/computer_vision/lena.jpg")
cv2.imshow("hello,World", image)
cv2.waitKey()
cv2.destroyAllWindows()