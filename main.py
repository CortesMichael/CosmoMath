# importar bibliotecas e classes
import pygame
from Sprites import *
from Mecanicas import *

# inicializar o pygame
pygame.init()

# dimensões da tela
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
tempo = pygame.time.Clock()
pygame.display.set_caption("CosmoMath")


sprite = carregar_nave()
x, y = 400, 300

# manter a tela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    teclas = pygame.key.get_pressed()
    x, y = mover_circulo(teclas, x, y)
    
    x, y = seguir_mouse()

    # pinta o fundo de preto
    tela.fill((PRETO))  
    
    desenhar_nave(tela, sprite, x, y)
    pygame.display.flip()
    
    tempo.tick(60)

pygame.quit()