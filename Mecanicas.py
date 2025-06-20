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
        
def mover_circulo (teclas, x, y, velocidade = 10):

    if teclas[ord('a')]:  # esquerda
        x -= velocidade
    if teclas[ord('d')]:  # direita
        x += velocidade
    return x, y
