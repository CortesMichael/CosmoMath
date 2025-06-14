import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (100, 100, 255)

def carregar_nave():
    nave = pygame.image.load("assets/imagens/spaceship.png").convert_alpha()
    nave = pygame.transform.scale(nave, (100, 100))
    return nave

def desenhar_nave(tela, nave, x, y):
    rect = nave.get_rect(center=(x, y))
    tela.blit(nave, rect)
    
def carregar_bola():
    bola = pygame.image.load("assets/imagens/fireball.png").convert_alpha()
    bola = pygame.transform.scale(bola, (75, 150))
    return bola

def desenhar_bola(tela, bola, x, y):
    rect = bola.get_rect(center=(x, y))
    tela.blit(bola, rect)

def desenhar_menu(tela):
    fonte = pygame.font.SysFont("Comic-sans", 40, bold=True)
    tela.fill(PRETO)

    # titulo
    titulo = fonte.render("CosmoWords", True, BRANCO)
    tela.blit(titulo, (tela.get_width() // 2 - titulo.get_width() // 2, 150))

    # botao
    botao = pygame.Rect(300, 300, 200, 60)
    cor_botao = (100, 100, 255)

    pygame.draw.rect(tela, cor_botao, botao, border_radius=15)

    texto_botao = fonte.render("Start", True, BRANCO)
    texto_x = botao.x + (botao.width - texto_botao.get_width()) // 2
    texto_y = botao.y + (botao.height - texto_botao.get_height()) // 2
    tela.blit(texto_botao, (texto_x, texto_y))

    return botao

def desenhar_game_over(tela, pontos):
    fonte_titulo = pygame.font.SysFont("Comic Sans", 50, bold=True)
    fonte_texto = pygame.font.SysFont("Comic Sans", 32)
    
    tela.fill((30, 0, 0))

    texto1 = fonte_titulo.render("Você perdeu", True, (255, 0, 0))
    texto2 = fonte_texto.render(f"Pontos: {pontos}", True, BRANCO)
    texto3 = fonte_texto.render("Jogar Novamente", True, BRANCO)

    tela.blit(texto1, (tela.get_width() // 2 - texto1.get_width() // 2, 150))
    tela.blit(texto2, (tela.get_width() // 2 - texto2.get_width() // 2, 220))

    botao = pygame.Rect(300, 300, 200, 60)
    pygame.draw.rect(tela, (200, 50, 50), botao, border_radius=15)
    tela.blit(texto3, (botao.x + (botao.width - texto3.get_width()) // 2, botao.y + 15))

    return botao

