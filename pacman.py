# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

class PacMan:
    #Construtor
    def __init__(self,x,y):
        self.x = x # attribute
        self.y = y # attribute
        self.r = 0
        self.speed = 10
        #image loading
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
        #image loading
        self.ghost_red_images = []
        for i in range(3):
            img = pg.image.load(f'images/ghost_red_{i}.png')
            img = pg.transform.scale(img, (32,32))
            self.ghost_red_images.append(img)
    
    def move(self,target):
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

class LevelConstructor:
    def __init__(self,level='level.txt'):
        self.level = []
        with open(level, 'r') as level_file:
            for r, line in enumerate(level_file):
                row = []
                for c, char in enumerate(line):
                    if char == "#":
                        row.append("#")
                    elif char == "p":
                        self.player_pos_y = r*32
                        self.player_pos_x = c*32
                        row.append(" ")
                    else:
                        row.append("*")

                self.level.append(row)

        self.num_rows = len(self.level)
        self.num_cols = len(self.level[0])
    
    def draw(self,screen):
        for r, row in enumerate(self.level):
            for c, tile in enumerate(row):
                left = c*32
                top = r*32
                if tile == "#":
                    pg.draw.rect(screen, (50,50,220), pg.Rect(left+1, top+1, 30,30), 1)
                elif tile == '*':
                    pg.draw.circle(screen, (250,250,250), (left+16,top+16), 4)

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
#pg.display.set_icon(pacman_images[1])

#opretter objekter
level = LevelConstructor()
pacman = PacMan(level.player_pos_x, level.player_pos_y)
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
    level.draw(screen)
    ghost.draw(screen)
    pacman.draw(screen,direction,tick)

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.2)
