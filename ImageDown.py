import numpy as np
import cv2.cv2 as cv2 #fixing pylint 
from matplotlib import pyplot as plt
#import file with precoded values to look neater
import GenUtils as gen
import random
#Select an image 
img = cv2.imread('FieldImages/1000img' + str(random.randint(1,1)) +'.png')

#Attempted some stuff, don't bother
#res = cv2.resize(img,(1000,500))#,None,None,None,cv2.INTER_AREA)



directory = 'FieldImages'
title = '1000'+'imgRun1.png'
filename = directory + '/' + title
# Display Window
cv2.imshow(title,img)
#cv2.imshow(title,res)

# Testing purposes
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(filename,res)
    cv2.destroyAllWindows()