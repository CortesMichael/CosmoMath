import pygame

VERMELHO = (255, 0, 0)
TELA = pygame.display.get_surface()

class Tiro:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 15)

    def mover(self):
        self.rect.y -= 10

    def desenhar(self):
        pygame.draw.rect(TELA, VERMELHO, self.rect)
