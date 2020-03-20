import numpy as np
import cv2.cv2 as cv2 #fixing pylint 
from matplotlib import pyplot as plt
#import file with precoded values to look neater
import GenUtils as gen
import random


randfile = random.randint(1,5)
xposit = random.randint(0,949)
yposit = random.randint(0,449)
img = cv2.imread('FieldImages/1000img' + str(randfile) +'.png')
img = img[yposit:yposit+50, xposit:xposit+50]

cv2.imshow("sun",img)

cv2.waitKey(0)
cv2.destroyAllWindows()