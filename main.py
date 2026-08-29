import pygame

pygame.init()

largura = 800
altura = 500

janela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Tetris Python")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()