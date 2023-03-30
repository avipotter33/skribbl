from Constants import *
from helpers import *
from buttons import *
import drawing_player
from drawing_player import drawing_player
from main2 import home_screen


class lang_window(drawing_player):
    lang_window = pygame.Rect(100, 50, LANG_WIDTH, LANG_HEIGHT)
    def run(self):
        # TODO: where is the language button???
        if ((EARTH_X_POS <= home_screen.mouse_pos[0] <= EARTH_X_POS + EARTH_WIDTH) and
                (EARTH_Y_POS <= home_screen.mouse_pos[1] <= EARTH_Y_POS + EARTH_HEIGHT)):
            pygame.draw.rect(screen, LIGHT_BLUE, lang_window)
            #TODO: images
            add_image(image, HE_BTN_X_POS, HE_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, EN_BTN_X_POS, EN_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, RU_BTN_X_POS, RU_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, AR_BTN_X_POS, AR_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, FR_BTN_X_POS, FR_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, SP_BTN_X_POS, SP_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)

            if ((EARTH_X_POS <= home_screen.mouse_pos[0] <= EARTH_X_POS + EARTH_WIDTH) and
                    (EARTH_Y_POS <= home_screen.mouse_pos[1] <= EARTH_Y_POS + EARTH_HEIGHT)):
                self.display_image = True
            if self.display_image:
                self.display_image = False
            screen.blit(lang_text, [250, 60])
# TODO: size??