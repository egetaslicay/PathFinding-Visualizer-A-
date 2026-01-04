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

# class to keep track of colour spots and how we can color in blocks and remove color too
class Spot: 
    def __init___(self, row, col, width, total_rows): 
        self.row = row
        self.col = col 
        self.x = row * width 
        self.y = col * width