import numpy as np
import cv2.cv2 as cv2 #fixing pylint 
from matplotlib import pyplot as plt
#import file with precoded values to look neater
import GenUtils as gen

# Make blank file
img = np.zeros((50,50,3), np.uint8)

# Naming Scheme & directory location declaration
directory = './TestShapes'
title = 'testing.png'
filename = directory + '/' + title
#gen.drawCircle(img,gen.WHITE,)
#gen.drawSquare(img,gen.Palet[3])
gen.drawRectangle(img, gen.Palet[9])
#cv2.ellipse(img,(24,14),(25,25),0,0,180,255,-1)
#cv2.ellipse(img,(5,5),(40,40),0,0,90,255,-1)
#gen.drawQuarterCircle(img, gen.Palet[5])
#gen.drawTriangle(img,gen.Palet[6])
#gen.drawTrapeziod(img, gen.Palet[2])
#gen.drawPentagon(img, gen.Palet[2])
#gen.drawQuarterCircle(img,gen.Palet[2])
#gen.drawOctagon(img,gen.Palet[3])
#gen.drawStar(img, gen.Palet[5])
#gen.drawSquare(img,gen.Palet[6])
#gen.drawTriangle(img,gen.Palet[6])
#gen.drawCross(img, gen.RED)
#gen.drawStar(img, gen.BLUE)
#gen.drawHeptagon(img,gen.RED)
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