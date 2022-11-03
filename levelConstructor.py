import pygame as pg

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
                    elif char == '.':
                        row.append("*")
                    elif char == 'g':
                        self.ghost_pos_y = r*32
                        self.ghost_pos_x = c*32
                        row.append(' ')
                    else:
                        row.append(' ')

                self.level.append(row)

        self.num_rows = len(self.level)
        self.num_cols = len(self.level[0])
    
    def hitbox_constuctor(self):
        for r, row in enumerate(self.level):
            for c, tile in enumerate(row):
                left = c*32
                top = r*32
                if tile == "#":
                    print(c,r)

    def draw(self,screen):
        for r, row in enumerate(self.level):
            for c, tile in enumerate(row):
                left = c*32
                top = r*32
                if tile == "#":
                    pg.draw.rect(screen, (50,50,220), pg.Rect(left+1, top+1, 30,30), 1)
                elif tile == '*':
                    pg.draw.circle(screen, (250,250,250), (left+16,top+16), 4)