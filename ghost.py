import pygame as pg

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

    def draw(self,screen,tick):
        k = int((tick/2)%3)
        screen.blit(self.ghost_red_images[k],(self.x,self.y))
        #pg.draw.circle(screen, (250,50,50), (self.x,self.y),16)