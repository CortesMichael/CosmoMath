import pygame

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
TELA = pygame.display.get_surface()

try:
    FONTE = pygame.font.Font("assets/press-start-2p-font/PressStart2P.ttf", 20)
except:
    FONTE = pygame.font.SysFont("Arial", 20)

class Numero:
    def __init__(self, valor, x, y):
        self.valor = valor
        self.rect = pygame.Rect(x, y, 50, 50)
        self.acertado = False

    def mover(self):
        self.rect.y += 1

    def desenhar(self):
        pygame.draw.rect(TELA, BRANCO, self.rect)
        texto = FONTE.render(str(self.valor), True, PRETO)
        TELA.blit(texto, (self.rect.x + 10, self.rect.y + 10))
