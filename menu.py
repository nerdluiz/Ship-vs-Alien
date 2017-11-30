# -- coding: UTF-8 --
import random
import pygame
from pygame.locals import *
from pygame import Rect
from sys import exit

pygame.init()

#Tamanho da tela
screen = pygame.display.set_mode((800, 600), 0, 32)

# Nome do Jogo
pygame.display.set_caption("ONE TOUCH")

#Text
title = pygame.font.Font('newspace.ttf', 100)
title2 = pygame.font.Font('newspace.ttf', 65)
subs = pygame.font.Font('A-Space Black Demo.otf', 40)
pressSpace = subs.render("Press <SPACE> to Start", True, (255, 255, 255))
one = title.render("ONE", True, (255, 255, 255))
touch = title2.render("TOUCH TO DEATH", True, (255, 255, 255))
#Background
bkg = pygame.image.load('bkg.png').convert_alpha()
# Rodando
while True:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bkg, (0, 0))
    screen.blit(pressSpace, (80, 500))
    screen.blit(one, (250, 200))
    screen.blit(touch,(10, 300))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                import shipvsalien
                print 'Entrou'




    pygame.display.update()