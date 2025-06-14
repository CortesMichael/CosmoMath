from random_word import RandomWords

r = RandomWords()

def palavra_aleatoria():
    palavra = r.get_random_word()
    return palavra if palavra else "space"  # fallback
