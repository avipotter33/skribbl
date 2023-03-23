import pygame
import os
import random
from Constants import *
from helpers import *
from main_player2 import *


def dp_main():

    # initialize Pygame
    pygame.init()

    pygame.display.set_caption("Draw on the Screen")


    global ran_Level1
    list_of_words = WORDS_LEVEL1
    ran_Level1 = random.choice(list_of_words)
    list_of_words.remove(ran_Level1)

    # set up the drawing surface
    drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawing_surface.fill(WHITE)

    # set up the drawing tools
    brush_size = 5
    brush_color = BLACK

    cursor_img = pygame.image.load('Images/cursor_image.png')
    cursor_img = pygame.transform.scale(cursor_img,
                                        (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
    cursor_img_rect = cursor_img.get_rect()

    timer_text = str(COUNTER).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    timer_font = pygame.font.SysFont('Consolas', 30)

    counter = COUNTER

    finished_drawing = False

    # start the game loop
    running = True
    while running:
        screen.blit(drawing_surface, (0, 0))
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
            elif event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter > 0:
                        timer_text = str(counter).rjust(3)
                    elif counter == 0:
                        timer_text = "time's up!"
                        screen.blit(timer_font.render(timer_text, True, WHITE), (32, 48))
                    else:
                        finished_drawing = True

        if finished_drawing:
            pygame.time.delay(500)
            g_player_main()

        timer_font = pygame.font.SysFont("Arial", 36)
        txtsurf = timer_font.render(ran_Level1, True, WHITE)
        screen.blit(txtsurf, (1000 - txtsurf.get_width() // 2, 700 - txtsurf.get_height() // 2))

        screen.blit(timer_font.render(timer_text, True, (0, 0, 0)), (32, 48))

        rect = pygame.Rect(20, 200, 50, 50)
        pygame.draw.rect(drawing_surface, BLACK, rect)

        cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
        screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

        word_font = pygame.font.SysFont('Anything Skribble', WORD_TEXT_SIZE)
        guess_word = word_font.render(ran_Level1, True, BLACK)
        screen.blit(guess_word, [WORD_X_POS,WORD_Y_POS])

        pygame.image.save(drawing_surface, os.path.join("screenshots", "screenshot.png"))

        # update the screen
        pygame.display.update()
        pygame.display.flip()

    # quit Pygame
    pygame.quit()