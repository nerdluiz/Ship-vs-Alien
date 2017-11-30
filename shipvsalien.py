# -- coding: UTF-8 --
import random
import pygame
from pygame.locals import *
from pygame import Rect
from sys import exit

pygame.init()

changePosY = random.randint(0,544)

class Shoot ():
    def __init__(self, pos_Y):
        self.pos_Y = pos_Y + 12
        self.pos_X = 90
        self.rect = pygame.Rect(self.pos_X, self.pos_Y, 17, 39)

    def movementX(self):
        self.pos_X += 3
        self.rect = pygame.Rect(self.pos_X, self.pos_Y, 17, 39)

class Alien():
    def __init__(self):
        self.alien_Y = random.randint(0,544)
        self.alien_X = 900
        self.rect = pygame.Rect(self.alien_X, self.alien_Y, 51, 56)

    def AlienMovement(self):
        self.alien_X -= 1
        self.rect = pygame.Rect(self.alien_X, self.alien_Y, 51, 56)

# Tamanho da tela
screen = pygame.display.set_mode((800, 600), 0, 32)
# Nome do Jogo
pygame.display.set_caption("ONE TOUCH")
# Backgroung
background = pygame.image.load('bkg.png').convert()
# Spaceship - Imagem, posição e velocidade
spaceship = pygame.image.load('ship.png').convert_alpha()
speed = 1
shipX = 50
shipY = 300

#Som tiros
Sound = pygame.mixer.Sound('1.ogg')



# Música
pygame.mixer.music.load('musictheme.ogg')
pygame.mixer.music.play(-1, 0.0)

# Tiro
shootIMG = pygame.image.load('shoot.png').convert_alpha()
shoot_obj = None
tiros = []
# Alien
alienIMG = pygame.image.load('alien.png').convert_alpha()
baseY = 100
alien_obj = None
aliens = []

pygame.key.set_repeat(1, 1)

cooldown_tiro = 50
cooldown = 0

#Sons
tiro_sound = pygame.mixer.Sound('1.ogg')
alien_sound = pygame.mixer.Sound('shoot destroy 1.ogg')


# Rodando
while True:
    ShipRect = pygame.Rect(shipX, shipY, 47, 64)
    cooldown += 1
    # Background
    screen.blit(background, (0, 0))
    # inputs_speceship and shot
    ShipMovement = pygame.key.get_pressed()

    if ShipMovement[K_UP]:
        shipY -= speed
    elif ShipMovement[K_DOWN]:
        shipY += speed

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tiro_sound.play(loops = 0)
                if cooldown > cooldown_tiro:
                    tiros.append(Shoot(shipY))
                    aliens.append(Alien())
                    cooldown = 0

    # colisão nave
    # colisão_com_bordas
    if shipY < 0:
        shipY = 0
    if shipY > 536:
        shipY = 536

    # lista_tiros
    if len(tiros) > 0:
        for shoot_obj in tiros:
            shoot_obj.movementX()
            screen.blit(shootIMG, (shoot_obj.pos_X, shoot_obj.pos_Y))

    # lista_alien
    if len(aliens) > 0:
        for alien_obj in aliens:
            alien_obj.AlienMovement()
            screen.blit(alienIMG, (alien_obj.alien_X, alien_obj.alien_Y))

    for alien_index, alien in enumerate(aliens):
        for shoot_index, shoot in enumerate(tiros):
            if shoot.rect.colliderect(alien.rect):
                tiro_sound.stop()
                alien_sound.play(loops = 0)
                tiros.pop(shoot_index)
                aliens.pop(alien_index)
        if alien.rect.colliderect(ShipRect):
            aliens.pop(alien_index)
            print 'GAME OVER!'
            import Lose

    for shoot_index, shoot in enumerate(tiros):
        if shoot.pos_X >= 800:
            tiros.pop(shoot_index)
    #print tiros



    screen.blit(spaceship, (shipX, shipY))

    pygame.display.update()