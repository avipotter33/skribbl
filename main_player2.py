# import sys module
import pygame
import sys
from Constants import *
from helpers import *
from buttons import *
from drawing_player import drawing_player
from Comment import Comment
from Image import Image
import os
import socket
import socketserver


class main_player2(drawing_player, Image):
    def __init__(self, rnd_word, counter, score):
        self.cursor_img = pygame.image.load('Images/cursor_image.png')
        self.cursor_img = pygame.transform.scale(self.cursor_img,
                                            (CURSOR_WIDTH + 20, CURSOR_HEIGHT))
        self.cursor_img_rect = self.cursor_img.get_rect()
        self.comments = []
        self.comments_display_index = 0
        # self.drawing_board = image
        self.rnd_word = rnd_word
        self.counter = counter
        self.score = score

    def add_image(img_path, x_pos, y_pos, width, height, screen):
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))

    def add_comment(self, comment_text):
        self.comments.append(comment_text)

    def display_comments(self):
            """
            Display guesses. In case there are more than 8
            guesses, show only the last 8

            :return: None
            """
            position_index = self.comments_display_index
            if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
                starting_index = len(self.comments) - NUM_OF_COMMENTS_TO_DISPLAY
            else:
                starting_index = 0
            for i in range(starting_index, len(self.comments)):
                if position_index > NUM_OF_COMMENTS_TO_DISPLAY:
                    position_index = 0
                self.comments[i].display(position_index)
                position_index += 1
                # if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                #     break

    def add_score(self):
        self.score += self.counter
        return self.score

    def g_player_main(self, client_socket):
        pygame.init()
        clock = pygame.time.Clock()
        base_font = pygame.font.Font(None, TEXT_WHILE_WRITING_SIZE)
        user_text = ''
        timer_text = "READY?"
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        timer_font = pygame.font.SysFont('Consolas', 30)
        timer_x_pos = GUESSING_TIMER_X_POS - 25
        # counter = COUNTER
        background = pygame.image.load('Images/background_image.jpg')
        background = pygame.transform.scale(background,
                                            (WINDOW_WIDTH, WINDOW_HEIGHT))

        while True:
            pressed_enter = False
            active = False
            while not(pressed_enter):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if mouse_in_button(send_button, mouse_pos):
                            pressed_enter = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            pressed_enter = True
                        else:
                            user_text += event.unicode
                    elif event.type == pygame.USEREVENT:
                        if str(timer_text) == "READY?":
                            timer_text = "GUESS!"
                        elif str(timer_text) == "GUESS!":
                            timer_text = str(COUNTER).rjust(3)
                            timer_x_pos = GUESSING_TIMER_X_POS
                        else:
                            self.counter -= 1
                            if self.counter > 0:
                                timer_text = str(self.counter).rjust(3)
                            if self.counter == 0:
                                timer_text = "time's up!"
                                timer_x_pos = GUESSING_TIMER_X_POS - 42
                            elif timer_text == "time's up!":
                                pressed_enter = True

                screen.fill(WHITE)
                screen.blit(background, (0, 0))

                image_data = client_socket.recv(10000)
                with open(os.path.join("saved_drawings", "image.png"), "wb") as f:
                    f.write(image_data)
                image = pygame.image.load(os.path.join("saved_drawings", f"image.png"))
                self.display_image()

                add_image("images/guessing box.png", CHAT_BTN_X_POS, CHAT_BTN_Y_POS, CHAT_BTN_WIDTH, CHAT_BTN_HEIGHT, screen)
                add_image("images/score box.png", SCORE_BOX_X_POS, SCORE_BOX_Y_POS, SCORE_BOX_WIDTH, SCORE_BOX_HEIGHT,
                          screen)

                timer_font = pygame.font.SysFont("Anything Skribble", TIMER_SIZE)
                screen.blit(timer_font.render(timer_text, True, BLUE), (timer_x_pos, GUESSING_TIMER_Y_POS))

                score_font = pygame.font.SysFont("Anything Skribble", SCORE_SIZE)
                screen.blit(score_font.render(SCORE_TEXT + str(self.score), True, BLUE), (SCORE_X_POS, SCORE_Y_POS))

                if len(user_text) > LINE_MAX_LENGTH:
                    user_text = user_text[0:LINE_MAX_LENGTH]
                text_surface = base_font.render(user_text, True, BLACK)
                screen.blit(text_surface, (GUESS_X_POS, GUESS_Y_POS))

                self.display_comments()

                self.cursor_img_rect.center = (pygame.mouse.get_pos()[0] + 22, pygame.mouse.get_pos()[1] - 40) # update position
                screen.blit(self.cursor_img, self.cursor_img_rect)  # draw the cursor

                pygame.display.flip()
                clock.tick(60)

            new_comment = user_text
            comment = Comment(new_comment)
            self.add_comment(comment)
            if user_text == self.rnd_word:
                score = self.add_score()
                return score
            elif timer_text == "time's up!":
                return self.score
            user_text = ""