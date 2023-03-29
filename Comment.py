from Constants import *
import pygame
from helpers import *


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        comment_font = pygame.font.SysFont("chalkduster.ttf", GUESS_SIZE)
        comment_text = comment_font.render(self.text, True, BLACK)
        screen.blit(comment_text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * comment_num)])