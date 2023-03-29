# Create Buttons: like, comment, change_image, view more comments
from Button import Button
from Constants import *

play_button = Button(PLAY_BTN_X_POS + 20,
                     PLAY_BTN_Y_POS - 41,
                     PLAY_BTN_WIDTH,
                     PLAY_BTN_HEIGHT)

colors = Button(COLORS_X_POS, COLORS_Y_POS - 15, COLORS_WIDTH, COLORS_HEIGHT)

red_button = Button(COLOR_CIRCLE_X_POS, COLOR_CIRCLE_Y_POS, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

orange_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_Y_POS, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

yellow_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 2, COLOR_CIRCLE_Y_POS, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

green_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 3, COLOR_CIRCLE_Y_POS, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

cyan_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 4, COLOR_CIRCLE_Y_POS, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

dark_blue_button = Button(COLOR_CIRCLE_X_POS, COLOR_CIRCLE_Y_POS + COLOR_CIRCLE_HEIGHT, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

purple_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_Y_POS + COLOR_CIRCLE_HEIGHT, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

pink_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 2, COLOR_CIRCLE_Y_POS + COLOR_CIRCLE_HEIGHT, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

brown_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 3, COLOR_CIRCLE_Y_POS + COLOR_CIRCLE_HEIGHT, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

black_button = Button(COLOR_CIRCLE_X_POS + COLOR_CIRCLE_WIDTH * 4, COLOR_CIRCLE_Y_POS + COLOR_CIRCLE_HEIGHT, COLOR_CIRCLE_WIDTH, COLOR_CIRCLE_HEIGHT)

eraser_button = Button(ERASER_TOOL_X_POS, ERASER_TOOL_Y_POS, ERASER_TOOL_WIDTH, ERASER_TOOL_HEIGHT)

trash_can_button = Button(TRASH_TOOL_X_POS, TRASH_TOOL_Y_POS, TRASH_TOOL_WIDTH, TRASH_TOOL_HEIGHT)

button_he = Button(HE_BTN_X_POS, HE_BTN_Y_POS, lang_button_width, lang_button_height)
button_en = Button(EN_BTN_X_POS, EN_BTN_Y_POS, lang_button_width, lang_button_height)
button_ru = Button(RU_BTN_X_POS, RU_BTN_Y_POS, lang_button_width, lang_button_height)
button_ar = Button(AR_BTN_X_POS, AR_BTN_Y_POS, lang_button_width, lang_button_height)
button_fr = Button(FR_BTN_X_POS, FR_BTN_Y_POS, lang_button_width, lang_button_height)
button_sp = Button(SP_BTN_X_POS, SP_BTN_Y_POS, lang_button_width, lang_button_height)

board_button = Button(BOARD_X_POS, BOARD_Y_POS, BOARD_WIDTH, BOARD_HEIGHT + 20)