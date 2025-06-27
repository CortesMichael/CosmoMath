import pygame
import sys
import random

pygame.init()

# Carrega o ícone (coloque seu arquivo na mesma pasta ou especifique o caminho)
try:
    icon = pygame.image.load('assets/imagens/icon.png')  # Pode ser .png, .jpg, .ico, .bmp
except:
    print("Erro ao carregar o ícone, usando padrão")
    # Cria um ícone simples como fallback
    icon = pygame.Surface((32, 32))
    icon.fill((255, 0, 255))  # Ícone magenta quadrado como fallback

# Coração do jogo
try:
    coracao_img = pygame.image.load("assets/imagens/heart.png")
    coracao_img = pygame.transform.scale(coracao_img, (40, 40))  # redimensiona
except:
    print("Erro ao carregar imagem do coração. Usando fallback.")
    coracao_img = pygame.Surface((30, 30))
    coracao_img.fill((255, 0, 0))  # fallback vermelho quadrado



# Define o ícone ANTES de criar a janela
pygame.display.set_icon(icon)


# Tela
LARGURA, ALTURA = 700, 900
TELA = pygame.display.set_mode((LARGURA, ALTURA))


from nave import Nave
from tiro import Tiro
from numero import Numero
from utils import gerar_conta, gerar_opcoes_com_resposta


pygame.display.set_caption("CosmoMath")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Fonte
try:
    FONTE = pygame.font.Font("assets/press-start-2p-font/PressStart2P.ttf", 20)
    # Ou se estiver em uma subpasta:
    # font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 20)
except:
    print("Erro ao carregar a fonte, usando fallback")
    FONTE = pygame.font.SysFont("Arial", 20)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Assets
nave_img = pygame.Surface((60, 60))
nave_img.fill((0, 100, 255))  # Use imagem real aqui se quiser

# Estados
TELA_INICIAL, JOGO, GAME_OVER = "inicio", "jogo", "fim"
estado = TELA_INICIAL

# Geração de contas e números
def gerar_conta(fase):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    if fase == 1:
        op = "+"
        resultado = a + b
    else:
        op = "-"
        resultado = a - b if a >= b else b - a
        a, b = max(a, b), min(a, b)
    conta = f"{a} {op} {b} ?"
    opcoes = [resultado, resultado + 1, resultado - 1]
    random.shuffle(opcoes)
    return conta, resultado, opcoes

# carregar imagem da logo
try:
    logo_img = pygame.image.load("assets/imagens/logoCosmo.png")
    logo_img = pygame.transform.scale(logo_img, (380, 65))  # Redimensiona se necessário
except:
    print("Erro ao carregar a logo, usando fallback")
    logo_img = pygame.Surface((300, 150))
    logo_img.fill((100, 100, 255))  # Um retângulo azul como substituto


# Tela Inicial
def tela_inicial():
    clock = pygame.time.Clock()

    # Posições e dimensões
    logo_y = 200
    y_botao = 450
    largura_botao = 200
    altura_botao = 60
    x_botao = LARGURA // 2 - largura_botao // 2
    botao_rect = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

    # Texto do botão
    texto_start = FONTE.render("START", True, PRETO)
    texto_temp = texto_start.copy()
    logo_temp = logo_img.copy()

    # Geração de estrelas
    estrelas = [(random.randint(0, LARGURA), random.randint(0, ALTURA)) for _ in range(60)]

    # Fade-in inicial
    alpha = 0
    while alpha < 255:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        TELA.fill(PRETO)

        # Estrelas
        for estrela in estrelas:
            pygame.draw.circle(TELA, (255, 255, 255), estrela, 2)

        logo_temp.set_alpha(alpha)
        texto_temp.set_alpha(alpha)

        # Logo
        TELA.blit(logo_temp, (LARGURA // 2 - logo_img.get_width() // 2, logo_y))

        # Botão com sombra e alpha
        sombra_rect = botao_rect.copy()
        sombra_rect.y += 4
        pygame.draw.rect(TELA, (0, 100, 0), sombra_rect, border_radius=20)

        botao_surface = pygame.Surface((largura_botao, altura_botao), pygame.SRCALPHA)
        pygame.draw.rect(botao_surface, (0, 200, 0, alpha), botao_surface.get_rect(), border_radius=20)
        TELA.blit(botao_surface, (x_botao, y_botao))

        TELA.blit(texto_temp, (
            x_botao + largura_botao // 2 - texto_start.get_width() // 2,
            y_botao + altura_botao // 2 - texto_start.get_height() // 2
        ))

        pygame.display.update()
        alpha += 5

    # Loop após o fade
    while True:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    return botao_rect

        # Animação leve nas estrelas
        for i in range(len(estrelas)):
            x, y = estrelas[i]
            y += 0.5
            if y > ALTURA:
                y = 0
                x = random.randint(0, LARGURA)
            estrelas[i] = (x, y)

        TELA.fill(PRETO)

        # Estrelas em movimento
        for estrela in estrelas:
            pygame.draw.circle(TELA, (255, 255, 255), (int(estrela[0]), int(estrela[1])), 2)

        # Logo
        TELA.blit(logo_img, (LARGURA // 2 - logo_img.get_width() // 2, logo_y))

        # Botão com sombra e hover
        mouse_pos = pygame.mouse.get_pos()
        cor_botao = (0, 255, 100) if botao_rect.collidepoint(mouse_pos) else (0, 200, 0)

        sombra_rect = botao_rect.copy()
        sombra_rect.y += 4
        pygame.draw.rect(TELA, (0, 100, 0), sombra_rect, border_radius=20)

        pygame.draw.rect(TELA, cor_botao, botao_rect, border_radius=20)

        TELA.blit(texto_start, (
            x_botao + largura_botao // 2 - texto_start.get_width() // 2,
            y_botao + altura_botao // 2 - texto_start.get_height() // 2
        ))

        pygame.display.update()


# Tela Final
def tela_final(pontos):
    clock = pygame.time.Clock()
    estrelas = [(random.randint(0, LARGURA), random.randint(0, ALTURA)) for _ in range(60)]

    # Textos
    texto_fim = FONTE.render("MISSÃO ENCERRADA", True, (255, 80, 80))
    texto_pontos = FONTE.render(f"Pontos: {pontos}", True, (255, 255, 255))
    texto_restart = FONTE.render("REINICIAR", True, PRETO)
    texto_sair = FONTE.render("SAIR", True, PRETO)

    # Botões
    largura_botao = 300
    altura_botao = 60
    espaco = 40
    x_botao = LARGURA // 2 - largura_botao // 2
    botao_restart = pygame.Rect(x_botao, 360, largura_botao, altura_botao)
    botao_sair = pygame.Rect(x_botao, 360 + altura_botao + espaco, largura_botao, altura_botao)

    while True:
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_restart.collidepoint(evento.pos):
                    global estado
                    estado = "inicio"
                    return
                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        # Atualizar posições das estrelas (descendo)
        for i in range(len(estrelas)):
            x, y = estrelas[i]
            y += 0.5
            if y > ALTURA:
                y = 0
                x = random.randint(0, LARGURA)
            estrelas[i] = (x, y)

        TELA.fill(PRETO)

        # Estrelas em movimento
        for estrela in estrelas:
            pygame.draw.circle(TELA, (255, 255, 255), (int(estrela[0]), int(estrela[1])), 2)

        # Títulos
        TELA.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, 180))
        TELA.blit(texto_pontos, (LARGURA // 2 - texto_pontos.get_width() // 2, 240))

        # Hover
        mouse_pos = pygame.mouse.get_pos()
        hover_restart = botao_restart.collidepoint(mouse_pos)
        hover_sair = botao_sair.collidepoint(mouse_pos)

        cor_restart = (0, 255, 100) if hover_restart else (0, 200, 0)
        cor_sair = (255, 100, 100) if hover_sair else (200, 0, 0)

        # Botão REINICIAR
        sombra_restart = botao_restart.copy()
        sombra_restart.y += 4
        pygame.draw.rect(TELA, (0, 100, 0), sombra_restart, border_radius=20)

        botao_surface_restart = pygame.Surface((largura_botao, altura_botao), pygame.SRCALPHA)
        pygame.draw.rect(botao_surface_restart, cor_restart, botao_surface_restart.get_rect(), border_radius=20)
        TELA.blit(botao_surface_restart, (x_botao, botao_restart.y))

        TELA.blit(texto_restart, (
            botao_restart.centerx - texto_restart.get_width() // 2,
            botao_restart.centery - texto_restart.get_height() // 2
        ))

        # Botão SAIR
        sombra_sair = botao_sair.copy()
        sombra_sair.y += 4
        pygame.draw.rect(TELA, (100, 0, 0), sombra_sair, border_radius=20)

        botao_surface_sair = pygame.Surface((largura_botao, altura_botao), pygame.SRCALPHA)
        pygame.draw.rect(botao_surface_sair, cor_sair, botao_surface_sair.get_rect(), border_radius=20)
        TELA.blit(botao_surface_sair, (x_botao, botao_sair.y))

        TELA.blit(texto_sair, (
            botao_sair.centerx - texto_sair.get_width() // 2,
            botao_sair.centery - texto_sair.get_height() // 2
        ))

        pygame.display.update()


def gerar_opcoes_com_resposta(correta):
    opcoes = [correta]
    while len(opcoes) < 5:
        n = random.randint(correta - 3, correta + 3)
        if n != correta and n not in opcoes:
            opcoes.append(n)
    random.shuffle(opcoes)
    return opcoes


# Lógica principal
def jogo():
    global estado
    estrelas_fundo = [(random.randint(0, LARGURA), random.randint(0, ALTURA)) for _ in range(80)]
    nave = Nave()
    tiros = []
    numeros = []
    fase = 1
    tempo_entre_numeros = 60  # 60 frames = 1 segundo entre cada número
    tempo_ultimo_numero = 0


    conta, resultado_certo, _ = gerar_conta(fase)
    grupo_opcoes = gerar_opcoes_com_resposta(resultado_certo)
    posicoes_x = random.sample([100, 200, 300, 400, 500], k=5)

    contador = 0
    tempo_entre_numeros = 60  # a cada 1 segundo (60 FPS)
    indice_numero = 0

    while True:
        clock.tick(FPS)
        TELA.fill(PRETO)

        for estrela in estrelas_fundo:
            pygame.draw.circle(TELA, (255, 255, 255), estrela, 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(Tiro(nave.rect.centerx, nave.rect.top))

        keys = pygame.key.get_pressed()
        nave.mover(keys)


        # ---------- CAIXA AZUL DA CONTA COM ESTILO ----------
        caixa_largura = 200
        caixa_altura = 40
        caixa_x = LARGURA // 2 - caixa_largura // 2
        caixa_y = 45

        # Gradiente vertical bonito (de cima pra baixo)
        caixa_surface = pygame.Surface((caixa_largura, caixa_altura))

        for y in range(caixa_altura):
            # Interpola do azul claro (ex: 100,150,255) para azul escuro (0,60,160)
            r = int(0 + (100 - 0) * (y / caixa_altura))
            g = int(60 + (150 - 60) * (y / caixa_altura))
            b = int(160 + (255 - 160) * (y / caixa_altura))
            pygame.draw.line(caixa_surface, (r, g, b), (0, y), (caixa_largura, y))

        caixa_surface = caixa_surface.convert()
        caixa_surface.set_colorkey((0, 0, 0))  # Se precisar usar transparência

        # Arredondar a borda aplicando uma máscara com border_radius
        bordas = pygame.Surface((caixa_largura, caixa_altura), pygame.SRCALPHA)
        pygame.draw.rect(bordas, (255, 255, 255), bordas.get_rect(), border_radius=20)
        caixa_surface.blit(bordas, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

        TELA.blit(caixa_surface, (caixa_x, caixa_y))

        # Texto centralizado
        conta_texto = FONTE.render(conta, True, BRANCO)
        conta_x = LARGURA // 2 - conta_texto.get_width() // 2
        conta_y = caixa_y + caixa_altura // 2 - conta_texto.get_height() // 2
        TELA.blit(conta_texto, (conta_x, conta_y))


        # Gerar número a cada tempo
        if indice_numero < 5 and contador - tempo_ultimo_numero >= tempo_entre_numeros:
            valor = grupo_opcoes[indice_numero]
            x = posicoes_x[indice_numero]
            y_inicial = 90  # nasce abaixo da caixa da conta
            numeros.append(Numero(valor, x, y_inicial))
            indice_numero += 1
            tempo_ultimo_numero = contador


        # Quando todos já caíram e a lista está vazia, iniciar nova rodada
        if indice_numero == 5 and len(numeros) == 0:
            fase += 1 if fase == 1 else 0  # avança só até fase 2
            conta, resultado_certo, _ = gerar_conta(fase)
            grupo_opcoes = gerar_opcoes_com_resposta(resultado_certo)
            posicoes_x = random.sample([100, 200, 300, 400, 500], k=5)
            indice_numero = 0

        for tiro in tiros[:]:
            tiro.mover()
            tiro.desenhar()
            if tiro.rect.bottom < 0:
                tiros.remove(tiro)

        for num in numeros[:]:
            num.mover()
            num.desenhar()

            # Colisão com a nave
            if num.rect.colliderect(nave.rect):
                nave.vidas -= 1
                numeros.remove(num)

            # Saiu da tela
            elif num.rect.top > ALTURA:
                if num.valor == resultado_certo:
                    nave.vidas -= 1  # perdeu por deixar passar a resposta certa
                numeros.remove(num)

            for tiro in tiros[:]:  # percorre cópia da lista
                if num.rect.colliderect(tiro.rect):
                    tiros.remove(tiro)  # remove o tiro após a colisão

                    if num.valor == resultado_certo:
                        nave.pontos += 1
                    else:
                        nave.vidas -= 1

                    numeros.remove(num)  # remove o número também
                    break  # para não comparar com outros tiros


        nave.desenhar()

        # Coordenadas do coração no canto superior direito
        coracao_x = LARGURA - 100
        coracao_y = 17

        # Desenha o coração
        TELA.blit(coracao_img, (coracao_x, coracao_y))

        ## Texto de vidas no canto superior direito
        vidas_texto = FONTE.render(f"{nave.vidas}", True, BRANCO)

        # Coordenadas ajustadas para o canto direito
        vidas_x = LARGURA - vidas_texto.get_width() - 30  # 20 de margem da borda direita
        vidas_y = 28  # altura no topo, igual à caixa da conta

        TELA.blit(vidas_texto, (vidas_x, vidas_y))

        if nave.vidas <= 0:
            estado = GAME_OVER
            return

        pygame.display.update()
        contador += 1


# Loop Principal
while True:
    if estado == TELA_INICIAL:
        tela_inicial()  # Ela já desenha e trata o clique
        estado = JOGO   # Após clicar no botão, voltamos pra cá e iniciamos o jogo

    elif estado == JOGO:
        jogo()
    elif estado == GAME_OVER:
        tela_final(pontos=0)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    estado = TELA_INICIAL
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
