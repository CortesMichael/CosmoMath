import pygame

LARGURA, ALTURA = 700, 900
TELA = pygame.display.get_surface()

# Tenta carregar a imagem da nave
try:
    nave_img = pygame.image.load("assets/imagens/spaceship.png")
    nave_img = pygame.transform.scale(nave_img, (60, 60))  # redimensiona, se necessário
except:
    print("Erro ao carregar imagem da nave. Usando fallback azul.")
    nave_img = pygame.Surface((137, 160))
    nave_img.fill((0, 100, 255))  # fallback azul

class Nave:
    def __init__(self):
        self.rect = nave_img.get_rect(center=(LARGURA//2, ALTURA - 70))
        self.vel = 5
        self.vidas = 3
        self.pontos = 0

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.vel

    def desenhar(self):
        TELA.blit(nave_img, self.rect)
