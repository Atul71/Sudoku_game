import pygame
import time
from sudoku import valid, solve, finished
pygame.font.init() #to initialise pygame

#grid class wraps the main sudoku board each with item box
class grid:

    
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    #initialise variables for grid

    def __init__(self, rows, cols, height, width):
        self.rows = rows
        self.cols = cols
        self.height = height
        self.width = width
        self.box = [[box(self.board[i][j], i, j, height, width) for j in range(cols)] for i in range(rows)]
        self.selected_pos = None
        self.model = None
    #finding x and y coordinates for clcikcing
    def click(self, pos):
        gap = self.width/9
        if(pos[0] < self.width and pos[1] < self.height):
            x = pos[0]//gap
            y = pos[1]//gap
        return (int(x),int(y))

    #Selecting a particular grid in board
    def select(self, x, y):
        for i in range(self.rows):
            for j in range(self.cols):
                self.box[i][j].selected = False


        self.box[x][y].selected = True
        self.selected_pos = (x,y)

    #Drawing the grid lines of sudoku board

    def draw_grid(self,win):
        gap_x = self.width / 9
        gap_y = self.height / 9
        for i in range(1,self.rows+1):
            if(i%3==0):
                thickness = 4
            else:
                thickness = 1        
            pygame.draw.line(win, (0,0,0),(0,(i)*gap_x), (self.width,i*gap_x),thickness)
        
            pygame.draw.line(win, (0,0,0),(i*gap_y,0),(i*gap_y,self.height),thickness)
        #Drawing each box insde grid

        for i in range(self.rows):
            for j in range(self.cols):
                self.box[i][j].draw(win)

    def sketch(self, val):
        row, col = self.selected_pos
        self.box[row][col].set_temp(val)
    #Placing temp value if is correct position   
    def place(self, val):
        row, col = self.selected_pos

        
        self.model = [[self.box[i][j].value for j in range(self.cols)] for i in range(self.rows)]


        if valid(self.model, row, col, val):
            self.box[row][col].value = val
            self.model = [[self.box[i][j].value for j in range(self.cols)] for i in range(self.rows)]
            if solve(self.model):
                return True
            else:
                self.box[row][col].set_temp(0)
                self.box[row][col].set_val(0)
                return False
    def isfinished(self):
        self.model = [[self.box[i][j].value for j in range(self.cols)] for i in range(self.rows)]
        if(finished(self.model)):
            return True
        else:
            return False

    #Function to clear the entered key
    def clear(self):
        row,col = self.selected_pos
        if(self.box[row][col].value==0):
            self.box[row][col].set_temp(0)
class box:
    def __init__(self, value, row, col, height, width):
        self.value = value
        self.col = col
        self.row = row
        self.height = height
        self.width = width
        self.selected = False
        self.temp = 0

    #Functon to draw box in sudoku grid

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)
        
        gap = self.width/9
        x = gap * self.row
        y = gap * self.col
        if self.temp!=0 and self.value == 0:
            text = fnt.render(str(self.temp),1,(255,0,0))
            win.blit(text, (x + gap/4, y + gap/4))
        elif(self.value!=0):

            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + gap/4,y + gap/4))
        
        if(self.selected):
            pygame.draw.rect(win,(255,0,0), (x,y,gap,gap), 3)
        
    def set_temp(self, val):
        self.temp = val
        

    def set_val(self, val):
        self.value = val

def main():
    #Initialising and setting up the sudoku board and canvas
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Sudoku")
    key = None
    grid_item = grid(9,9,500,500)
    run = True
    while run:
        
        #Enabling exit condition in pygame
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    grid_item.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = grid_item.selected_pos
                    if grid_item.box[i][j].temp!=0:
                        if grid_item.place(grid_item.box[i][j].temp):
                            print("Successfully placed")
                        else:
                            print("Not successful")
                        key = None

                        if grid_item.isfinished():
                            win.fill((0,0,0))
                            fnt = pygame.font.SysFont("comicsans", 40)
                            text_surface = fnt.render("Game Over! You won",1,(150,150,150))
                            textrect = text_surface.get_rect()
                            textrect.centerx, textrect.centery = 250,250
                            win.blit(text_surface,textrect)
                            pygame.display.update()
                            print("Game over!")
                            pygame.time.wait(5000)
                            
                            #run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click_pos = grid_item.click(pos)
                if click_pos:
                    grid_item.select(click_pos[0],click_pos[1])
                    
        if grid_item.selected_pos and key!=None:
            grid_item.sketch(key)



        win.fill((255,255,255))
      #  k.draw(win)
        grid_item.draw_grid(win)
        #pygame.display.flip()
               
        pygame.display.update()
main()
pygame.quit()