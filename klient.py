# importera bibliotek och initialisera konstanter
import pygame, sys
from pygame.locals import *
SURFHEIGHT = 500
SURFWIDTH = 500
SQUARESIDE = 10

# färger
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
color_strings = {RED: "red", "red": RED, GREEN: "green", "green": GREEN, BLUE: "blue", "blue": BLUE, BLACK: "black", "black": BLACK}

# anslut till server och läs in data
from socket import *
conn = socket()
host = input("Ange serverns IP-adress: ")
# host = "localhost"    # för testning/avlusning
port = 12345
conn.connect((host, port))
b = conn.recv(1024)
msg = b.decode('utf-16')

# initialisera stats
mycolor = RED
mypos = [0, 0]
mycolor = color_strings[msg]
if msg == "green":
    mypos = [0, SURFHEIGHT - SQUARESIDE]
if msg == "blue":
    mypos = [SURFWIDTH - SQUARESIDE, 0]
if msg == "black":
    mypos = [SURFWIDTH - SQUARESIDE, SURFHEIGHT - SQUARESIDE]
all_pos = {}

# starta spelet
pygame.init()
DISPLAYSURF = pygame.display.set_mode((SURFWIDTH, SURFHEIGHT))
pygame.display.set_caption("Användarkontroll över nätverk")

# klocka
FPS = 30
fpsclock = pygame.time.Clock()

# tråd för att lyssna på servern och hantera meddelanden
def listen_to_server(conn):
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        msg = msg.split(":")
        color = msg[0]
        msg = msg[1].split(",")
        pos = [int(msg[0][1:]), int(msg[1][1:-1])]
        all_pos[color] = pos
        print(all_pos)
        
from _thread import *
start_new_thread(listen_to_server, (conn, ))

# game loop
while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, mycolor, (mypos[0], mypos[1], SQUARESIDE, SQUARESIDE))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT and mypos[0] > 0:
                mypos[0] -= 10
            if event.key == pygame.K_RIGHT and mypos[0] < SURFWIDTH - SQUARESIDE:
                mypos[0] += 10
            if event.key == pygame.K_UP and mypos[1] > 0:
                mypos[1] -= 10
            if event.key == pygame.K_DOWN and mypos[1] < SURFHEIGHT - SQUARESIDE:
                mypos[1] += 10
            msg = color_strings[mycolor] + ":" + str(mypos)
            b = msg.encode("utf-16")
            conn.send(b)
    fpsclock.tick(FPS)
    for color in all_pos:
        if color != mycolor:
            pygame.draw.rect(DISPLAYSURF, color, (all_pos[color][0], all_pos[color][1], SQUARESIDE, SQUARESIDE))
    pygame.display.update()