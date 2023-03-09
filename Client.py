import socket
import pickle
import pygame

HOST = '172.16.190.43'  # replace with the IP address of the server computer
PORT = 5000

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# Receive screen size from server
screen_size = pickle.loads(client_socket.recv(1024))

# Set up Pygame screen
pygame.init()
screen = pygame.display.set_mode(screen_size)

# start the game loop
while True:
    # get the player's move
    move = input("Enter your move (rock, paper, scissors): ")

    # send the move to the server
    client_socket.send(move.encode())

    # receive the result from the server
    result = client_socket.recv(1024)
    print(result.decode())

# close the connection
client
