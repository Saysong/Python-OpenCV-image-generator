import numpy as np
import cv2.cv2 as cv2 #fixing pylint 
from matplotlib import pyplot as plt
#import file with precoded values to look neater
import GenUtils as gen
from GenUtils import generation 
Rex = []
for i in range (13):
    Rex.append(generation(i))