# import sys module
import pygame
import sys
from Constants import *
from helpers import *

global ran_Level1

cursor_img = pygame.image.load('Images/cursor_image.png')
cursor_img = pygame.transform.scale(cursor_img,
                                    (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
cursor_img_rect = cursor_img.get_rect()


def g_player_main():
    counter = 0
    pygame.init()
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(200, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    pressed_enter = False
    while not(pressed_enter):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pressed_enter = True
                else:
                    user_text += event.unicode
        screen.fill(WHITE)
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, WHITE)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)

        cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
        screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

        pygame.display.flip()
        clock.tick(60)

    print("yay!")


