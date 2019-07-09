import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Barra (Sprite):
    def __init__(self):
        Sprite.__init__(self)
	self.imagenes = util.cargar_imagen('imagenes/barra.png')
	self.rect = self.imagenes.get_rect()
	self.rect.centerx = 360/2
	self.rect.centery = 440-30
	self.vida = True
    def update(self):
	teclas = pygame.key.get_pressed()
	if teclas[K_LEFT] and self.rect.x>=5:
	    self.rect.x -= 4
	elif teclas[K_RIGHT] and self.rect.x<=355-self.rect.width:
            self.rect.x += 4

