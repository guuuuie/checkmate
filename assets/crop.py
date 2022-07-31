import cv2 as cv
import numpy as np 
import config
from time import sleep

def imageCrop(num):
    #Initializing the image
    img = cv.imread(f"{config.path}\\newChessPNGs\\realChessPNGs (coloured)\\Move" + str(num) + ".png")
    #Resizing the image for managability 
    rsz_img = cv.resize(img, None, fx=0.20, fy=0.20)

    #Creating an empty array for the mask based off the image dimmensions
    mask = np.zeros(rsz_img.shape[:2], dtype = "uint8")
    #Creating the image mask around the chess board
    mask = cv.rectangle(mask, (115,225), (500, 600), (255,255,255), -1)

    #Performing a bitwise AND operation to combine the original photo onto the mask
    result = cv.bitwise_and(rsz_img, rsz_img, mask = mask)

    #img_gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    #contours = cv.findContours(img_gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(rsz_img, contours, -1, (0,255,0), 3)

    #Defining the area of the array as the area of the contour 
    (x, y) = np.where(mask == 255)
    #Finding the top left corner of the contour
    (topx, topy) = (np.min(x), np.min(y))
    #Finding the bottom right corner of the contour
    (bottomx, bottomy) = (np.max(x), np.max(y))
    #Cropping the area enclosed by the corners
    img_final = result[topx:bottomx+1, topy:bottomy+1]

    #Writing the output image to a folder
    cv.imwrite(f"{config.path}\\cutPhotos\\Move" + str(num) + ".png", img_final)

    #cv.imwrite(f"{config.path}\\cutPhotos\\Move" + str(num) + ".png", result)
    #cv.imshow("Masked Move " + str(num), rsz_img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    


#Standard Thresholding
#ret, thresh_gray = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

#Inverted Thresholding
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY_INV)

#Otsu's Method
#ret, thresh_gray = cv.threshold(gray, 150, 55, cv.THRESH_BINARY + cv.THRESH_OTSU)

#Adaptive Mean Thresholding
#thresh_gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           #cv.THRESH_BINARY, 11, 2) 

#Adaptive Gaussian Thresholding 
#thresh_gray = cv.adaptiveThreshold(gray, 220, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
           #cv.THRESH_BINARY, 11, 2)