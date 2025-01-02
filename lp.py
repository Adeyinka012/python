from turtle import *
class face:
    def __init__(self, xpos, ypos):
        self.size =90
        self.coord =(xpos, ypos)
        self.nosesize = 'small'
    
    def setsize(self, radius):
        self.size =radius
        
    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        pensize(3)

    def gohome(self):
        penup()
        goto(self.coord)
        setheading(0)
        
    def drawoutline(self)        




def drawOutline(self):

penup()

forward(self.size)

left(90)

pendown()

circle(self.size)

self.goHome()


def drawEye(self, turn):

penup()

left(turn)

forward(self.size/2)

pendown()

dot(self.size/10)

self.goHome()


def drawMouth(self):

penup()

right(135)

forward(self.size/1.7)

left(90)

circle(self.size/1.7,90)

self.goHome()


def drawNose(self):

if self.noseSize == "large":

dot(self.size/2, 'grey')

if self.noseSize == "large":

dot(self.size/6, 'small')


else:

dot(self.size/4, 'grey')

self.goHome()


f1 = face(0,0)

f1.draw()

showturtle()

done()     
        