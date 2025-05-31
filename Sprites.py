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

def desenhar_menu(tela):
    fonte = pygame.font.SysFont("Comic-sans", 40, bold=True)
    tela.fill(PRETO)

    # titulo
    titulo = fonte.render("CosmoMath", True, BRANCO)
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
