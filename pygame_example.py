import pygame
from random import random
from numpy import sin, cos, linspace, pi


#initialize pygame
pygame.init()

#color shortcuts
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")

class Dot():

    def __init__(self, x_var, y_var):
        self.x = x_var
        self.y = y_var
        self.xspeed = 0
        self.yspeed = 10
        self.loc = (self.x, self.y)
        
        
    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_up(self):
        self.y -= self.yspeed *5

    def move_down(self):
        self.y += self.speed

    def draw(self):
           pygame.draw.rect(screen, red, pygame.Rect(self.x, self.y, 10, 10))
           
class Platform():

    def __init__(self, x_var, y_var, length):
        self.x = x_var
        self.y = y_var
        self.length = length
        self.color = blue
        self.top = [(i, self.y) for i in range(self.x, self.x + self.length)]

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.length, 15))
        
player = Dot(30,30)


def rx():
    return int(random()* (700-15))

def ry():
    return int(random()* (500 - 50))

plist = [Platform(rx(), ry(), 40) for i in range(25)]



surfaces = []
for i in plist:
    surfaces += i.top

#main program loop
done = False
stable = True
clock = pygame.time.Clock()
screen.fill(white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #moving square with arrows

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.xspeed = 0
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.xspeed = 3
            elif event.key == pygame.K_LEFT:
                player.xspeed = -3
            elif event.key == pygame.K_UP:
                #jumping only allowed from platform
                if stable:
                    player.move_up()

    #have player dot fall if not on platform                
    
    if (player.loc) in surfaces:
        stable = True
    else:
        stable = False

    for i in plist:
        for j in range(i.x, i.x + i.length):
            if player.loc in (j, i.y):
                i.color = green

    if not stable:
        player.y +=1
            
    #draw platforms
    for i in plist:
        i.draw()

        
    player.draw()
    player.x += player.xspeed
    pygame.display.flip()

    player.loc = (player.x, player.y + 10)
    screen.fill(white)
    clock.tick(20)
    
pygame.quit()
