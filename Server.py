import socket
import asyncio
import threading
import pickle
from Constants import *

# create a socket object
server_socket = socket.socket()

HOST = ''  # listen on all available network interfaces
PORT = 6000  # use a non-reserved port number

# bind the socket object to a specific host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen(5)

print("server running")

# accept two client connections
player1, address1 = server_socket.accept()
print("accepted connection")
player1.send(b'0')
print(f"Player 1 connected from {address1}")
player2, address2 = server_socket.accept()
player2.send(b'1')
print(f"Player 2 connected from {address2}")

while True:
    # Receive the image data from player0
    data = player1.recv(IMAGE_SIZE)
    player2.send(data)


# close the connections and the socket object
player1.close()
player2.close()
server_socket.close()
