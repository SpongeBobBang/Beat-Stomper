import pygame
from pygame.locals import *
from sys import exit

blank_surface = pygame.Surface((256, 256))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))
