import pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 800
ALPHA_BACKGROUND = 50
CURSOR_WIDTH, CURSOR_HEIGHT = 100, 100

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Skribbl')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('‏‏background_image.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    image_x_index = 0

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load('cursor_image.png')
    cursor_img = pygame.transform.scale(cursor_img,
                                        (CURSOR_WIDTH, CURSOR_HEIGHT))
    cursor_img_rect = cursor_img.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((180, 223, 247))
        screen.blit(background, (image_x_index, 0))
        image_x_index -= 1

        if image_x_index != (0 - WINDOW_WIDTH):
            screen.blit(background, (WINDOW_WIDTH + image_x_index + 1, 0))
        else:
            screen.blit(background, (WINDOW_WIDTH + image_x_index + 1, 0))
            image_x_index = 0

        cursor_img_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(20)

    pygame.quit()
    quit()

main()