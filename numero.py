import pygame

# Cores
LARANJA_CLARO = (255, 180, 60)
LARANJA_ESCURO = (200, 70, 0)
BRANCO = (255, 255, 255)

# Fonte
try:
    FONTE = pygame.font.Font("assets/press-start-2p-font/PressStart2P.ttf", 20)
except:
    FONTE = pygame.font.SysFont("Arial", 20)

class Numero:
    def __init__(self, valor, x, y):
        self.valor = valor
        self.rect = pygame.Rect(x, y, 50, 50)
        self.acertado = False
        self.surface = self._gerar_gradiente()

    def mover(self):
        self.rect.y += 2.2

    def desenhar(self):
        tela = pygame.display.get_surface()
        tela.blit(self.surface, self.rect.topleft)

        # Texto centralizado
        texto = FONTE.render(str(self.valor), True, BRANCO)
        texto_rect = texto.get_rect(center=self.rect.center)
        tela.blit(texto, texto_rect)

    def _gerar_gradiente(self):
        raio = self.rect.width // 2
        surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)

        # Desenha círculos concêntricos para criar o gradiente
        for r in range(raio, 0, -1):
            cor = self._interpolar_cor(LARANJA_CLARO, LARANJA_ESCURO, r / raio)
            pygame.draw.circle(surface, cor, (raio, raio), r)

        return surface

    def _interpolar_cor(self, cor1, cor2, fator):
        """Interpolação entre duas cores (de fora para dentro)."""
        return (
            int(cor1[0] * (1 - fator) + cor2[0] * fator),
            int(cor1[1] * (1 - fator) + cor2[1] * fator),
            int(cor1[2] * (1 - fator) + cor2[2] * fator)
        )
