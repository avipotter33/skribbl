import socket
from main_player2 import main_player2
from drawing_player import *
from Constants import *


def game_loop():
    # initialize Pygame
    pygame.init()

    # init the socket
    # TODO: constants
    HOST = '192.168.128.254'  # TODO: replace with the IP address of the server computer
    PORT = 6000

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    client_socket.connect((HOST, PORT))

    # get player index
    player_index = int(client_socket.recv(1024).decode())
    print(player_index)

    running = True

    change_player_index = False

    for i in range(NUM_OF_ROUNDS):
        score = 0
        list_of_words = WORDS_LEVEL1
        rnd_level1 = random.choice(list_of_words)
        list_of_words.remove(rnd_level1)
        if player_index == 0:
            # Read the image data from a file
            dr_player = drawing_player(rnd_level1)
            dr_player.dp_main(client_socket)
        else:
            while running:
                hm_screen = main_player2(rnd_level1, COUNTER, score)
                score = hm_screen.g_player_main(client_socket)
                change_player_index = True
                break

        if change_player_index:
            if player_index == 0:
                player_index = 1
            else:
                player_index = 0
            change_player_index = False

        # quit Pygame
        pygame.quit()


game_loop()
