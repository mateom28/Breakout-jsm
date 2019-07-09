import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Bloque (Sprite):
    def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.imagenes = util.cargar_imagen('imagenes/bloque.png')
		self.rect = self.imagenes.get_rect()
		self.rect.move_ip(coord[0], coord[1])   
		self.velocidad=0
		self.dir = "r"
    def update(self):
		if self.dir == "l":
			self.rect.x -= self.velocidad
		elif self.dir == "r":
			self.rect.x += self.velocidad
		if self.rect.x<=0:
                        self.rect.y += 0
			self.dir="r"
		if self.rect.x>=340:
                        self.rect.y += 0
			self.dir="l"
