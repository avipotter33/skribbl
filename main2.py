import pygame
from Constants import *


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Skribbl')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/‏‏background_image.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH + 500, WINDOW_HEIGHT))

    image_x_index = 0

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('Images/cursor_image.png')
    cursor_img = pygame.transform.scale(cursor_img,
                                        (CURSOR_WIDTH, CURSOR_HEIGHT))
    cursor_img_rect = cursor_img.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLUE)
        screen.blit(background, (image_x_index, 0))

        if image_x_index != (0 - WINDOW_WIDTH):
            screen.blit(background, (WINDOW_WIDTH + 500 + image_x_index, 0))
        else:
            screen.blit(background, (WINDOW_WIDTH + 500 + image_x_index, 0))
            image_x_index = 0

        image_x_index -= 1

        add_image('Images/home page5(2).png', HOME_PAGE_X_POS, HOME_PAGE_Y_POS, HOME_PAGE_WIDTH, HOME_PAGE_HEIGHT, screen)
        add_image('Images/button.png', PLAY_BTN_X_POS, PLAY_BTN_Y_POS, PLAY_BTN_WIDTH, PLAY_BTN_HEIGHT, screen)
        #add_image('Images/yellow button.png', BUTTON_X_POS, BUTTON_Y_POS, BUTTON_WIDTH, BUTTON_HEIGHT, screen)

        cursor_img_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(20)

    pygame.quit()
    quit()

main()