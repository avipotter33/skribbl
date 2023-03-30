import socket
import pickle
import pygame
import threading
import os
import translators as ts
from main_player2 import main_player2
import random
from drawing_player import *

# def receive_image:
#     global received_image
from Constants import *

def game_loop():
    # initialize Pygame
    pygame.init()

    # init the socket
    # TODO: constants
    HOST = '192.168.128.254'  # TODO: replace with the IP address of the server computer
    PORT = 5000

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    client_socket.connect((HOST, PORT))

    # get player index
    player_index = int(client_socket.recv(1024).decode())
    print(player_index)

    # window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # pygame.display.set_caption("Skribble")

    running = True

    change_player_index = False

    for i in range(NUM_OF_ROUNDS):
        score = 0
        list_of_words = WORDS_LEVEL1
        rnd_level1 = random.choice(list_of_words)
        list_of_words.remove(rnd_level1)
        if player_index == 0:
            # #TODO: screen setup here
            # # set up the drawing surface
            # drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            # drawing_surface.fill(WHITE)
            #
            # # set up the drawing tools
            # brush_size = BRUSH_SIZE
            # brush_color = BLACK
            #
            # clicked_save = False
            # # start the game loop
            # while running:
            #     # handle events
            #     for event in pygame.event.get():
            #         if event.type == pygame.QUIT:
            #             running = False
            #         elif event.type == pygame.MOUSEBUTTONDOWN:
            #             if event.button == 1:  # left mouse button
            #                 mouse_y_pos = pygame.mouse.get_pos()[1]
            #                 mouse_x_pos = pygame.mouse.get_pos()[0]
            #                 if 20 < mouse_x_pos < 20 + 50 and 50 < mouse_y_pos < 100:
            #                     pygame.image.save(drawing_surface, os.path.join("screenshots", f"screenshot.png"))
            #                     clicked_save = True
            #                 else:
            #                     pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)
            #                     last_pos = event.pos
            #             elif event.button == 3:  # right mouse button
            #                 # undo last path
            #                 drawing_surface.fill(WHITE)
            #         elif event.type == pygame.MOUSEMOTION:
            #             if event.buttons[0]:  # left mouse button
            #                 pygame.draw.line(drawing_surface, brush_color, last_pos, event.pos, brush_size)
            #                 last_pos = event.pos
            #
            #     rect = pygame.Rect(20, 50, 50, 50)
            #     pygame.draw.rect(drawing_surface, BLACK, rect)
            #
            #     # update the screen
            #     window.blit(drawing_surface, (0, 0))
            #     pygame.display.flip()

            dr_player = drawing_player(rnd_level1)
            dr_player.dp_main()
            # Read the image data from a file
            with open("screenshots/screenshot.png", "rb") as f:
                image_to_bytes = f.read()

            # send the move to the server
            client_socket.sendall(image_to_bytes)

            # receive the result from the server
            result = client_socket.recv(1024)

            print(result.decode())

            clicked_save = False
        else:
            while running:
                # image_data = client_socket.recv(10000)
                # with open(os.path.join("saved_drawings", "image.png"),"wb") as f:
                #     f.write(image_data)
                # image = pygame.image.load(os.path.join("saved_drawings", f"image.png"))
                hm_screen = main_player2(rnd_level1, COUNTER, score)
                score = hm_screen.g_player_main(client_socket)
                change_player_index = True
                break
            break

        if change_player_index:
            if player_index == 0:
                player_index = 1
            else:
                player_index = 0
            change_player_index = False


            # image = pygame.transform.scale(image,(WINDOW_WIDTH ,WINDOW_HEIGHT))

            # update the screen
            # window.blit(image,(0,0))
            # pygame.display.flip()

        # quit Pygame
        pygame.quit()

