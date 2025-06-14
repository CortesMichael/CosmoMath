import pygame
from Sprites import *
from Mecanicas import *

pygame.init()

# Tela e controle
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CosmoMath")
tempo = pygame.time.Clock()

# Estados do jogo
MENU = "menu"
JOGO = "jogo"
GAME_OVER = "game_over"
estado = MENU

# Pontuação
pontos = 0
fonte_pontos = pygame.font.SysFont("Comic Sans", 28)

# Nave
sprite_nave = carregar_nave()
x_nave, y_nave = 400, 500

# Asteroide
asteroide = Asteroide(400, 0, 1.5)

# manter a tela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if estado == MENU:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao.collidepoint(mouse_pos):
                    estado = JOGO  # inicia o jogo

        elif estado == JOGO:
            
            if evento.type == pygame.KEYDOWN:
                teclas = pygame.key.get_pressed()
                x, y = mover_circulo(teclas, x, y)
                pass

        elif estado == GAME_OVER:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if botao_gameover.collidepoint(mouse_pos):
                    # Reinicia o jogo
                    pontos = 0
                    asteroide = Asteroide(400, 0, 1.5)
                    estado = JOGO
                    
    # Lógica de exibição
    tela.fill(PRETO)

    if estado == MENU:
        botao = desenhar_menu(tela)

    elif estado == JOGO:
        asteroide.atualizar(tela)
        desenhar_nave(tela, sprite_nave, x_nave, y_nave)
        
        # Atualiza asteroide e nave
        asteroide.atualizar(tela)
        desenhar_nave(tela, sprite_nave, x_nave, y_nave)
        
        rect_nave = sprite_nave.get_rect(center=(x_nave, y_nave))
        rect_asteroide = asteroide.sprite.get_rect(center=(asteroide.x, asteroide.y))

        # Mostra pontuação no canto
        texto_pontos = fonte_pontos.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))
        
    elif estado == GAME_OVER:
        botao_gameover = desenhar_game_over(tela, pontos)

    pygame.display.flip()
    
    tempo.tick(60)

pygame.quit()