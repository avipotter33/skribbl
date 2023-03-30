import pygame

import buttons
from Constants import *
from helpers import *
from buttons import *
import translators as ts
from drawing_player import *
# from Translator import *
from Client import *

class home_screen:
    change_language = True
    PLAY_TEXT = ts.translate_text(PLAY_TEXT, to_language='he')
    mouse_pos = [0, 0]

    def __init__(self):
        pass

    play_button = buttons.play_button


    def main(self):
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        # Set up the game display, clock and headline
        pygame.init()

        # Change the title of the window
        pygame.display.set_caption('Skribbl')

        clock = pygame.time.Clock()

        # Set up background image
        background = pygame.image.load('Images/background_image.jpg')
        background = pygame.transform.scale(background,
                                            (WINDOW_WIDTH, WINDOW_HEIGHT))

        image_x_index = 0

        pygame.mouse.set_visible(False)
        cursor_img = pygame.image.load('Images/cursor_image.png')
        cursor_img = pygame.transform.scale(cursor_img,
                                            (CURSOR_WIDTH, CURSOR_HEIGHT))
        cursor_img_rect = cursor_img.get_rect()

        language = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    print(mouse_pos)
                    if mouse_in_button(play_button, mouse_pos):
                        print("meow")
                        game_loop()
                        # dr_player = drawing_player("shnizel")
                        # dr_player.dp_main()
                    if mouse_in_button(language_icon, mouse_pos):
                        # game_loop()
                        language = True
                        # dr_player = drawing_player("shnizel")
                        # dr_player.dp_main()
            screen.fill(BLUE)
            screen.blit(background, (image_x_index, 0))

            if image_x_index != (0 - WINDOW_WIDTH):
                screen.blit(background, (WINDOW_WIDTH + image_x_index, 0))
            else:
                screen.blit(background, (WINDOW_WIDTH + image_x_index, 0))
                image_x_index = 0

            image_x_index -= 1

            add_image('Images/home page5(2).png', HOME_PAGE_X_POS, HOME_PAGE_Y_POS, HOME_PAGE_WIDTH, HOME_PAGE_HEIGHT, screen)
            add_image('Images/button.png', PLAY_BTN_X_POS, PLAY_BTN_Y_POS, PLAY_BTN_WIDTH, PLAY_BTN_HEIGHT, screen)
            #add_image('Images/yellow button.png', BUTTON_X_POS, BUTTON_Y_POS, BUTTON_WIDTH, BUTTON_HEIGHT, screen)

            if language:
                add_image("Images/flags.png", LANGUAGE_X_POS, LANGUAGE_Y_POS, LANGUAGE_WIDTH, LANGUAGE_HEIGHT, screen)

            cursor_img_rect.center = pygame.mouse.get_pos()  # update position
            if mouse_in_button(play_button, pygame.mouse.get_pos()):
                add_image('Images/yellow button.png', PLAY_BTN_X_POS, PLAY_BTN_Y_POS, PLAY_BTN_WIDTH, PLAY_BTN_HEIGHT,
                          screen)
            font = pygame.font.SysFont('Anything Skribble', PLAY_TEXT_SIZE)
            text = font.render(PLAY_TEXT, True, WHITE)
            screen.blit(text, [PLAY_BTN_X_POS + 22, PLAY_BTN_Y_POS])

            screen.blit(cursor_img, cursor_img_rect)  # draw the cursor
            pygame.display.update()

            # Set the clock tick to be 60 times per second. 60 frames for second.
            # If we want faster game - increase the parameter.
            clock.tick(20)

        pygame.quit()
        quit()

    def add_image(img_path, x_pos, y_pos, width, height, screen):
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))