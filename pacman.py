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