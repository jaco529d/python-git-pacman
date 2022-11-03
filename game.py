# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg
from ghost import Ghost
from pacman import PacMan
from levelConstructor import LevelConstructor


## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
#pg.display.set_icon(pacman_images[1])

#opretter objekter
level = LevelConstructor()
pacman = PacMan(level.player_pos_x, level.player_pos_y)
ghost = Ghost(level.ghost_pos_x,level.ghost_pos_y)

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
    ghost.draw(screen,tick)
    pacman.draw(screen,direction,tick)

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.2)
