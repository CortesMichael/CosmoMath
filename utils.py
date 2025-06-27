import random

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

def gerar_opcoes_com_resposta(correta):
    opcoes = [correta]
    while len(opcoes) < 5:
        n = random.randint(correta - 3, correta + 3)
        if n != correta and n not in opcoes:
            opcoes.append(n)
    random.shuffle(opcoes)
    return opcoes
