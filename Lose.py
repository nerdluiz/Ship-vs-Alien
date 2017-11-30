# -- coding: UTF-8 --
import pygame
from sys import exit

pygame.init()

#Tamanho da tela
screen = pygame.display.set_mode((800, 600), 0, 32)

# Nome do Jogo
pygame.display.set_caption("ONE TOUCH")

#Text
subs = pygame.font.Font('A-Space Black Demo.otf', 40)
subs_2 = pygame.font.Font('A-Space Black Demo.otf', 100)
pressSpace = subs.render("Press <SPACE> to Restart", True, (255, 255, 255))
You = subs_2.render("YOU", True, (255, 255, 255))
Lose = subs_2.render("LOSE!", True, (255, 255, 255))
#Background
bkg = pygame.image.load('bkg.png').convert_alpha()
# Rodando
while True:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bkg, (0, 0))
    screen.blit(You, (250, 200))
    screen.blit(Lose, (200, 300))

    pygame.display.update()
