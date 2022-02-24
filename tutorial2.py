# initialisera
import pygame, sys
from pygame.locals import *
pygame.init()
HEIGHT = 500
WIDTH = 500
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bilder, animation och användarkontroll")

# klocka
FPS = 30
fpsclock = pygame.time.Clock()

# färger
WHITE = (255, 255, 255)

# bild
holgImg = pygame.image.load('bild.jpg')
imgx = 10
imgy = 10
direction = "right"

# game loop
while True:
    DISPLAYSURF.fill(WHITE)
    if direction == "right":
        imgx += 10
    else:
        imgx -= 10
    if imgx >= WIDTH - holgImg.get_width():
        direction = "left"
    if imgx <= 0:
        direction = "right"
    DISPLAYSURF.blit(holgImg, (imgx, imgy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP and imgy > 0:
                imgy -= 10
            if event.key == pygame.K_DOWN and imgy < HEIGHT - holgImg.get_height():
                imgy += 10
    fpsclock.tick(FPS)
    pygame.display.update()
