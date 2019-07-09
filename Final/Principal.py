import sys, pygame, util
from pygame.locals import *
from Barra import *
from Bloque import *

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 440
ICON_SIZE = 32

def game():

    pygame.init()
    pygame.mixer.init()
    jugando = True
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Breakout JSM')
    fuente = pygame.font.Font(None, 30)
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    barra = Barra()
    bloque = [Bloque((20,10),2),Bloque((60,10),2),Bloque((100,10),2),Bloque((140,10),2),Bloque((180,10),2),Bloque((220,10),2),Bloque((260,10),2),Bloque((300,10),2),Bloque((20,40),2),Bloque((60,40),2),Bloque((100,40),2),Bloque((100,40),2),Bloque((140,40),2),Bloque((180,40),2),Bloque((220,40),2),Bloque((260,40),2),Bloque((300,40),2)]
    while jugando:
        barra.update()
        for n in bloque:
              n.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                sys.exit()       
        screen.blit(background_image, (0,0))
        screen.blit(barra.imagenes, barra.rect)
        for n in bloque:
            screen.blit(n.imagenes, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
      game()
