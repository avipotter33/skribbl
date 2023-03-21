import socket
import os
import pickle
import pygame
from Constants import *

HOST = '192.168.4.254'  # replace with the IP address of the server computer
PORT = 6000

# create a socket object
client_socket = socket.socket()

# connect to the server
client_socket.connect((HOST, PORT))

# get player index
player_index = int(client_socket.recv(1024).decode())
print(player_index)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw on the Screen")


running = True

if player_index == 0:
    # set up the drawing surface
    drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    drawing_surface.fill(WHITE)

    # set up the drawing tools
    brush_size = BRUSH_SIZE
    brush_color = BLACK

    clicked_save = False
    # start the game loop
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button
                    mouse_y_pos = pygame.mouse.get_pos()[1]
                    mouse_x_pos = pygame.mouse.get_pos()[0]
                    if 20 < mouse_x_pos < 20 + 50 and 50 < mouse_y_pos < 100:
                        pygame.image.save(drawing_surface, os.path.join("screenshots", f"screenshot.png"))
                        clicked_save = True
                    else:
                        pygame.draw.circle(drawing_surface, brush_color, event.pos, brush_size)
                        last_pos = event.pos
                elif event.button == 3:  # right mouse button
                    # undo last path
                    drawing_surface.fill(WHITE)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # left mouse button
                    pygame.draw.line(drawing_surface, brush_color, last_pos, event.pos, brush_size)
                    last_pos = event.pos

        rect = pygame.Rect(20, 50, 50, 50)
        pygame.draw.rect(drawing_surface, BLACK, rect)

        # update the screen
        window.blit(drawing_surface, (0, 0))
        pygame.display.flip()

        if clicked_save:
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
        image_data = client_socket.recv(1024)
        with open(os.path.join("saved_drawings", f"image.png"),"wb") as f:
            f.write(image_data)
        image = pygame.image.load(os.path.join("saved_drawings", f"image.png"))
        image = pygame.transform.scale(image,(WINDOW_WIDTH ,WINDOW_HEIGHT))

        # update the screen
        window.blit(image,(0,0))
        pygame.display.flip()

# quit Pygame
pygame.quit()

