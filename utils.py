import random

def gerar_conta(fase):
    if fase == 1:
        a = random.randint(15, 100)
        b = random.randint(15, 100)
        op = "+"
        resultado = a + b

    elif fase == 2:
        a = random.randint(13, 100)
        b = random.randint(13, 100)
        op = "-"
        resultado = a - b if a >= b else b - a
        a, b = max(a, b), min(a, b)

    else:
        a = random.randint(2, 9 + fase // 2)  # cresce com o tempo
        b = random.randint(2, 9 + fase // 2)
        op = "x"
        resultado = a * b

    conta = f"{a} {op} {b} ?"
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
