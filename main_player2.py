# import sys module
import pygame
import sys
from Constants import *
from helpers import *
from buttons import *

global ran_Level1

cursor_img = pygame.image.load('Images/cursor_image.png')
cursor_img = pygame.transform.scale(cursor_img,
                                    (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
cursor_img_rect = cursor_img.get_rect()


def g_player_main():
    pygame.init()
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(COMMENT_BOX_WIDTH, COMMENT_BOX_HEIGHT, COMMENT_BOX_X_POS, COMMENT_BOX_Y_POS)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    count = 1
    rect_list = []
    text_list = []
    printing_list = []

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
                    printing_list.append(event.unicode)
                    text_list.insert(count, printing_list)
                    if len(printing_list) == LINE_MAX_LENGTH:
                        count += 1
                        printing_list = []

        screen.fill(WHITE)
        if active:
            color = color_active
        else:
            color = color_passive

        for i in range(count):
            input_rect = pygame.Rect(COMMENT_BOX_X_POS, COMMENT_BOX_Y_POS + COMMENT_BOX_HEIGHT * i, COMMENT_BOX_WIDTH, COMMENT_BOX_HEIGHT)
            rect_list.append(input_rect)
        # input_rect.w = max(100, text_surface.get_width() + 10)

        for rect in rect_list:
            pygame.draw.rect(screen, color, rect)

        for text in range(len(text_list)):
            print(text_list[text])
            text_surface = base_font.render("".join(text_list[text]), True,
                                            WHITE)
            screen.blit(text_surface, (GUESS_X_POS, GUESS_Y_POS + COMMENT_BOX_HEIGHT * text))

        cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
        screen.blit(cursor_img, cursor_img_rect)  # draw the cursor

        pygame.display.flip()
        clock.tick(60)

    print("yay!")


# g_player_main()