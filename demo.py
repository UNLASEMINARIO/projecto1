import pygame,sys
from pygame.locals import*
def main():
    pygame.init()
    pantalla=pygame.display.set_mode([800,600])
    salir=False
    reloj1=pygame.time.Clock()
    blanco=(240,255,252)
    color=(250,68,35)
    s1=pygame.Surface((800,100))
    s1.fill(color)

    while salir!=True:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                salir=True

        reloj1.tick(30)
        pantalla.fill(blanco)
        pantalla.blit(s1,[0,500])
        pygame.display.update()

    pygame.quit()

main()
