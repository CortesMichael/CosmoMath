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

# Define o ícone ANTES de criar a janela
pygame.display.set_icon(icon)


# Tela
LARGURA, ALTURA = 700, 900
TELA = pygame.display.set_mode((LARGURA, ALTURA))
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

# Classe Nave
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

# Classe Tiro
class Tiro:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 15)

    def mover(self):
        self.rect.y -= 10

    def desenhar(self):
        pygame.draw.rect(TELA, VERMELHO, self.rect)

# Classe Numero
class Numero:
    def __init__(self, valor, x, y):
        self.valor = valor
        self.rect = pygame.Rect(x, y, 50, 50)
        self.acertado = False

    def mover(self):
        self.rect.y += 1  # velocidade reduzida

    def desenhar(self):
        pygame.draw.rect(TELA, BRANCO, self.rect)
        texto = FONTE.render(str(self.valor), True, PRETO)
        TELA.blit(texto, (self.rect.x + 10, self.rect.y + 10))

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
    conta = f"{a} {op} {b}"
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
    TELA.fill(PRETO)

    # Posições
    logo_y = 200
    y_botao = 450
    largura_botao = 200
    altura_botao = 60
    x_botao = LARGURA // 2 - largura_botao // 2
    botao_rect = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

    # Carrega texto e superfícies
    texto_start = FONTE.render("START", True, PRETO)
    logo_temp = logo_img.copy()
    texto_temp = texto_start.copy()

    # Fade-in apenas uma vez
    alpha = 0
    while alpha < 255:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        TELA.fill(PRETO)

        logo_temp.set_alpha(alpha)
        texto_temp.set_alpha(alpha)

        # Exibe logo com alpha
        TELA.blit(logo_temp, (LARGURA//2 - logo_img.get_width()//2, logo_y))

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

    # Depois do fade, mantém tela fixa com logo e botão completos
    while True:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    return botao_rect

        mouse_pos = pygame.mouse.get_pos()
        mouse_hover = botao_rect.collidepoint(mouse_pos)
        cor_botao = (0, 255, 100) if mouse_hover else (0, 200, 0)

        TELA.fill(PRETO)

        # Logo fixa
        TELA.blit(logo_img, (LARGURA//2 - logo_img.get_width()//2, logo_y))

        # Sombra e botão normal
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
    TELA.fill(PRETO)
    fim = FONTE.render(f"Fim de Jogo - Pontuação: {pontos}", True, BRANCO)
    botao = FONTE.render("R para reiniciar ou ESC para sair", True, BRANCO)
    TELA.blit(fim, (LARGURA//2 - fim.get_width()//2, 200))
    TELA.blit(botao, (LARGURA//2 - botao.get_width()//2, 300))
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

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(Tiro(nave.rect.centerx, nave.rect.top))

        keys = pygame.key.get_pressed()
        nave.mover(keys)

        # Mostrar conta
        conta_texto = FONTE.render(conta, True, BRANCO)
        TELA.blit(conta_texto, (LARGURA//2 - conta_texto.get_width()//2, 20))

        # Gerar número a cada tempo
        if indice_numero < 5 and contador - tempo_ultimo_numero >= tempo_entre_numeros:
            valor = grupo_opcoes[indice_numero]
            x = posicoes_x[indice_numero]
            numeros.append(Numero(valor, x, 0))
            indice_numero += 1
            tempo_ultimo_numero = contador  # marca o tempo em que esse caiu


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

            for tiro in tiros:
                if num.rect.colliderect(tiro.rect):
                    if num.valor == resultado_certo:
                        nave.pontos += 1
                        numeros.remove(num)
                        break
                    else:
                        nave.vidas -= 1
                        numeros.remove(num)
                        break

        nave.desenhar()

        # Vidas
        vidas_texto = FONTE.render(f"Vidas: {nave.vidas}", True, BRANCO)
        TELA.blit(vidas_texto, (10, 10))

        # Fim do jogo
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
