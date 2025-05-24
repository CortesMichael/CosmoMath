# importar bibliotecas e classes
import pygame
from Sprites import BRANCO

# inicializar o pygame
pygame.init()

# dimensões da tela
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
tempo = pygame.time.Clock()
pygame.display.set_caption("CosmoMath")

# manter a tela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # pinta o fundo de preto
    tela.fill((BRANCO))  
    
    pygame.display.flip()
    
    tempo.tick(60)

pygame.quit()