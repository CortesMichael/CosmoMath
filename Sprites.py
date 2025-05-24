import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

def carregar_nave():
    nave = pygame.image.load("assets/imagens/spaceship.png").convert_alpha()
    nave = pygame.transform.scale(nave, (100, 100))
    return nave

def desenhar_nave(tela, nave, x, y):
    rect = nave.get_rect(center=(x, y))
    tela.blit(nave, rect)