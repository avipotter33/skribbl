from Constants import *
import pygame
from helpers import *


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

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()
            # Display the background, presented Image, likes, comments, tags and
            # location(on the Image)
            screen.fill(WHITE)
            screen.blit(background, rect)
            screen.blit(button1, (BUTTON1_X_POS, BUTTON1_Y_POS))

            # Update display - without input update everything
            pygame.display.update()

            # Set the clock tick to be 60 times per second. 60 frames for second.
            # If we want faster game - increase the parameter.
            clock.tick(60)

    pygame.quit()
    quit()


main()
