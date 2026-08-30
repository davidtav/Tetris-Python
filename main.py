import pygame

pygame.init()

largura = 800
altura = 500

janela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()  #controla FPS

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((20,20,20)) #cor RGB
    pygame.draw.rect(
        janela, 
        (0,200,255),     #cor RGB
        # x   y  l   a (onde l = largura e a de altura)
        (200,150,30,30)  #retangulo
    )
    pygame.display.update()
    clock.tick(60)       #60 FPS   

pygame.quit()