import pygame

WIDTH, HEIGHT = 700, 700    #pixels #width and hight of window
ROWS, COLS = 8, 8           #number of colmns and rows
SQUARE_SIZE = WIDTH//COLS   #size of the square

        #RGB
RED = (128, 0, 0)
# REDPIECE = (128, 0, 0)
GREEN = (60, 179, 112)
WHITEBOARD=(240, 248, 254)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('images/king.png'), (40, 25)) #load image of crown and resize