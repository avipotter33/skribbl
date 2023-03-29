import pygame

from Constants import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def from_text_to_array(text):
    """
    the function get text and break it into sentences that fits the screen, in
    case the text too long to for one line
    :param text: string
        text to show on screen
    :return: list of sentences
    """
    text_array = []
    text_to_edit = text
    if len(text) > 20:
        while not (len(text_to_edit) <= 0):
            if len(text_to_edit) < LINE_MAX_LENGTH:
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[0: LINE_MAX_LENGTH]
                text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                while not (temp[-1] == ' ') and not (temp[-1] == ','):
                    text_to_edit = temp[-1] + text_to_edit
                    temp_len = int(len(temp))
                    temp = temp[0: temp_len - 1]
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def display_comments(self):
    """
    Display comments on post. In case there are more than 4
    comments, show only 4 comments chosen by reset_comments_display_index

    :return: None
    """
    position_index = self.comments_display_index
    # If there are more than 4 comments, print "view more comments"
    if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
        comment_font = pygame.font.SysFont('chalkduster.ttf',
                                           COMMENT_TEXT_SIZE)
        view_more_comments_button = comment_font.render("view more comments",
                                                        True, LIGHT_GRAY)
        screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                VIEW_MORE_COMMENTS_Y_POS))

    # Display 4 comments starting from comments_display_index
    for i in range(0, len(self.comments)):
        if position_index >= len(self.comments):
            position_index = 0
        self.comments[position_index].display(i)
        position_index += 1
        if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
            break


def last_pos_in_board(event_pos):
    event_pos = list(event_pos)
    if event_pos[0] <= BOARD_X_POS:
        event_pos[0] = BOARD_X_POS + 1
        return event_pos
    elif event_pos[0] >= BOARD_X_POS + BOARD_WIDTH:
        event_pos[0] = BOARD_X_POS + BOARD_WIDTH - 1
        return event_pos
    elif event_pos[1] <= BOARD_Y_POS:
        event_pos[1] = BOARD_Y_POS + 1
        return event_pos
    elif event_pos[1] >= BOARD_Y_POS + BOARD_HEIGHT:
        event_pos[1] = BOARD_Y_POS + BOARD_HEIGHT - 1
        return event_pos


def last_pos_outside_color_palette(event_pos):
    event_pos = list(event_pos)
    if event_pos[1] >= BOARD_Y_POS + COLORS_HEIGHT:
        event_pos[1] = BOARD_Y_POS  + COLORS_HEIGHT + 1
        return event_pos
    elif event_pos[0] <= BOARD_X_POS + COLORS_WIDTH:
        print("meow")
        event_pos[0] = BOARD_X_POS + COLORS_WIDTH + 1
        return event_pos