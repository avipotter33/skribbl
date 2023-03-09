from Constants import *
import pygame
from helpers import *


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Skribbl')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('background image.jpg')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    background = background.convert()
    rect = background.get_rect()
    background.set_alpha(ALPHA_BACKGROUND)
    button1 = pygame.image.load('button.png')
    button1 = pygame.transform.scale(button1, (BUTTON_WIDTH, BUTTON_HEIGHT))

    add_icons = False

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y_pos = pygame.mouse.get_pos()[1]
                mouse_x_pos = pygame.mouse.get_pos()[0]
                if BUTTON1_X_POS < mouse_x_pos < BUTTON1_X_POS + BUTTON_WIDTH and BUTTON1_Y_POS * 1.8 < mouse_y_pos < BUTTON1_Y_POS * 1.8 + BUTTON_HEIGHT:
                    if add_icons:
                        add_icons = False
                    else:
                        add_icons = True

            pygame.display.update()
            # Display the background, presented Image, likes, comments, tags and
            # location(on the Image)
            screen.fill(WHITE)
            screen.blit(background, rect)
            add_image('play button.png', BUTTON1_X_POS, BUTTON1_Y_POS, BUTTON_WIDTH, BUTTON_HEIGHT, screen)
            add_image('button.png', BUTTON1_X_POS, BUTTON1_Y_POS * 1.8, BUTTON_WIDTH - 10, BUTTON_HEIGHT, screen)
            add_image('thumbnail.png', THUMBNAIL_X_POS, THUMBNAIL_Y_POS, THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT, screen)

            mouse_y_pos = pygame.mouse.get_pos()[1]
            mouse_x_pos = pygame.mouse.get_pos()[0]

            if BUTTON1_X_POS < mouse_x_pos < BUTTON1_X_POS + BUTTON_WIDTH and BUTTON1_Y_POS < mouse_y_pos < BUTTON1_Y_POS + BUTTON_HEIGHT:
                add_image('play button bold.png', BUTTON1_X_POS - 8, BUTTON1_Y_POS - 14, BUTTON_WIDTH + 30, BUTTON_HEIGHT + 12, screen)

            if BUTTON1_X_POS < mouse_x_pos < BUTTON1_X_POS + BUTTON_WIDTH and BUTTON1_Y_POS * 1.8 < mouse_y_pos < BUTTON1_Y_POS * 1.8 + BUTTON_HEIGHT:
                add_image('topics button bold.png', BUTTON1_X_POS - 16, BUTTON1_Y_POS * 1.8 - 6, BUTTON_WIDTH + 13, BUTTON_HEIGHT + 13, screen)

            if add_icons:
                add_image('music icon.png', ICON_BUTTON_X_POS, ICON_BUTTON_Y_POS, ICON_BUTTON_WIDTH,
                          ICON_BUTTON_HEIGHT, screen)
                add_image('sports icon.png', ICON_BUTTON_X_POS + 250, ICON_BUTTON_Y_POS, ICON_BUTTON_WIDTH - 10,
                          BUTTON_HEIGHT, screen)
                add_image('movies icon.png', ICON_BUTTON_X_POS + 250 * 2, ICON_BUTTON_Y_POS, ICON_BUTTON_WIDTH - 10,
                          BUTTON_HEIGHT,
                          screen)

            # Update display - without input update everything
            pygame.display.update()

            # Set the clock tick to be 60 times per second. 60 frames for second.
            # If we want faster game - increase the parameter.
            clock.tick(60)

    pygame.quit()
    quit()


main()
