import numpy as np
import cv2.cv2 as cv2 #fixing pylint 
from matplotlib import pyplot as plt
#import file with precoded values to look neater
import GenUtils as gen

# Make blank file
img = np.zeros((50,50,3), np.uint8)
img = cv2.imread( 'FieldImages/imgGrass.png')

# Naming Scheme & directory location declaration
directory = './TestShapes'
title = 'testing.png'
filename = directory + '/' + title
gen.drawRectangle(img, gen.Palet[9])
gen.drawLetter(img,'Q',gen.Palet[5],3,(12,37),1.2)


# Display Window
cv2.imshow(title,img)

# Testing purposes
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(filename,img)
    cv2.destroyAllWindows()