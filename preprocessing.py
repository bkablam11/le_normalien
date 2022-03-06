import numpy as np 
import cv2

RESIZED_IMAGE_WIDTH = 30 
RESIZED_IMAGE_HEIGHT = 40

charA = 66
charB = 66
charC = 67
charD = 68
charV = 118
charF = 102

imgTrainingA = cv2.imread("./data/A/A.jpg")
imgTrainingB = cv2.imread("./data/B/B.jpg")
imgTrainingC = cv2.imread("./data/C/C.jpg")
imgTrainingD = cv2.imread("./data/D/D.jpg")
imgTrainingF = cv2.imread("./data/F/F.jpg")
imgTrainingV = cv2.imread("./data/V/V.jpg")

imgGrayA = cv2.cvtColor(imgTrainingA, cv2.COLOR_BGR2GRAY)
imgGrayB = cv2.cvtColor(imgTrainingB, cv2.COLOR_BGR2GRAY)
imgGrayC = cv2.cvtColor(imgTrainingC, cv2.COLOR_BGR2GRAY)
imgGrayD = cv2.cvtColor(imgTrainingD, cv2.COLOR_BGR2GRAY)
imgGrayF = cv2.cvtColor(imgTrainingF, cv2.COLOR_BGR2GRAY)
imgGrayV = cv2.cvtColor(imgTrainingV, cv2.COLOR_BGR2GRAY)


retvalA, imgThreshA = cv2.threshold(imgGrayA, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalB, imgThreshB = cv2.threshold(imgGrayB, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalC, imgThreshC = cv2. threshold(imgGrayC, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalD, imgThreshD = cv2. threshold(imgGrayD, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalF, imgThreshF = cv2. threshold(imgGrayF, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalV, imgThreshV = cv2. threshold(imgGrayV, 150, 255, cv2.CHAIN_APPROX_NONE)

imgThreshCopyA = imgThreshA.copy()
imgThreshCopyB = imgThreshB.copy()
imgThreshCopyC = imgThreshC.copy()
imgThreshCopyD = imgThreshD.copy()
imgThreshCopyF = imgThreshF.copy()
imgThreshCopyV = imgThreshV.copy()


imgContoursA, hA = cv2.findContours(imgThreshCopyA, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursB, hB = cv2.findContours(imgThreshCopyB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursC, hC = cv2.findContours(imgThreshCopyB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursD, hD = cv2.findContours(imgThreshCopyD, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursF, hF = cv2.findContours(imgThreshCopyF, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursV, hV = cv2.findContours(imgThreshCopyV, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


flattenedImages = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)) 

intClassifications = []

for cA in imgContoursA:
    [intX, intY, intW, intH] = cv2.boundingRect(cA)
    imgROIA = imgThreshA[intY:intY+intH, intX:intX + intW]
    imgResizedROIA = cv2.resize(imgROIA, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charA)
    flattenImg = imgResizedROIA.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

for cB in imgContoursB:
    [intX, intY, intW, intH] = cv2.boundingRect(cB) 
    imgROIB = imgThreshB[intY:intY+intH, intX:intX + intW]
    imgResizedROIB = cv2.resize(imgROIB, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charB)
    flattenImg = imgResizedROIB.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

for cC in imgContoursC:
    [intX, intY, intW, intH] = cv2.boundingRect(cC) 
    imgROIC = imgThreshC[intY:intY+intH, intX:intX + intW]
    imgResizedROIC = cv2.resize(imgROIC, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charC)
    flattenImg = imgResizedROIC.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

for cD in imgContoursD:
    [intX, intY, intW, intH] = cv2.boundingRect(cD)
    imgROID = imgThreshD[intY:intY+intH, intX:intX + intW]
    imgResizedROID = cv2.resize(imgROID, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charD)
    flattenImg = imgResizedROID.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

for cF in imgContoursF:
    [intX, intY, intW, intH] = cv2.boundingRect(cF)
    imgROIF = imgThreshF[intY:intY+intH, intX:intX + intW]
    imgResizedROIF = cv2.resize(imgROIF, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charF)
    flattenImg = imgResizedROIF.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

for cV in imgContoursV:
    [intX, intY, intW, intH] = cv2.boundingRect(cV)
    imgROIV = imgThreshV[intY:intY+intH, intX:intX + intW]
    imgResizedROIV = cv2.resize(imgROIV, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

    intClassifications.append(charV)
    flattenImg = imgResizedROIV.reshape(1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)
    flattenedImages = np.append(flattenedImages, flattenImg, 0)

fltClassifications = np.array(intClassifications, np.float64)
finalClassifications = fltClassifications.reshape(fltClassifications.size, 1)


print("\nComplete!!!\n")

np.savetxt("classifications.txt", finalClassifications)
np.savetxt("flatcharImages.txt", flattenedImages)