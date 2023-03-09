import socket

HOST = ''  # listen on all available network interfaces
PORT = 5000  # use a non-reserved port number

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket object to a specific host and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

print(f"Server is listening on port {PORT}")

# accept two client connections
player1, address1 = server_socket.accept()
print(f"Player 1 connected from {address1}")
player2, address2 = server_socket.accept()
print(f"Player 2 connected from {address2}")

# send screen to each player
player1.send(100)
player2.send(100)

# start the game loop
while True:
    # receive a move from player 1
    move1 = player1.recv(1024)
    if not move1:
        print("Player 1 disconnected")
        break

    # receive a move from player 2
    move2 = player2.recv(1024)
    if not move2:
        print("Player 2 disconnected")
        break

    # determine the winner and send the result to each player
    if move1 == b"rock" and move2 == b"scissors":
        player1.send(b"You win!")
        player2.send(b"You lose!")
    elif move1 == b"paper" and move2 == b"rock":
        player1.send(b"You win!")
        player2.send(b"You lose!")
    elif move1 == b"scissors" and move2 == b"paper":
        player1.send(b"You win!")
        player2.send(b"You lose!")
    elif move1 == move2:
        player1.send(b"It's a tie!")
        player2.send(b"It's a tie!")
    else:
        player1.send(b"You lose!")
        player2.send(b"You win!")

# close the connections and the socket object
player1.close()
player2.close()
server_socket.close()
