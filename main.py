import pygame
import os
import random
from Constants import *
from helpers import *


# initialize Pygame
pygame.init()

# set the window size and title
# TODO: in constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CURSOR_WIDTH, CURSOR_HEIGHT = 100, 100

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw on the Screen")

# set up the colors
# TODO: in constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
global ran_Level1
ran_Level1 = random.choice(WORDS_LEVEL1)

# set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill(WHITE)

# set up the drawing tools
# TODO: in constants
brush_size = 5
brush_color = BLACK

cursor_img = pygame.image.load('Images/cursor_image.png')
cursor_img = pygame.transform.scale(cursor_img,
                                    (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
cursor_img_rect = cursor_img.get_rect()

# start the game loop
running = True
while running:
    window.blit(drawing_surface, (0, 0))
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
                mouse_y_pos = pygame.mouse.get_pos()[1]
                mouse_x_pos = pygame.mouse.get_pos()[0]
                if 20 < mouse_x_pos < 20 + 50 and 50 < mouse_y_pos < 100:
                    pygame.image.save(drawing_surface, os.path.join("screenshots", "screenshot.png"))
                else:
                    pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size - 2)
                    last_pos = event.pos
            elif event.button == 3:  # right mouse button
                # undo last path
                drawing_surface.fill(WHITE)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # left mouse button
                pygame.draw.line(drawing_surface, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render(ran_Level1, True, WHITE)
    screen.blit(txtsurf, (200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))

    rect = pygame.Rect(20, 50, 50, 50)
    pygame.draw.rect(drawing_surface, BLACK, rect)

    cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
    window.blit(cursor_img, cursor_img_rect)  # draw the cursor

    # update the screen
    pygame.display.update()
    pygame.display.flip()

# quit Pygame
pygame.quit()

