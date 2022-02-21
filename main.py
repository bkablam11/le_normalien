import numpy as np 
import cv2

RESIZED_IMAGE_WIDTH = 30 
RESIZED_IMAGE_HEIGHT = 40

charB = 66
charC = 67


imgTrainingB = cv2.imread("b/b.png")
imgTrainingC = cv2.imread("c/c.png")
#imgTrainingX = cv2.imread("x/x.jpg")
#imgTrainingZ = cv2.imread("z/z.jpg")

imgGrayB = cv2.cvtColor(imgTrainingB, cv2.COLOR_BGR2GRAY) 
imgGrayC = cv2.cvtColor(imgTrainingC, cv2.COLOR_BGR2GRAY) 
#imgGrayX = cv2.cvtColor(img Trainingx, cv2.COLOR_BGR2GRAY) 
#imgGrayZ = cv2.cvtColor(imgTrainingz, cv2.COLOR_BGR2GRAY),

retvaleB, imgThreshB = cv2.threshold(imgGrayB, 150, 255, cv2.CHAIN_APPROX_NONE)
retvalC, imgThreshC = cv2. threshold(imgGrayC, 150, 255, cv2.CHAIN_APPROX_NONE) 
#retvalX, imgThreshX = cv2.threshold(imgGrayx, 150, 255, cv2.CHAIN_APPROX_NONE)
#retvalz, img ThreshZ = cv2. threshold(imgGrayz, 150, 255, cv2.CHAIN_APPROX_NONE)

imgThreshCopyB = imgThreshB.copy()
imgThreshCopyC = imgThreshC.copy()

imgContoursB, hB = cv2.findContours(imgThreshCopyB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imgContoursC, hC = cv2.findContours(imgThreshCopyB, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


flattenedImages = np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)) 

intClassifications = []

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


fltClassifications = np.array(intClassifications, np.float64)
finalClassifications = fltClassifications.reshape(fltClassifications.size, 1)


print("Complete!!!")
np.savetxt("classifications.txt", finalClassifications)
np.savetxt("flatchar Images.txt", flattenedImages)


