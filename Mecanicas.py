import pygame
from Sprites import *

def mover_circulo (teclas, x, y, velocidade = 10):
    if teclas[ord('w')]:  # cima
        y -= velocidade
    if teclas[ord('s')]:  # baixo
        y += velocidade
    if teclas[ord('a')]:  # esquerda
        x -= velocidade
    if teclas[ord('d')]:  # direita
        x += velocidade
    return x, y

def seguir_mouse ():
    x, y = pygame.mouse.get_pos()
    return x, y