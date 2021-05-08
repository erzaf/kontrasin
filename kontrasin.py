#!/usr/bin/env python3
#Author: Erzaf

import sys, os
import cv2
import numpy as np
import argparse
import pyfiglet
import time

kontrasin = pyfiglet.figlet_format("KONTRASIN")
print(kontrasin,'By Erzaf. [Version BETA 1.0]')

pathname = os.path.dirname(sys.argv[0])
path = os.path.abspath(pathname)
time = time.time()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                required=True,
                help="Path to image, e.g: ./path/to/image.jpg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (500, 600))                               #Adjust it yourself
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=8.0, tileGridSize=(8,8))
konImg = clahe.apply(image_bw)
invImg = cv2.bitwise_not(konImg)
cv2.imshow("Original", image)
cv2.imshow("Contrasted", konImg)
cv2.imshow("Inverted", invImg)
print('Press ESC to exit')
print('Press S to save the images')
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite(os.path.join(path, './images_saved/con_result_{}.jpg'.format(time)), konImg)
    cv2.imwrite(os.path.join(path, './images_saved/inv_result_{}.jpg'.format(time)), invImg)
    cv2.destroyAllWindows()
    print('[Images successfully saved to "images_saved" directory.]')