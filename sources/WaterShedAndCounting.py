from __future__ import print_function
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

# python3 WaterShedAndCounting.py '../dataset/training/image-10.png'

def show(img):
    '''Fuinction for show img'''
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        '''Test if filename is present in args'''
        print("Error bad args!")
        exit(0)

    img = cv2.imread(sys.argv[1])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # preprocessing the image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    show(hsv)

    h, s, v = cv2.split(hsv)
    show(s)

    _, thr = cv2.threshold(s, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    show(thr)

    blur = cv2.medianBlur(thr, 5)
    show(blur)

    contours, hierarchy = cv2.findContours(
        blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = []
    for x in contours:
        area = cv2.contourArea(x)
        if area > 1000:
            count.append(x)

    D = ndimage.distance_transform_edt(thr)
    localMax = peak_local_max(D, indices=False, min_distance=40, labels=thr)
    markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
    labels = watershed(-D, markers, mask=thr)
    ws = len(np.unique(labels)) - 1

    #Count number of segmentation
    ans = int((ws + len(count)) / 2)
    print("number of blood cells segments detected = ", ans)
    cv2.drawContours(img, count, -1, (255, 0, 0), 3)
    show(img)
