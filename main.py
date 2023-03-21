import pygame
import os
import random

# initialize Pygame
pygame.init()

# set the window size and title
# TODO: in constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw on the Screen")

# set up the colors
# TODO: in constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill(WHITE)

# set up the drawing tools
# TODO: in constants
brush_size = 5
brush_color = BLACK

words_level1 = ["coin", "star", "ear", "pie", "bus", "window", "ocean", "shield", "bridge", "Earth", "legs", "car", "mountains", "door", "flower"]
words_level2 = ["needle", "waterfall", "school bus", "north", "pool", "popcorn", "glass", "popsicle", "t shirt", "hockey", "bike", "hospital", "picture frame", "smoke", "camel"]
words_level3 = ["professor", "half", "toothpasre", "date", "sushi", "birthday", "classroom", "time", "sponge", "skinny", "panda", "cinema", "dawn", "pot", "high five"]
word = random.choice(words_level1)


# start the game loop
running = True
while running:
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
                    pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)
                    last_pos = event.pos
            elif event.button == 3:  # right mouse button
                # undo last path
                drawing_surface.fill(WHITE)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # left mouse button
                pygame.draw.line(drawing_surface, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    rect = pygame.Rect(20, 50, 50, 50)
    pygame.draw.rect(drawing_surface, BLACK, rect)

    # update the screen
    window.blit(drawing_surface, (0, 0))
    pygame.display.flip()

# quit Pygame
pygame.quit()
