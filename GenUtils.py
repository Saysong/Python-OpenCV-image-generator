import numpy as np
import cv2.cv2 as cv2
from matplotlib import pyplot as plt
import random
from pathlib import Path

# Directory info
#directory = './TestShapes'
#title = 'testing.png'
#filename = directory + '/' + title

# Color values according to opencv
WHITE = [255,255,255]
BLACK = [0,0,0]
GRAY = [128,128,128]
RED = [0,0,255]
BLUE = [255,0,0]
GREEN = [0,255,0]
YELLOW = [0,255,255]
PURPLE = [204,0,102]
BROWN = [0,51,102]
ORANGE = [0,128,255]
Palet = [WHITE,BLACK,GRAY,RED,BLUE,GREEN,YELLOW,PURPLE,BROWN,ORANGE]



# Drawing Shapes
def drawCircle(img, color, center = (24,24), radius = 24, thickness = -1):
    cv2.circle(img, center, radius, color, thickness)
    # Ideal lettering 
    # Thickness: 3
    # Origin: 13,35
    # Scale: 1

def drawSemiCircle(img, color, center = None, axes = (25,25), 
    angle = 0, sAngle = 0, eAngle=None, thic = -1):
    dir = random.randint(1,2)
    if center == None:
        if dir == 1:
            center = (24,14)
            eAngle = 180
        else:
            center = (24,35)
            eAngle = -180
    cv2.ellipse(img, center, axes, angle, sAngle, eAngle, color, thic)
    # Ideal lettering 
    # Thickness: 3
    # Origin: 16,33
    # Scale: 0.8

def drawQuarterCircle(img, color, center = None, axes = (40,40), 
    angle = 0, sAngle = None, eAngle=None, thic = -1):
    dir = random.randint(1,4)
    if center == None:
        #Quadrant 1
        if dir == 1:
            center = (5,44)
            sAngle = 270
            eAngle = 360
        #Quadrant 2
        elif dir == 2:
            center = (44,44)
            sAngle = 180
            eAngle = 270
        #Quadrant 3
        elif dir == 3:
            center = (44,5)
            sAngle = 90
            eAngle = 180
        #Quadrant 4
        else:
            center = (5,5)
            sAngle = 0
            eAngle = 90
    cv2.ellipse(img, center, axes, angle, sAngle, eAngle, color, thic)
    # Ideal lettering 
    # Thickness: 3
    # Origin: 16,33
    # Scale: 0.8    

def drawTriangle(img, color):
    pts = np.array([[8,40],[24,10],[42,40]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)
    

def drawSquare(img, color, pt1 = (4,4), pt2 = (45,45),thic = -1):
    cv2.rectangle(img, pt1, pt2,color,thic)

def drawRectangle(img, color, pt1 = None, pt2 = None, thic = -1):
    dir = random.randint(1,2)
    if pt1 == None and pt2 == None:
        if dir == 1:
            pt1 = (4,8)
            pt2 = (45,42)
        else:
            pt1 = (8,4)
            pt2 = (42,45)
    cv2.rectangle(img, pt1, pt2, color, thic)

def drawTrapeziod(img, color):
    pts = np.array([[0,40],[49,40],[40,8],[10,8]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img, [pts], color)

def drawPentagon(img, color):
    pts = np.array([[24,4],[44,20],[40,44],[9,44],[4,20]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

def drawHexagon(img, color):
    pts = np.array([[12,5],[38,5],[46,24],[38,45],[12,45],[4,24]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

def drawHeptagon(img, color):
    pts = np.array([[24,3],[42,13],[45,33],[35,45],[15,45],[5,33],[9,13]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

def drawOctagon(img, color):
    pts = np.array([[35,5],[45,18],[45,32],[35,45],[15,45],[5,32],[5,18],[15,5]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

def drawStar(img, color):
    pts = np.array([[24,5],[30,20],[45,20],[35,30],[40,45],[24,35],[10,45],[13,30],[5,20],[18,20]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

def drawCross(img, color):
    #pts = np.array([[20,10],[20,20],[10,20],[10,30],[20,30],[20,40],[30,40],[30,30],[40,30],[40,20],[30,20],[30,10]], np.int32)
    pts = np.array([[14,5],[14,18],[4,18],[4,33],[14,33],[14,45],[34,45],[34,33],[44,33],[44,18],[34,18],[34,5]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts], color)

#Write Letter
# NEEDS ADJUSTMENT per shape  
def drawLetter(img, letter, color, thic = 3, org = (13,35), scale = 1, font = 0 ):
    cv2.putText(img, letter, org,font,scale ,color,thic)

# Set Background
def setBackground (img):
    pass




# Generation
#p = Path('.')

class Generation():
    
    
    # Generate Images when Generation Class is called
    def __init__(self,num):
        # Shape
        self.ids = ''
        # Counter that shouldn't need to exist
        self.c = 0
        # Text color
        self.TextC = ''
        # Shape color
        self.ShapeC  = ''
        # Text
        self.Text = ''
        # Directory
        self.dir = ''
        if (num == 0):
            self.ids  = 'CIRCLE'
            Path('./' + self.ids).mkdir()
            self.genCircleImages()
        elif (num == 1):
            self.ids  = 'SEMICIRCLE'
            Path('./' + self.ids).mkdir()
            self.genSemiCircleImages()
        elif (num == 2):
            self.ids  = 'QUARTERCIRCLE'
            Path('./' + self.ids).mkdir()
            self.genQuarterCircleImages()
        elif (num == 3):
            self.ids  = 'TRIANGLE'
            Path('./' + self.ids).mkdir()
            self.genTriangleImages()
        elif (num == 4):
            self.ids  = 'SQUARE'
            Path('./' + self.ids).mkdir()
            self.genSquareImages()
        elif (num == 5):
            self.ids  = 'RECTANGLE'
            Path('./' + self.ids).mkdir()
            self.genRectangleImages()
        elif (num == 6):
            self.ids  = 'TRAPEZOID'
            Path('./' + self.ids).mkdir()
            self.genTrapeziodImages()
        elif (num == 7):
            self.ids  = 'PENTAGON'
            Path('./' + self.ids).mkdir()
            self.genPentagonImages()
        elif (num == 8):
            self.ids  = 'HEXAGON'
            Path('./' + self.ids).mkdir()
            self.genHexagonImages()
        elif (num == 9):
            self.ids  = 'HEPTAGON'
            Path('./' + self.ids).mkdir()
            self.genHeptagonImages()
        elif (num == 10):
            self.ids  = 'OCTAGON'
            Path('./' + self.ids).mkdir()
            self.genOctagonImages()
        elif (num == 11):
            self.ids  = 'STAR'
            Path('./' + self.ids).mkdir()
            self.genStarImages()
        elif (num == 12):
            self.ids  = 'CROSS'
            Path('./' + self.ids).mkdir()
            self.genCrossImages()
        
    # Assigns Text color file name
    def textCAssignment(self, count):
        if (count == 0):
            self.TextC  = 'WHITE'
        elif (count == 1):
            self.TextC  = 'BLACK'
        elif (count == 2):
            self.TextC  = 'GRAY'
        elif (count == 3):
            self.TextC  = 'RED'
        elif (count == 4):
            self.TextC  = 'BLUE'
        elif (count == 5):
            self.TextC  = 'GREEN'
        elif (count == 6):
            self.TextC  = 'YELLOW'
        elif (count == 7):
            self.TextC  = 'PURPLE'
        elif (count  == 8):
            self.TextC  = 'BROWN'
        elif (count  == 9):
            self.TextC  = 'ORANGE'


    # Assigns Shape color file name
    def ShapeCAssign(self, i):
        if (i == 0):
            self.ShapeC  = 'WHITE'
        elif (i == 1):
            self.ShapeC  = 'BLACK'
        elif (i == 2):
            self.ShapeC  = 'GRAY'
        elif (i == 3):
            self.ShapeC  = 'RED'
        elif (i == 4):
            self.ShapeC  = 'BLUE'
        elif (i == 5):
            self.ShapeC  = 'GREEN'
        elif (i == 6):
            self.ShapeC  = 'YELLOW'
        elif (i == 7):
            self.ShapeC  = 'PURPLE'
        elif (i == 8):
            self.ShapeC  = 'BROWN'
        elif (i == 9):
            self.ShapeC  = 'ORANGE'
    
    # Creates a background from a random section of the 5 images
    def setBackground(self):
        # Determines from which file to crop
        randfile = random.randint(1,5)
        xposit = random.randint(0,949)
        yposit = random.randint(0,449)
        img = cv2.imread('FieldImages/1000img' + str(randfile) +'.png')
        img = img[yposit:yposit+50, xposit:xposit+50]
        return img


    # Below are the Shape and letter generation.
    # Should shorted these methods soon

    def genCircleImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawCircle(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c])
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genCircleImages()    
                

    def genSemiCircleImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawSemiCircle(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c],3,(16,33),0.8)
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genSemiCircleImages()


    def genQuarterCircleImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawQuarterCircle(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c],3,(13,35),0.9)
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genQuarterCircleImages()
    

    def genTriangleImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawTriangle(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c],2,(17,37),0.7)
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genTriangleImages()

    def genSquareImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawSquare(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c],4,(11,38),1.3)
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genSquareImages()
            
    def genRectangleImages(self):
        self.textCAssignment(self.c)
        for i in range (0,10):
            self.ShapeCAssign(i)
            for j in range (0,26):
                img = self.setBackground()
                drawRectangle(img,Palet[i])
                drawLetter(img,str(chr(65+j)),Palet[self.c],3,(12,37),1.2)
                Text = str(chr(65+j))
                title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                filename = self.ids + '/' + title
                cv2.imwrite(filename,img)
                
        if (not(self.c == 9)):
                self.c += 1
                self.genRectangleImages()

    def genTrapeziodImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawTrapeziod(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],3,(12,35),1.1)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genTrapeziodImages()

    def genPentagonImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawPentagon(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],4,(11,39),1.2)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genPentagonImages()


    def genHexagonImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawHexagon(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],4,(10,38),1.3)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genHexagonImages()


    def genHeptagonImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawHeptagon(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],3,(14,35),1)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genHeptagonImages()


    def genOctagonImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawOctagon(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],3,(13,35),1)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genOctagonImages()


    def genStarImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawStar(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],2,(15,35),.8)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genStarImages()


    def genCrossImages(self):
            self.textCAssignment(self.c)
            for i in range (0,10):
                self.ShapeCAssign(i)
                for j in range (0,26):
                    img = self.setBackground()
                    drawCross(img,Palet[i])
                    drawLetter(img,str(chr(65+j)),Palet[self.c],3,(13,35),1)
                    Text = str(chr(65+j))
                    title = '{}_{}_{}_{}.png'.format(self.TextC, Text, self.ShapeC, self.ids)
                    filename = self.ids + '/' + title
                    cv2.imwrite(filename,img)
                
            if (not(self.c == 9)):
                    self.c += 1
                    self.genCrossImages()


        