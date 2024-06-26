import translators as ts
from Constants import *
from helpers import *
from buttons import *
import drawing_player
from drawing_player import drawing_player
from main2 import home_screen

class Tranlator(drawing_player):
    #עברית אנגלית רוסית ערבית צרפתית ספרדית


    #font = pygame.font.SysFont('David', PLAY_TEXT_SIZE)
    #text = font.render(PLAY_TEXT, True, WHITE)

    lang_button_list = [button_he, button_en, button_ru, button_ar, button_fr, button_sp]
    lang_button_X_pos = [HE_BTN_X_POS, EN_BTN_X_POS, RU_BTN_X_POS, AR_BTN_X_POS, FR_BTN_X_POS, SP_BTN_X_POS]
    lang_button_Y_pos = [HE_BTN_Y_POS, EN_BTN_Y_POS, RU_BTN_Y_POS, AR_BTN_Y_POS, FR_BTN_Y_POS, SP_BTN_Y_POS]

    lang = 'en'
    for index in range(6):
        if ((lang_button_X_pos[index] <= home_screen.mouse_pos[0] <= lang_button_X_pos[index] + lang_button_width) and (
                lang_button_Y_pos[index] <= home_screen.mouse_pos[1] <= lang_button_Y_pos[index] + lang_button_height)):
            lang = lang_button_list[-2:]

    TEXTS_TO_TRANSLATE = [PLAY_TEXT, drawing_player.rnd_Level1]
    for index in TEXTS_TO_TRANSLATE:
        i = ts.translate_text(index, to_language=lang)
        if (lang == 'he'):
            index = index[::-1]
