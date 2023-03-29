import pygame
import os
import random
from Constants import *
from helpers import *
from buttons import *


class drawing_player:

    def __init__(self):
        pass


    def dp_main(self):
        rnd_level1 = ""

        # initialize Pygame
        pygame.init()

        pygame.display.set_caption("Draw on the Screen")


        list_of_words = WORDS_LEVEL1
        rnd_Level1 = random.choice(list_of_words)
        list_of_words.remove(rnd_Level1)

        # set up the drawing surface
        # drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        # drawing_surface.fill(WHITE)
        drawing_surface = pygame.image.load("Images/board.png")
        drawing_surface =  pygame.transform.scale(drawing_surface,
                                            (WINDOW_WIDTH, WINDOW_HEIGHT))

        # set up the drawing tools
        #TODO: in constants
        brush_size = 5
        brush_color = BLACK

        cursor_img = pygame.image.load('Images/cursor_image.png')
        cursor_img = pygame.transform.scale(cursor_img,
                                            (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
        cursor_img_rect = cursor_img.get_rect()

        timer_text = str(COUNTER).rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        timer_font = pygame.font.SysFont('Consolas', 30)
        timer_x_pos = TIMER_X_POS
        counter = COUNTER

        finished_drawing = False

        background = pygame.image.load('Images/background_image.jpg')
        background = pygame.transform.scale(background,
                                            (WINDOW_WIDTH, WINDOW_HEIGHT))

        clock = pygame.time.Clock()

        # start the game loop
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and mouse_in_button(board_button, mouse_pos):
                        event_pos = event.pos
                        if not(mouse_in_button(board_button, event_pos)):
                            event_pos = last_pos_in_board(event_pos)
                        pygame.draw.circle(drawing_surface, brush_color, event_pos, brush_size - 2)
                        last_pos = event_pos
                    if mouse_in_button((red_button), mouse_pos):
                        brush_color = RED
                    if mouse_in_button((orange_button), mouse_pos):
                        brush_color = ORANGE
                    if mouse_in_button((yellow_button), mouse_pos):
                        brush_color = YELLOW
                    if mouse_in_button((green_button), mouse_pos):
                        brush_color = GREEN
                    if mouse_in_button((cyan_button), mouse_pos):
                        brush_color = CYAN
                    if mouse_in_button((dark_blue_button), mouse_pos):
                        brush_color = DARK_BLUE
                    if mouse_in_button((purple_button), mouse_pos):
                        brush_color = PURPLE
                    if mouse_in_button((pink_button), mouse_pos):
                        brush_color = PINK
                    if mouse_in_button((brown_button), mouse_pos):
                        brush_color = BROWN
                    if mouse_in_button((black_button), mouse_pos):
                        brush_color = BLACK
                    if mouse_in_button((eraser_button), mouse_pos):
                        brush_color = BOARD_COLOR
                elif event.type == pygame.MOUSEMOTION and mouse_in_button(board_button, mouse_pos):
                    if event.buttons[0]:  # left mouse button
                        event_pos = event.pos
                        if not (mouse_in_button(board_button, event_pos)):
                            event_pos = last_pos_in_board(event_pos)
                        pygame.draw.line(drawing_surface, brush_color, last_pos, event_pos, brush_size)
                        last_pos = event_pos
                elif event.type == pygame.USEREVENT:
                        counter -= 1
                        if counter > 0:
                            timer_text = str(counter).rjust(3)
                        elif counter == 0:
                            timer_text = "time's up!"
                            timer_x_pos = TIMER_X_POS - 50
                        else:
                            finished_drawing = True

            screen.blit(drawing_surface, (13, 45))

            # add_image("images/board.png", BOARD_X_POS, BOARD_Y_POS, BOARD_WIDTH, BOARD_HEIGHT, screen)
            add_image("images/colors2.png", COLORS_X_POS, COLORS_Y_POS, COLORS_WIDTH, COLORS_HEIGHT, screen)
            add_image("images/tools.png", TOOLS_X_POS, TOOLS_Y_POS, TOOLS_WIDTH, TOOLS_HEIGHT, screen)

            # if finished_drawing:
            #     pygame.time.delay(3000)

            timer_font = pygame.font.SysFont("Anything Skribble", TIMER_SIZE)
            screen.blit(timer_font.render(timer_text, True, LIGHT_BROWN), (timer_x_pos, TIMER_Y_POS))
            # txtsurf = timer_font.render(rnd_Level1, True, WHITE)
            # screen.blit(txtsurf, (1000 - txtsurf.get_width() // 2, 700 - txtsurf.get_height() // 2))
            # screen.blit(txtsurf, (TIMER_X_POS-))

            if mouse_in_button(board_button, mouse_pos):
                pygame.mouse.set_visible(False)
                cursor_img_rect.center = (mouse_pos[0] + 35, mouse_pos[1] + 5) # update position
                screen.blit(cursor_img, cursor_img_rect)  # draw the cursor
            else:
                pygame.mouse.set_visible(True)

            word_font = pygame.font.SysFont('Anything Skribble', WORD_TEXT_SIZE)
            guess_word = word_font.render(rnd_Level1, True, LIGHT_BROWN)
            screen.blit(guess_word, [WORD_X_POS,WORD_Y_POS])

            pygame.image.save(drawing_surface, os.path.join("screenshots", "screenshot.png"))

            # update the screen
            pygame.display.update()
            pygame.display.flip()

            clock.tick(60)

        # quit Pygame
        pygame.quit()

# dp_main()