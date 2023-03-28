# import sys module
import pygame
import sys
from Constants import *
from helpers import *
from buttons import *
from drawing_player import drawing_player


class main_player2(drawing_player):
    def __init__(self):
        cursor_img = pygame.image.load('Images/cursor_image.png')
        cursor_img = pygame.transform.scale(cursor_img,
                                            (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
        cursor_img_rect = cursor_img.get_rect()


    def add_image(img_path, x_pos, y_pos, width, height, screen):
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))


    def g_player_main(self):
        pygame.init()
        clock = pygame.time.Clock()
        base_font = pygame.font.Font(None, 32)
        user_text = ''
        input_rect = pygame.Rect(COMMENT_BOX_WIDTH, COMMENT_BOX_HEIGHT, COMMENT_BOX_X_POS, COMMENT_BOX_Y_POS)
        color_active = pygame.Color('lightskyblue1')
        color_passive = pygame.Color('lightskyblue3')
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
                    print(pygame.mouse.get_pos())
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
                        # printing_list.append(event.unicode)
                        # text_list.insert(count, printing_list)
                        # if len(printing_list) == LINE_MAX_LENGTH:
                        #     count += 1
                        #     printing_list = []

            screen.fill(WHITE)
            if active:
                color = color_active
            else:
                color = color_passive

            add_image("images/guessing box.png", CHAT_BTN_X_POS, CHAT_BTN_Y_POS, CHAT_BTN_WIDTH, CHAT_BTN_HEIGHT, screen)

            input_rect = pygame.Rect(COMMENT_BOX_X_POS, COMMENT_BOX_Y_POS, COMMENT_BOX_WIDTH, COMMENT_BOX_HEIGHT)

            pygame.draw.rect(screen, color, input_rect)

            if active:
                if len(user_text) <= LINE_MAX_LENGTH:
                # for text in range(len(text_list)):
                #     print(text_list[text])
                    text_surface = base_font.render(user_text, True, WHITE)
                    screen.blit(text_surface, (GUESS_X_POS, GUESS_Y_POS))
                else:
                    text_surface = base_font.render(user_text[0:LINE_MAX_LENGTH], True, WHITE)
                    screen.blit(text_surface, (GUESS_X_POS, GUESS_Y_POS))

            self.cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
            screen.blit(self.cursor_img, self.cursor_img_rect)  # draw the cursor

            pygame.display.flip()
            clock.tick(60)

        # if user_text == rnd_Level1:
        #     print("yay!")


#g_player_main()