from main_player2 import main_player2
import pygame
from Constants import *
from Image import Image

image = pygame.image.load('screenshots/screenshot.png')


def main():
    score = 0
    for i in range(20):
        hm_screen = main_player2(image, "shnizel", COUNTER, score)
        score = hm_screen.g_player_main()
        print(score)



main()