import numpy as np
import cv2
from matplotlib import pyplot as plt


if __name__ == "__main__":
    img = cv2.imread('rowing.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", img)

    #Erosion, dilatation, opening and closing
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv2.erode(gray,kernel,iterations = 1)
    # dilation = cv2.dilate(gray,kernel,iterations = 1)
    # opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    #Watershed algorithme
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow("Thresh", thresh)

    # noise removal
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    cv2.imshow("Opening", opening)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    cv2.imshow("Sure_fg", unknown)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [0,255,0]

    cv2.imshow("Image F", img)

    print(len(markers))

    # cv2.imshow("Image", img)
    # cv2.imshow("Image Gray", gray)
    # cv2.imshow("Erosion", erosion)
    # cv2.imshow("Dilatation", dilation)
    # cv2.imshow("Opening", opening)
    # cv2.imshow("Closing", closing)

    cv2.waitKey(0)
