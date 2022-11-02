# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Load images ##

class PacMan:
    #Construtor
    def __init__(self,x,y):
        self.x = x # attribute
        self.y = y # attribute
        self.r = 0
        self.speed = 10
        self.pacman_images = []
        for i in range(6):
            img = pg.image.load(f"images/pacman_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.pacman_images.append(img)

    def move(self, new_direction):
        if new_direction == "left":
            self.x -= self.speed
            self.r = 0
        elif new_direction == "right":
            self.x += self.speed
            self.r = 180
        elif new_direction == "up":
            self.y -= self.speed
            self.r = -90
        elif new_direction == "down":
            self.y += self.speed
            self.r = 90

    def draw(self,screen,direction,tick):
        #pg.draw.circle(screen, (220,220,20), (self.x,self.y), 16)
        k = int((tick/2)%6)
        img_direction = pg.transform.rotate(self.pacman_images[k],self.r)
        screen.blit(img_direction,(self.x,self.y))

class Ghost:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.speed = 2
        self.ghost_red_images = []
        for i in range(3):
            img = pg.image.load(f'images/ghost_red_{i}.png')
            img = pg.transform.scale(img, (32,32))
            self.ghost_red_images.append(img)
    
    def move(self,target):
        """dx = random.randint(-10,10)
        dy = random.randint(-10,10)
        self.x += dx
        self.y += dy"""
        if self.x > target.x:
            self.x -= self.speed
        elif self.x < target.x:
            self.x += self.speed
        if self.y > target.y:
            self.y -= self.speed
        elif self.y < target.y:
            self.y += self.speed

    def draw(self,screen):
        k = int((tick/2)%3)
        screen.blit(self.ghost_red_images[k],(self.x,self.y))
        #pg.draw.circle(screen, (250,50,50), (self.x,self.y),16)

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
#pg.display.set_icon(pacman_images[1])

#opretter objekter
pacman = PacMan(100,100)
ghost = Ghost(200,200)

direction = None
running = True
tick = 0
while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_ESCAPE:
                running = False

    # Logic #
    pacman.move(direction) # Kalde metoden move()
    ghost.move(pacman)

    # Drawing #
    screen.fill((0,0,0))
    ghost.draw(screen)
    pacman.draw(screen,direction,tick)

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.2)
