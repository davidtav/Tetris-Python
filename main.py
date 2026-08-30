import pygame

pygame.init()

largura = 800
altura = 500

janela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption("Tetris Python")

clock = pygame.time.Clock()  #controla FPS

linhas = 20
colunas = 10
tamanho_celula = 25


rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((20,20,20)) #cor RGB

    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula
            pygame.draw.rect(
            janela, 
            (80,80,80),     #cor RGB
            # x   y  l   a (onde l = largura e a de altura)
            (x,y,tamanho_celula,tamanho_celula),  #retangulo
            1
    )

    pygame.display.update()
    clock.tick(60)       #60 FPS   

pygame.quit()