import pygame
pygame.init()
import math 
from queue import PriorityQueue



def h(p1, p2):  ## !!using manhattan distance function (basically the quickest L shape from one point to another since we cannot move in diagonals on grid)
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw): 
    while current in came_from: 
        current = came_from[current]
        current.make_path()
        draw()
 

def algorithm(draw, grid, start, end):  
    count = 0 
    
    open_set = PriorityQueue() 
    open_set.put((0, count, start))
    
    came_from = {}
    
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty(): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()

        current = open_set.get()[2] # index 2 since we only want the node. 
        open_set_hash.remove(current)

        if current == end: 
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors: 
            temp_g_score = g_score[current] + 1  # assuming all the neighbours are 1 away from the node
            
            if temp_g_score < g_score[neighbor]: 
                
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                
                if neighbor not in open_set_hash: 
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start and current != end: 
            current.make_closed()

    return False




