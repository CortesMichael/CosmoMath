import pygame
from Sprites import *
from Palavras import *

class Asteroide:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.palavra = palavra_aleatoria()
        self.letras_digitadas = 0
        self.sprite = carregar_bola()
        self.fonte = pygame.font.SysFont("Comic Sans", 28, bold=True)
    
    def mover(self):
        self.y += self.velocidade

    def atualizar(self, tela):
        self.mover()
        self.desenhar(tela)

    def desenhar(self, tela):
        # desenha o sprite do asteroide
        desenhar_bola(tela, self.sprite, self.x, self.y)

        # destaca letras 
        palavra_formatada = ""
        for i, letra in enumerate(self.palavra):
            if i < self.letras_digitadas:
                palavra_formatada += f"[{letra}]"
            else:
                palavra_formatada += letra

        texto_render = self.fonte.render(palavra_formatada, True, (255, 255, 255))
        texto_x = self.x - texto_render.get_width() // 2
        texto_y = self.y - 70
        tela.blit(texto_render, (texto_x, texto_y))
        
def verificar_colisao(nave_rect, asteroide_rect):
    return nave_rect.colliderect(asteroide_rect)
