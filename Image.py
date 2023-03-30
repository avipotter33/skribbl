import pygame
from Constants import *
from helpers import *


class Image:
    def __init__(self, image):
        self.drawing_board = image

    def display_image(self):
        img = pygame.transform.scale(self.drawing_board,
                                     (BOARD_DISPLAYING_DRAWING_WIDTH, BOARD_DISPLAYING_DRAWING_HEIGHT))
        screen.blit(img, (BOARD_DISPLAYING_DRAWING_X_POS, BOARD_DISPLAYING_DRAWING_Y_POS))