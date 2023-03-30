from Constants import *
from helpers import *
from buttons import *
import drawing_player
from drawing_player import drawing_player
from main2 import home_screen


class lang_window(drawing_player):
    lang_window = pygame.Rect(100, 50, LANG_WIDTH, LANG_HEIGHT)

    def run(self):
        pygame.draw.rect(screen, LIGHT_BLUE, lang_window)
        if ((EARTH_X_POS <= home_screen.mouse_pos[0] <= EARTH_X_POS + EARTH_WIDTH) and
                (EARTH_Y_POS <= home_screen.mouse_pos[1] <= EARTH_Y_POS + EARTH_HEIGHT)):
            self.display_image = True
        if self.display_image:
            self.display_image = False
        screen.blit(lang_text, [250, 60])
# TODO: size??
