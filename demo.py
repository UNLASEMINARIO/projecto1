import pygame
def main():
    pygame.init()
    pantalla=pygame.display.set_mode([800,600])
    imagen1 = pygame.image.load("pacman.png")
    salir=False
    reloj1=pygame.time.Clock()
    blanco=(240,255,252)
    color=(150,254,55)
    s1=pygame.Surface((20,10))
    s1.fill(color)

    while salir!=True:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                salir=True

        reloj1.tick(30)
        pantalla.fill(blanco)
        pantalla.blit(imagen1,(0,0))
        pantalla.blit(s1,[100,200])
        pygame.display.update()

    pygame.quit()

main()
