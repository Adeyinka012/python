import random
import pygame
class Button():
    def _init_(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.width =width
        self.height = height
        self.pos = pos
         
    def clicked(self,pos):
        self.pos=pygame.mouse.get.pos()
        if self.pos[0]> self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
class pygame():
    def _init_(self):
        pygame.init()
        self.screen =pygame.display.set_mode((960,640))
        pygame.display.set_caption('RPS smasher')
        self.bg=pygame.image.load("https://wallpapercave.com/wp/wp8121945.jpg")
        self.r_btn = pygame.image.load('r_btn.png').convert_alpha()
        self.p_btn = pygame.image.load('p_btn.png').convert_alpha()
        self.s_btn = pygame.image.load('s_btn.png').convert_alpha()
        
        self.choose_rock = pygame.image.load('https://th.bing.com/th/id/OIP.zTeskWPh8ozPLTQ11IBlKgHaFj?rs=1&pid=ImgDetMain.png').convert_alpha()
        self.choose_paper = pygame.image.load('https://static.vecteezy.com/system/resources/previews/000/526/441/original/vector-two-empty-papers.jpg.png').convert_alpha()
        self.choose_scissors = pygame.image.load('https://th.bing.com/th/id/R.680ce8a9cf105b860fb74c8690d9f1bc?rik=s2Z%2bjzppqzHMXw&riu=http%3a%2f%2fpngimg.com%2fuploads%2fscissors%2fscissors_PNG31.png&ehk=%2bmxYJ27rgx0AnPkWoNO64y%2fmeSMat%2f0wXk4uH4wPq7I%3d&risl=&pid=ImgRaw&r=0.png').convert_alpha()               