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

# # WORK Drawings
# # Shape 
#cv2.circle(img,(25,25),25,gen.BROWN,-1)

# # Letter
#cv2.putText(img,'A', (10,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,gen.WHITE,5,cv2.FILLED)
# # Display window 

cv2.rectangle(img, (12,7), (37,42),gen.WHITE,-1 )
#cv2.putText(img,'T', (13,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,gen.BLUE,5,cv2.FILLED)


cv2.imshow(title,img)
#gen.drawCircle


# Here for testing purposes if files work
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(filename,img)
    cv2.destroyAllWindows()