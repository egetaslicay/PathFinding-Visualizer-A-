import pygame

from constants import WIDTH, ROWS, WHITE, GREY
from spot import Spot
from astar import algorithm

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH)) 
pygame.display.set_caption("A* Path Finding Algorithm")

def make_grid(rows, width): 
    grid = []
    gap = width // rows 
    for i in range(rows): # row
        grid.append([])
        for j in range(rows): #col 
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width): 
    gap = width // rows
    for i in range(rows): 
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range (rows): 
            pygame.draw.line(win, GREY, (j * gap, 0), (j* gap, width))

def draw(win, grid, rows, width): 
    win.fill(WHITE)

    for row in grid: 
        for spot in row: 
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width): 
    gap = width // rows 
    x,y = pos 

    row = y // gap 
    col = x // gap

    return row, col

def main(win, width): 
    ROWS = 50  # you can adjust this variable depending on however many cubes you want
    grid = make_grid(ROWS, width)

    start = None
    end = None 

    run = True
    started = False 

    while run: 
        draw(win, grid, ROWS, width)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
            
            if started: 
                continue


          
            if pygame.mouse.get_pressed()[0]:  ## left mouse btn
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if not start and spot != end: 
                    start = spot
                    start.make_start()

                elif not end and spot != start: 
                    end = spot 
                    end.make_end()

                elif spot != end and spot != start: 
                    spot.make_barrier()


            elif pygame.mouse.get_pressed()[2]: # right mouse btn 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset() 
                if spot == start: 
                    start = None
                elif spot == end: 
                    end = None


            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and not started: 
                    for row in grid: 
                        for spot in row: 
                            spot.update_neighbors(grid)
                          
                    algorithm(lambda: draw (win, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_c: 
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

if __name__ == "__main__": 
    main()