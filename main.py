import pygame

# inicializar o pygame
pygame.init()

# dimensões da tela
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Spaceship Game")

# manter a tela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))  # pinta o fundo de preto
    pygame.display.update()

pygame.quit()