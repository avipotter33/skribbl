from main_player2 import main_player2
import pygame

def main():
    image = pygame.image.load('screenshots/screenshot.png')
    hm_screen = main_player2(image)
    hm_screen.g_player_main()

main()