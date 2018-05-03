from pygame import *
from math import *
import random

init()
dimensions = (1000, 700)  
screen = display.set_mode(dimensions)

#Colours 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
MINTGREEN = (62, 180, 137)
FORESTGREEN = (34,139,34)
BLUE = (0, 0, 255)
MEDIUMBLUE = (0,0,205)
POWDERBLUE = (176,224,230)
SKYBLUE = (135, 206, 235)
PINK = (255, 105, 180)
DEEPPINK = (255, 20, 147)
DARKPINK = (193, 41, 87)
LIGHTPINK = (231, 84, 128)
MISTYROSE = (255, 228, 225)
PURPLE = (128, 0, 128)
DARKVIOLET = (148,0,211)
ORANGE = (255, 165, 0)
PEACH = (255, 218, 185)
GREY = (220,220,220)
LIGHTGREY = (217, 208, 200)
MINT = (152, 255, 152)
LIGHTBROWN = (204, 102, 0)
DARKBROWN = (101, 67, 33)
MEDIUMBROWN = (139, 103, 66)
LIGHTESTBROWN = (177, 144, 111)
BRICK = (150, 22, 11)
BEIGE = (215, 191, 167)
YELLOW = (255, 255, 0)


def drawScene():
    screen.fill(WHITE)

#1 stands for the coloured in shape
#2 stands for the outline of the shape

def houseOutline():
    draw.polygon(screen, LIGHTPINK, [[470, 255], [485, 255], [535, 285], [535, 315], [510, 315], [510, 395], [485, 395], [470, 410]])   #1
    draw.polygon(screen, BLACK, [[470, 255], [485, 255], [535, 285], [535, 315], [510, 315], [510, 395], [485, 395], [470, 410]], 3)    #2
    draw.polygon(screen, LIGHTPINK, [[295, 255], [325, 255], [325, 420], [295, 410]])   #1
    draw.polygon(screen, BLACK, [[295, 255], [325, 255], [325, 420], [295, 410]], 3)    #2
    draw.polygon(screen, MISTYROSE, [[510, 315], [820, 315], [795, 350], [510, 350]])   #1    
    draw.polygon(screen, BLACK, [[510, 315], [820, 315], [795, 350], [510, 350]], 3)    #2
    draw.polygon(screen, MISTYROSE, [[195, 330], [295, 330], [295, 355], [220, 355]])   #1
    draw.polygon(screen, BLACK, [[195, 330], [295, 330], [295, 355], [220, 355]], 3)    #2
    draw.polygon(screen, DEEPPINK, [[195, 330], [295, 315], [295, 330]])    #1
    draw.polygon(screen, BLACK, [[195, 330], [295, 315], [295, 330]], 3)    #2
    draw.polygon(screen, DEEPPINK, [[535, 285], [795, 315], [535, 315]])    #1
    draw.polygon(screen, BLACK, [[535, 285], [795, 315], [535, 315]], 3)    #2
    draw.polygon(screen, DARKPINK, [[325, 255], [470, 255], [470, 410], [475, 420], [325, 420]])    #1
    draw.polygon(screen, BLACK, [[325, 255], [470, 255], [470, 410], [475, 420], [325, 420]], 3)    #2
    draw.rect(screen, DEEPPINK, [510, 350, 285, 260])   #1
    draw.rect(screen, BLACK, [510, 350, 285, 260], 3)   #2
    draw.polygon(screen, DEEPPINK, [[450, 430], [580, 415], [580, 575], [450, 575]])    #1
    draw.polygon(screen, BLACK, [[450, 430], [580, 415], [580, 575], [450, 575]], 3)    #2
    draw.rect(screen, DEEPPINK, [150,600,50,50])    #1
    draw.rect(screen, BLACK, [150,600,50,50], 3)    #2
    draw.rect(screen, PURPLE, [165, 500, 20, 100])  #1
    draw.rect(screen, BLACK, [165, 500, 20, 100], 3)    #2
    draw.rect(screen, LIGHTBROWN, [200, 500, 250,150])  #1
    draw.rect(screen, BLACK, [200, 500, 250,150], 3)    #2
    
    #Garage Vertical Lines Outline
    draw.line(screen, BLACK, [200, 515], [450, 515], 3) 
    draw.line(screen, BLACK, [200, 545], [450, 545], 3)
    draw.line(screen, BLACK, [200, 575], [450, 575], 3)
    draw.line(screen, BLACK, [200, 605], [450, 605], 3)
    draw.line(screen, BLACK, [200, 635], [450, 635], 3)
    
    draw.rect(screen, DEEPPINK, [150, 480, 325, 20])    #1
    draw.rect(screen, BLACK, [150, 480, 325, 20], 3)    #2
    draw.rect(screen, DEEPPINK, [310, 230, 175, 25])    #1
    draw.rect(screen, BLACK, [310, 230, 175, 25], 3)    #2
    draw.rect(screen, BRICK, [450, 575, 350, 75])   #1
    draw.rect(screen, BLACK, [450, 575, 350, 75], 3)    #2
    draw.rect(screen, DEEPPINK, [510, 380, 245, 3])     #1
    draw.rect(screen, BLACK, [510, 380, 245, 15], 3)    #2
    draw.rect(screen, PINK, [220, 430, 230, 50])    #1
    draw.rect(screen, BLACK, [220, 430, 230, 50], 3)    #2
    draw.polygon(screen, PINK, [[330, 230], [460, 230], [395, 200]])    #1
    draw.polygon(screen, BLACK, [[330, 230], [460, 230], [395, 200]], 3)    #2
    draw.polygon(screen, PINK, [[150, 480], [125, 480], [125, 455], [150, 455], [220, 430], [220, 480]])    #1
    draw.polygon(screen, BLACK, [[150, 480], [125, 480], [125, 455], [150, 455], [220, 430], [220, 480]], 3)    #2
    draw.polygon(screen, DEEPPINK, [[755, 380], [510, 380], [510, 395], [755, 395]])    #1
    draw.polygon(screen, BLACK, [[755, 380], [510, 380], [510, 395], [755, 395]], 3)    #2
    draw.polygon(screen, PINK, [[220, 355], [295, 355], [295, 410], [220, 430]])    #1
    draw.polygon(screen, BLACK, [[220, 355], [295, 355], [295, 410], [220, 430]], 3)    #2
    draw.rect(screen, BLACK, [310, 230, 175, 25], 3) 
    draw.polygon(screen, BLACK, [[330, 230], [460, 230], [395, 200]], 3)
    draw.polygon(screen, DEEPPINK, [[220, 430], [295, 410], [325, 420], [460, 420], [445, 430]])    #1
    draw.polygon(screen, BLACK, [[220, 430], [295, 410], [325, 420], [460, 420], [445, 430]], 3)    #2
    draw.polygon(screen, DEEPPINK, [[445, 430], [485, 395], [510, 395], [570, 395], [570, 415]])    #1
    draw.polygon(screen, BLACK, [[445, 430], [485, 395], [510, 395], [570, 395], [570, 415]], 3)    #2
    draw.polygon(screen, POWDERBLUE, [[475, 455], [550, 445], [550, 575], [475, 575]])  #1
    draw.polygon(screen, BLACK, [[475, 455], [550, 445], [550, 575], [475, 575]], 3)    #2
    draw.polygon(screen, POWDERBLUE, [[795, 455], [715, 445], [715, 573], [795, 573]])  #1
    draw.polygon(screen, BLACK, [[795, 455], [715, 445], [715, 575], [795, 575]], 3)    #2
    draw.rect(screen, PINK, [530, 395, 205, 15]) #1
    draw.rect(screen, BLACK, [530, 395, 205, 15], 3) #2
    
    #Outlines
    draw.rect(screen, BLACK, [150, 480, 325, 20], 3)
    draw.rect(screen, BLACK, [165, 500, 20, 100], 3)
    draw.rect(screen, BLACK, [150,600,50,50], 3) 
    draw.line(screen, BLACK, [260, 355], [260, 420], 3)
    draw.line(screen, BLACK, [150, 455], [150, 480], 3)
    draw.line(screen, BLACK, [185, 445], [185, 480], 3)
    draw.line(screen, BLACK, [125, 480], [475, 480], 3)
    draw.line(screen, BLACK, [150, 455], [220, 430], 3)
    draw.line(screen, BLACK, [125, 455], [150, 455], 3)
    draw.line(screen, BLACK, [125, 480], [125, 455], 3)
    draw.line(screen, BLACK, [260, 430], [260, 480], 3)
    draw.line(screen, BLACK, [300, 430], [300, 480], 3)
    draw.line(screen, BLACK, [340, 430], [340, 480], 3)
    draw.line(screen, BLACK, [380, 430], [380, 480], 3)
    draw.line(screen, BLACK, [450, 430], [450, 480], 3)
    draw.line(screen, BLACK, [420, 430], [420, 480], 3)
    draw.line(screen, BLACK, [685, 415], [795, 430], 4)
  
def garageWindows():
    draw.rect(screen, SKYBLUE, [225, 525, 50, 25])
    draw.rect(screen, BLACK, [225, 525, 50, 25], 3)
    draw.rect(screen, SKYBLUE, [300, 525, 50, 25])
    draw.rect(screen, BLACK, [300, 525, 50, 25], 3)
    draw.rect(screen, SKYBLUE, [375, 525, 50, 25])
    draw.rect(screen, BLACK, [375, 525, 50, 25], 3)
    draw.line(screen, BLACK, [250, 525], [250, 550], 3)
    draw.line(screen, BLACK, [225, 537], [275, 537], 3)
    draw.line(screen, BLACK, [325, 525], [325, 550], 3)
    draw.line(screen, BLACK, [300, 537], [350, 537], 3)
    draw.line(screen, BLACK, [400, 525], [400, 550], 3)
    draw.line(screen, BLACK, [375, 537], [425, 537], 3)
    draw.line(screen, BLACK, [305, 620], [345, 620], 3) 
    draw.line(screen, BLACK, [305, 620], [300, 625], 3)     #Garage handle
    draw.line(screen, BLACK, [345, 620], [350, 625], 3) 

def door():
    draw.rect(screen, BRICK, [570, 410, 125, 165])      #Door Background
    draw.rect(screen, BLACK, [570, 410, 125, 165], 3)
    draw.rect(screen, LIGHTBROWN, [595, 430, 75, 145])
    draw.rect(screen, BLACK, [595, 430, 75, 145], 3)
    draw.line(screen, BLACK, [610, 430], [610, 575], 3)
    draw.line(screen, BLACK, [625, 430], [625, 575], 3)
    draw.line(screen, BLACK, [640, 430], [640, 575], 3)
    draw.line(screen, BLACK, [655, 430], [655, 575], 3)
    draw.circle(screen, BLACK, [655, 510], 6)
    draw.circle(screen, WHITE, [655, 510], 2)

def steps(): #Underneath door 
    draw.rect(screen, GREY, [530, 620, 200, 30])
    draw.rect(screen, BLACK, [530, 620, 200, 30], 3)
    draw.rect(screen, LIGHTGREY, [550, 600, 160, 20])
    draw.rect(screen, BLACK, [550, 600, 160, 20], 3)
    draw.rect(screen, GREY, [570, 585, 120, 15])
    draw.rect(screen, BLACK, [570, 585, 120, 15], 3)
    draw.rect(screen, LIGHTGREY, [595, 575, 75, 10])
    draw.rect(screen, BLACK, [595, 575, 75, 10], 3)
    
def chimney(): #Made of bricks
    draw.polygon(screen, LIGHTBROWN, [[610, 295], [610, 240], [660, 240], [660, 300]])
    draw.polygon(screen, BLACK, [[610, 295], [610, 240], [660, 240], [660, 300]], 3)
    draw.rect(screen, BRICK, [600, 215, 70, 25])
    draw.rect(screen, BLACK , [600, 215, 70, 25], 3)
    draw.line(screen, BLACK, [610, 295], [610, 240], 3)
    draw.line(screen, BLACK, [660, 300], [660, 240], 3)
    draw.line(screen, BLACK, [614, 215], [614, 240], 3)
    draw.line(screen, BLACK, [628, 215], [628, 240], 3)
    draw.line(screen, BLACK, [642, 215], [642, 240], 3)
    draw.line(screen, BLACK, [656, 215], [656, 240], 3)
    draw.line(screen, BLACK, [610, 250], [660, 250], 3)
    draw.line(screen, BLACK, [610, 260], [660, 260], 3)
    draw.line(screen, BLACK, [610, 270], [660, 270], 3)
    draw.line(screen, BLACK, [610, 280], [660, 280], 3)
    draw.line(screen, BLACK, [610, 290], [660, 290], 3)
    draw.line(screen, BLACK, [620, 240], [620, 250], 3)
    draw.line(screen, BLACK, [635, 240], [635, 250], 3)
    draw.line(screen, BLACK, [650, 240], [650, 250], 3)
    draw.line(screen, BLACK, [627, 250], [627, 260], 3)
    draw.line(screen, BLACK, [642, 250], [642, 260], 3)
    draw.line(screen, BLACK, [620, 260], [620, 270], 3)
    draw.line(screen, BLACK, [635, 260], [635, 270], 3)
    draw.line(screen, BLACK, [650, 260], [650, 270], 3)    
    draw.line(screen, BLACK, [627, 270], [627, 280], 3)
    draw.line(screen, BLACK, [642, 270], [642, 280], 3)
    draw.line(screen, BLACK, [620, 280], [620, 290], 3)
    draw.line(screen, BLACK, [635, 280], [635, 290], 3)
    draw.line(screen, BLACK, [650, 280], [650, 290], 3)
    draw.line(screen, BLACK, [627, 290], [627, 296], 3)
    draw.line(screen, BLACK, [642, 290], [642, 296], 3)
    
def window(): #Highest window
    draw.rect(screen, POWDERBLUE, [350, 325, 90, 75])
    draw.rect(screen, BLACK, [350, 325, 90, 75], 3)
    draw.rect(screen, BRICK, [345, 315, 100, 10])
    draw.rect(screen, BLACK, [345, 315, 100, 10], 3)
    draw.line(screen, BLACK, [395, 325], [395, 400], 4)
    draw.line(screen, BLACK, [350, 362], [440, 362], 4)
    draw.line(screen, BLUE, [355, 335], [360, 330], 3)
    draw.line(screen, BLUE, [356, 345], [374, 330], 3)
    draw.line(screen, BLUE, [358, 355], [388, 330], 3)

def windowArc(): #Arc above the window 
    draw.circle(screen, POWDERBLUE, [395, 315], 44)
    draw.circle(screen, BLACK, [395, 315], 44, 3)

def stars(): #Only during nighttime (if/else statements below)
    xRand = random.randint(0, 1000)
    yRand = random.randint(0, 300)
    draw.circle(screen, WHITE, [xRand, yRand], 3)
    
def clouds():
    xRand = random.randint(0, 800)
    yRand = random.randint(0, 50)
    draw.circle(screen, WHITE, [xRand + 100, yRand + 100], 30)
    draw.circle(screen, GREY, [xRand + 100, yRand + 100], 30, 8)
    draw.rect(screen, WHITE, [xRand + 100, yRand + 70, 100, 60])
    draw.circle(screen, WHITE, [xRand + 200, yRand + 100], 30)
    draw.circle(screen, WHITE, [xRand + 125, yRand + 70], 35)
    draw.circle(screen, WHITE, [xRand + 175, yRand + 70], 35)
    draw.line(screen, GREY, [xRand + 100, yRand + 126], [xRand + 200, yRand + 126], 7)    

def sky():      #Sky has 2 options; daytime and nighttime
    Color = (MEDIUMBLUE,SKYBLUE)
    rand = random.choice(Color)
    draw.rect(screen, rand, [0, 0, 1000, 515])
    if rand == SKYBLUE:
        draw.circle(screen, YELLOW, [850, 125], 70)
        draw.rect(screen, GREEN, [0, 515, 1000, 515])
        draw.line(screen, BLACK, [0, 515], [1000, 515], 3)
        
        for i in range(5): #Calling function clouds repeatedly 5 times
            clouds()
            
    else:
        for i in range(150): #Calling function stars repeatedly 100 times
            stars()
        draw.rect(screen, DARKGREEN, [0, 515, 1000, 515])
        draw.line(screen, BLACK, [0, 515], [1000, 515], 3)
        draw.circle(screen, GREY, [850, 125], 70)
        draw.circle(screen, MEDIUMBLUE, [880, 125], 60)
        
def rails(): #Rails beside door
        draw.line(screen, DARKBROWN, [470, 515], [555, 500], 6)
        draw.line(screen, BLACK, [490, 512], [490, 575], 6)
        draw.line(screen, BLACK, [512, 509], [512, 575], 6)
        draw.line(screen, BLACK, [534, 506], [534, 575], 6)
        draw.line(screen, DARKBROWN, [710, 500], [800, 515], 6)
        draw.line(screen, BLACK, [730, 503], [730, 575], 6)
        draw.line(screen, BLACK, [752, 506], [752, 575], 6)
        draw.line(screen, BLACK, [774, 509], [774, 575], 6)
    
def rabbit(): #Changes positioning a little on the left side of the house
    xPosition = random.randint(0, 50) 
    yPosition = random.randint(0, 60) 
    #BodyOutline
    draw.rect(screen, BLACK, [24+ xPosition, 510+ yPosition, 4, 4])
    draw.rect(screen, BLACK, [28+ xPosition, 514+ yPosition, 10, 4])
    draw.rect(screen, BLACK, [30+ xPosition, 522+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [34+ xPosition, 532+ yPosition, 4, 4])
    draw.rect(screen, BLACK, [38+ xPosition, 536+ yPosition, 4, 12])
    draw.rect(screen, BLACK, [34+ xPosition, 548+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [34+ xPosition, 552+ yPosition, 10, 4])
    draw.rect(screen, BLACK, [42+ xPosition, 548+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [46+ xPosition, 542+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [46+ xPosition, 540+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [50+ xPosition, 532+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [54+ xPosition, 528+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [54+ xPosition, 542+ yPosition, 4, 7])
    draw.rect(screen, BLACK, [50+ xPosition, 548+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [50+ xPosition, 552+ yPosition, 34, 4])
    draw.rect(screen, BLACK, [34+ xPosition, 518+ yPosition, 4, 4])
    draw.rect(screen, BLACK, [20+ xPosition, 500+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [24+ xPosition, 492+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [28+ xPosition, 488+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [36+ xPosition, 478+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [40+ xPosition, 470+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [44+ xPosition, 466+ yPosition, 4, 4])
    draw.rect(screen, BLACK, [48+ xPosition, 462+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [52+ xPosition, 466+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [56+ xPosition, 474+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [52+ xPosition, 482+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [48+ xPosition, 490+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [52+ xPosition, 498+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [56+ xPosition, 508+ yPosition, 4, 4])
    draw.rect(screen, BLACK, [60+ xPosition, 512+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [68+ xPosition, 516+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [76+ xPosition, 520+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [84+ xPosition, 524+ yPosition, 4, 8])
    draw.rect(screen, BLACK, [88+ xPosition, 532+ yPosition, 4, 16])
    draw.rect(screen, BLACK, [84+ xPosition, 548+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [92+ xPosition, 540+ yPosition, 6, 4])
    draw.rect(screen, BLACK, [98+ xPosition, 536+ yPosition, 8, 4])
    draw.rect(screen, BLACK, [106+ xPosition, 540+ yPosition, 4, 10])
    draw.rect(screen, BLACK, [92+ xPosition, 550+ yPosition, 14, 4])
    draw.rect(screen, PINK, [40+ xPosition, 484 + yPosition, 4, 4])
    draw.rect(screen, PINK, [44+ xPosition, 476 + yPosition, 4, 8])
    draw.rect(screen, DEEPPINK, [48+ xPosition, 472+ yPosition, 4, 8])
    #BodyColour
    draw.rect(screen, WHITE, [48+ xPosition, 464+ yPosition, 4, 8])
    draw.rect(screen, LIGHTGREY, [52+ xPosition, 474+ yPosition, 4, 8])
    draw.rect(screen, LIGHTGREY, [48+ xPosition, 498+ yPosition, 4, 12])
    draw.rect(screen, LIGHTGREY, [52+ xPosition, 506+ yPosition, 4, 8])
    draw.rect(screen, LIGHTGREY, [56+ xPosition, 512+ yPosition, 4, 6])
    draw.rect(screen, LIGHTGREY, [60+ xPosition, 516+ yPosition, 8, 6])
    draw.rect(screen, LIGHTGREY, [68+ xPosition, 520+ yPosition, 8, 2])
    draw.rect(screen, LIGHTGREY, [76+ xPosition, 524+ yPosition, 8, 4])
    draw.rect(screen, LIGHTGREY, [84+ xPosition, 532+ yPosition, 4, 16])
    draw.rect(screen, LIGHTGREY, [78+ xPosition, 540+ yPosition, 6, 12])
    draw.rect(screen, WHITE, [44+ xPosition, 470+ yPosition, 4, 6])
    draw.rect(screen, WHITE, [40+ xPosition, 478+ yPosition, 4, 6])
    draw.rect(screen, WHITE, [44+ xPosition, 484+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [48+ xPosition, 480+ yPosition, 4, 4])
    draw.rect(screen, LIGHTGREY, [48+ xPosition, 484+ yPosition, 4, 6])
    draw.rect(screen, WHITE, [36+ xPosition, 488+ yPosition, 12, 4])
    draw.rect(screen, WHITE, [28+ xPosition, 492+ yPosition, 16, 8])
    draw.rect(screen, LIGHTGREY, [44+ xPosition, 492+ yPosition, 4, 8])
    draw.rect(screen, WHITE, [28+ xPosition, 496+ yPosition, 16, 8])
    draw.rect(screen, WHITE, [24+ xPosition, 500+ yPosition, 24, 10])
    draw.rect(screen, BLACK, [32+ xPosition, 500+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [28+ xPosition, 510+ yPosition, 24, 4])
    draw.rect(screen, WHITE, [38+ xPosition, 514+ yPosition, 18, 4])
    draw.rect(screen, LIGHTGREY, [38+ xPosition, 518+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [42+ xPosition, 518+ yPosition, 18, 4])
    draw.rect(screen, LIGHTGREY, [34+ xPosition, 522+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [38+ xPosition, 522+ yPosition, 38, 4])
    draw.rect(screen, WHITE, [34+ xPosition, 526+ yPosition, 42, 2])
    draw.rect(screen, LIGHTGREY, [50+ xPosition, 528+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [34+ xPosition, 528+ yPosition, 16, 4])
    draw.rect(screen, WHITE, [38+ xPosition, 532+ yPosition, 8, 4])
    draw.rect(screen, LIGHTGREY, [46+ xPosition, 532+ yPosition, 4, 8])
    draw.rect(screen, WHITE, [42+ xPosition, 536+ yPosition, 4, 12])
    draw.rect(screen, WHITE, [38+ xPosition, 548+ yPosition, 4, 4])
    draw.rect(screen, LIGHTGREY, [50+ xPosition, 544+ yPosition, 4, 4])
    draw.rect(screen, WHITE, [60+ xPosition, 528+ yPosition, 24, 4])
    draw.rect(screen, WHITE, [54+ xPosition, 532+ yPosition, 30, 10])
    draw.rect(screen, WHITE, [58+ xPosition, 542+ yPosition, 20, 8])
    draw.rect(screen, WHITE, [54+ xPosition, 548+ yPosition, 24, 4])
    draw.rect(screen, WHITE, [92+ xPosition, 544+ yPosition, 10, 4])
    draw.rect(screen, WHITE, [92+ xPosition, 546+ yPosition, 14, 4])
    draw.rect(screen, LIGHTGREY, [98+ xPosition, 540+ yPosition, 8, 4])
    draw.rect(screen, LIGHTGREY, [102+ xPosition, 544+ yPosition, 4, 2])
    
def easterEgg(): 
    Color = (MINTGREEN, YELLOW, DEEPPINK)
    Color2 = (PINK, LIGHTPINK)
    rand = random.choice(Color)
    rand2 = random.choice(Color2)
    xRand = random.randint(-800, 60)
    yRand = random.randint(0, 30)   
    draw.rect(screen, rand, [xRand + 900, yRand + 600, 12, 4])
    draw.rect(screen, rand, [xRand + 896, yRand + 604, 20, 4])
    draw.rect(screen, rand, [xRand + 892, yRand + 608, 28, 8])
    draw.rect(screen, rand, [xRand + 888, yRand + 616, 36, 8])
    draw.rect(screen, rand, [xRand + 884, yRand + 624, 44, 20])
    draw.rect(screen, rand, [xRand + 888, yRand + 644, 36, 4])
    draw.rect(screen, rand, [xRand + 892, yRand + 648, 28, 4])
    draw.rect(screen, rand, [xRand + 896, yRand + 652, 20, 4])
    draw.rect(screen, rand2, [xRand + 904, yRand + 604, 4, 8])
    draw.rect(screen, rand2, [xRand + 900, yRand + 608, 4, 4]) 
    draw.rect(screen, rand2, [xRand + 892, yRand + 620, 4, 4])
    draw.rect(screen, rand2, [xRand + 892, yRand + 624, 4, 4])
    draw.rect(screen, rand2, [xRand + 888, yRand + 624, 4, 4])
    draw.rect(screen, rand2, [xRand + 916, yRand + 616, 4, 12])
    draw.rect(screen, rand2, [xRand + 912, yRand + 620, 12, 4])
    draw.rect(screen, rand2, [xRand + 904, yRand + 628, 4, 4])
    draw.rect(screen, rand2, [xRand + 908, yRand + 632, 4, 4])
    draw.rect(screen, rand2, [xRand + 900, yRand + 632, 8, 4])
    draw.rect(screen, rand2, [xRand + 904, yRand + 636, 4, 4])
    draw.rect(screen, rand2, [xRand + 900, yRand + 648, 8, 8])
    draw.rect(screen, rand2, [xRand + 924, yRand + 640, 4, 4])
    draw.rect(screen, rand2, [xRand + 920, yRand + 644, 4, 4])
    
def driveway(): 
    draw.polygon(screen, GREY, [[150, 700], [200, 650], [445,650], [496, 700]])

def treeBush(): #Changes shape every time
    for i in range(1,16):
        size = random.randint(60, 80)
        xRand = random.randint(-50, 50)
        yRand = random.randint (-30, 30)
        draw.ellipse(screen, DARKGREEN,[875+xRand, 330+yRand, size, size])
    draw.circle(screen, DARKGREEN, [875, 375], 40)
    draw.circle(screen, DARKGREEN, [945, 375], 40)
    draw.circle(screen, DARKGREEN, [910, 330], 45)
    draw.rect(screen, DARKGREEN, [875, 330, 70, 80])

def treetrunk():
        draw.rect(screen, LIGHTBROWN, [890, 410, 40, 150])
        draw.circle(screen, DARKBROWN, [910, 485], 11)
        draw.line(screen, DARKBROWN, [896, 420], [896, 430], 3)
        draw.line(screen, DARKBROWN, [896, 440], [896, 490], 3)
        draw.line(screen, DARKBROWN, [896, 500], [896, 550], 3)
        draw.line(screen, DARKBROWN, [904, 418], [904, 450], 3)
        draw.line(screen, DARKBROWN, [904, 460], [904, 510], 3)
        draw.line(screen, DARKBROWN, [904, 520], [904, 545], 3)
        draw.line(screen, DARKBROWN, [912, 423], [912, 440], 3)
        draw.line(screen, DARKBROWN, [912, 450], [912, 465], 3)
        draw.line(screen, DARKBROWN, [912, 500], [912, 547], 3)
        draw.line(screen, DARKBROWN, [920, 419], [920, 480], 3)
        draw.line(screen, DARKBROWN, [920, 490], [920, 520], 3)
        draw.line(screen, DARKBROWN, [920, 530], [920, 550], 3)
    
drawScene()
sky()
houseOutline()
garageWindows()
door()
steps()
chimney()
windowArc()
window()
rails()
driveway()
treetrunk()
treeBush()
rabbit()
easterEgg()
easterEgg()
easterEgg()
easterEgg()
display.flip()

running = True
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False             