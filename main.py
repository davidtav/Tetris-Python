import pygame

pygame.init()

largura = 800
altura = 500

janela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((20,20,20))
    pygame.display.update()
    clock.tick(60)        

pygame.quit()