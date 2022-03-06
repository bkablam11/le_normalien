import cv2
import numpy as np
import sys

RESIZED_IMAGE_WIDTH = 30
RESIZED_IMAGE_HEIGTH = 40

charClassifications = np.loadtxt("classifications.txt", np.float32) 
flatCharImages = np.loadtxt("flatcharImages.txt", np.float32)
charClassifications = charClassifications.reshape((charClassifications.size, 1))


# KNN
knn = cv2.ml.KNearest_create()
kNearest = knn


knn.train(flatCharImages, cv2.ml.ROW_SAMPLE, charClassifications)


imgTestSample = cv2.imread(sys.path[0]+"/test_image/001.png", 1) 

bf = cv2.bilateralFilter(imgTestSample, 50, 100, 100) 

imgGray = cv2.cvtColor(bf, cv2.COLOR_BGR2GRAY)

retval, th = cv2.threshold(imgGray, 150, 255, cv2.CHAIN_APPROX_NONE)

thCopy = th.copy()
contours, h = cv2.findContours(thCopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours, h = cv2.findContours(thCopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 


# contoursCopy = contours.copy()
contoursCopy = contours

strFinalString = ""

for c in contoursCopy:
    approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True) 
    if len(approx) == 4: 
        if len(str(cv2.contourArea(approx))) < 6:
            pass 
        else:
            [intX, intY, intW, intH] = cv2.boundingRect(approx)
            cv2.rectangle(imgTestSample, (intX, intY), (intX+intW, intY+intH), (0, 255, 0), 2)
            
            imgChar = th[intY:intY+intH, intX:intX+intW]
            imgChar = imgChar[5:50, 5:48]

            imgInv = cv2.bitwise_not(imgChar) 
            ret, th1 = cv2.threshold(imgInv, 150, 255, cv2.CHAIN_APPROX_NONE) 
            cntr, h = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
            for myc in cntr:
                [intX, intY, intW, intH] = cv2.boundingRect(myc) 
                imgROI = th1[intY:intY+intH, intX:intX+intW] 
                imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGTH))
                
                # cv2.imshow('windows', imgROIResized)
                # cv2.waitKey(0)

                finalResized = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGTH)) 
                finalResized = np.float32(finalResized)

                ret, result, neighbours, dist = kNearest.findNearest(finalResized, k=1)
                
                tmpString = str(chr(int(result[0][0])))

                strFinalString = strFinalString + tmpString


print(strFinalString)


with open('result.csv','w') as file:
    for line in strFinalString:
        file.write(line)
        file.write('\n')

