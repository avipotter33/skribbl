from main_player2 import main_player2
import pygame
from Constants import *


def main():
    score = 0
    for i in range(3):
        image = pygame.image.load('screenshots/screenshot.png')
        hm_screen = main_player2(image, "shnizel", COUNTER, score)
        score = hm_screen.g_player_main()
        print(score)


main()