import pygame
import math 
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH)) 
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot: 
    def __init___(self, row, col, width, total_rows): 
        self.row = row
        self.col = col 
        self.width = width
        self.x = row * width 
        self.y = col * width
        # sidenote, for self.x and self.y, 
        # we can get these coordinate points since we multiply the size of each of the cubes until we get to the row or column we want 

        self.neighbours = []    
        self.total_rows = total_rows
    
    def get_pos(self): 
        return self.row, self.col
    
    def is_closed(self): 
        return self.color == RED
    
    def is_open(self): 
        return self.color == GREEN 
    
    def is_barrier(self): 
        return self.color == BLACK
    
    def is_start(self): 
        return self.color == ORANGE
    
    def is_end(self): 
        return self.color == TURQUOISE
    
    def reset(self):
        self.color == WHITE 

    def make_closed(self): 
        self.color = RED 

    def make_open(self): 
        self.color = GREEN
    
    def make_barrier(self): 
        self.color = BLACK 

    def make_end(self): 
        self.color = TURQUOISE
    
    def make_path(self): 
        self.color = PURPLE
    
    def draw(self, win): 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width)) 

    def update_neightbors(self, grid): 
        pass

    def __lt__(self,other): 
        return False
    

def heuristic(p1, p2):  ## !!using manhattan distance function (basically the quickest L shape from one point to another since we cannot move in diagonals on grid)
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width): 
    grid = []
    gap = width // rows 
    for i in range(rows): # row
        grid.append([])
        for j in range(rows): #col 
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

