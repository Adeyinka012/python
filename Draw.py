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
        
    def drawoutline(self):
        penup()
        left(90)
        pendown()
        circle(self.size)
        self.gohome()   
    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self.size/2)
        pendown()
        dot(self.size/10)
        self.gohome()

    def drawmouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        circle(self.size/1.7,90)
        self.gohome()
        
    def drawNose(self):
        if self.nosesize == 'large':
            dot(self.size/2, 'grey')
        if self.nosesize == 'large':
            dot(self.size/6, 'small')
        else:
            dot(self.size/4, 'grey')
            self.gohome()   
    f1 = (0,0)
    f1.draw()
    showturtle()  
    done()       

        