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
        if ((x_pos <= home_screen.mouse_pos[0] <= x_pos + button_width) and
                (y_pos <= home_screen.mouse_pos[1] <= y_pos + lbutton_height)):
            pygame.draw.rect(screen, LIGHT_BLUE, lang_window)
            #TODO: images
            add_image(image, HE_BTN_X_POS, HE_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, EN_BTN_X_POS, EN_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, RU_BTN_X_POS, RU_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, AR_BTN_X_POS, AR_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, FR_BTN_X_POS, FR_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)
            add_image(image, SP_BTN_X_POS, SP_BTN_Y_POS, LANG_WIDTH, LANG_HEIGHT, screen)

            if ((100 >= home_screen.mouse_pos[0] or home_screen.mouse_pos[0]>=600) and
                    (50 >= home_screen.mouse_pos[1] or home_screen.mouse_pos[1]>=450)):

                # TODO: run main
            screen.blit(lang_text, [250, 60])
            # TODO: size??