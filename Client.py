import socket
import pickle
import pygame

HOST = '172.16.190.43'  # replace with the IP address of the server computer
PORT = 5000

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client_socket.connect((HOST, PORT))

# get player index
player_index = client_socket.recv(1024)

# set the window size and title
# TODO: in constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw on the Screen")

# set up the colors
# TODO: in constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the drawing surface
drawing_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_surface.fill(WHITE)

# set up the drawing tools
# TODO: in constants
brush_size = 5
brush_color = BLACK

clicked_save = False
got_drawing = False

# start the game loop
running = True
if player_index == 0:
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
            client_socket.send(image_to_bytes)

            # receive the result from the server
            result = client_socket.recv(1024)

            print(result.decode())

            # Make sure to only update this client's screen
            client_socket.sendall(b'update')

            clicked_save = False
else:
    while running:
        if not got_drawing:
            image_data = client_socket.recv(1024)
            with open(os.path.join("saved_drawings", f"image.png"),"wb") as f:
                f.write(image_data)
            image = pygame.image.load(os.path.join("saved_drawings", f"image.png"))
            image = pygame.transform.scale(image,(WINDOW_WIDTH ,WINDOW_HEIGHT))
            got_drawing = True

        # update the screen
        window.blit(image,(0,0))
        pygame.display.flip()

# quit Pygame
pygame.quit()

