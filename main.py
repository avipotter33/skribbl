import pygame

# initialize Pygame
pygame.init()

# set the window size and title
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw on the Screen")

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill(WHITE)

# set up the drawing tools
brush_size = 5
brush_color = BLACK

# set up the undo button
undo_button = pygame.Rect(10, 10, 50, 30)
undo_font = pygame.font.SysFont(None, 24)
undo_text = undo_font.render("Undo", True, BLACK)

# start the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
                pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)
                last_pos = event.pos
            elif event.button == 3:  # right mouse button
                # undo last path
                drawing_surface.fill(WHITE)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # left mouse button
                pygame.draw.line(drawing_surface, brush_color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    # draw the undo button
    pygame.draw.rect(drawing_surface, WHITE, undo_button)
    pygame.draw.rect(drawing_surface, BLACK, undo_button, 1)
    drawing_surface.blit(undo_text, (undo_button.x + 5, undo_button.y + 5))

    # update the screen
    window.blit(drawing_surface, (0, 0))
    pygame.display.flip()

# quit Pygame
pygame.quit()
