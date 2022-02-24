# initialisera
import pygame, sys
from pygame import mixer
from pygame.locals import *
pygame.init()
HEIGHT = 500
WIDTH = 500
VOLUME = 0.01
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ljud")

# klocka
FPS = 30
fpsclock = pygame.time.Clock()

# färger
WHITE = (255, 255, 255)

# bild
holgImg = pygame.image.load('bild.jpg')
imgx = (WIDTH - holgImg.get_width()) // 2
imgy = HEIGHT-holgImg.get_height()
speed_y = 0

pygame.mixer.music.load('cantina.mp3')
mixer.music.set_volume(5*VOLUME)
pygame.mixer.music.play(-1) # -1 betyder repetera i all evighet

# game loop
while True:
    DISPLAYSURF.fill(WHITE)
    imgy += speed_y
    if imgy < HEIGHT-holgImg.get_height():
        speed_y += 5    # acceleration
    else:
        speed_y = 0
        imgy = imgy = HEIGHT-holgImg.get_height()
    DISPLAYSURF.blit(holgImg, (imgx, imgy))
    fpsclock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            jump = pygame.mixer.Sound('jump.mp3')
            jump.set_volume(VOLUME)
            pygame.mixer.Channel(0).play(jump)
            speed_y = -60
    pygame.display.update()
