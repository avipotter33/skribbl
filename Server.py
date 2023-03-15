import socket
import threading
import pickle

HOST = ''  # listen on all available network interfaces
PORT = 5000  # use a non-reserved port number

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket object to a specific host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

# Get the hostname of the machine
hostname = socket.gethostname()

# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)

# Print the IP address
print(f"IP address: {ip_address}")

print(f"Server is listening on port {PORT}")

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
    data = player1.recv(1024)
    player1.send(b'ok')
    player2.send(data)

# close the connections and the socket object
player1.close()
player2.close()
server_socket.close()
