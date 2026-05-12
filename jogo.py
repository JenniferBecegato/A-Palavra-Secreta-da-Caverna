import random

PALAVRAS = [
    "CORDA", "COBRA", "PEDRA", "FORCA", "MAGIA",
    "TORCA", "BRIGA", "CHAMA", "FUSCA", "BRISA",
    "TROCA", "FLOCO", "GRADE", "GRUTA", "LUNAR",
    "MANTO", "NOBRE", "OCASO", "PRATA", "QUOTA",
    "RAIVA", "SABRE", "TARDE", "ULTRA", "VAPOR",
    "XEROX", "ZUMBI", "ABRIR", "BURRO", "CHUVA",
]

TENTATIVAS_MAX = 6


def comparar(secreta, tentativa):
    """Compara a tentativa com a palavra secreta e retorna os indicadores.

    Retorna uma lista de strings no formato 'LETRA[C]', 'LETRA[P]' ou 'LETRA[X]'.

    [C] – A letra está na palavra e na posição correta.
    [P] – A letra está na palavra, mas em posição errada.
    [X] – A letra não existe na palavra secreta.
    """
    resultado = []
    secreta_lista = list(secreta)
    tentativa_lista = list(tentativa)
    marcadores = [None] * len(tentativa)

    # Primeira passagem: marcar acertos exatos [C]
    for i in range(len(tentativa)):
        if tentativa_lista[i] == secreta_lista[i]:
            marcadores[i] = "C"
            secreta_lista[i] = None  # consumir a letra da palavra secreta

    # Segunda passagem: marcar [P] ou [X]
    for i in range(len(tentativa)):
        if marcadores[i] is not None:
            continue
        if tentativa_lista[i] in secreta_lista:
            marcadores[i] = "P"
            secreta_lista[secreta_lista.index(tentativa_lista[i])] = None
        else:
            marcadores[i] = "X"

    for i, letra in enumerate(tentativa):
        resultado.append(f"{letra}[{marcadores[i]}]")

    return resultado


def jogar():
    palavra_secreta = random.choice(PALAVRAS)
    tamanho = len(palavra_secreta)

    print("=" * 40)
    print("  Bem-vindo a A Palavra Secreta da Caverna!")
    print("=" * 40)
    print(f"A palavra secreta tem {tamanho} letras.")
    print(f"Você tem {TENTATIVAS_MAX} tentativas.\n")
    print("Indicadores: [C] posição correta | [P] letra existe, posição errada | [X] letra não existe\n")

    for tentativa_num in range(1, TENTATIVAS_MAX + 1):
        while True:
            entrada = input(f"Tentativa {tentativa_num}/{TENTATIVAS_MAX}: ").strip().upper()
            if len(entrada) != tamanho:
                print(f"A palavra deve ter {tamanho} letras. Tente novamente.")
            else:
                break

        resultado = comparar(palavra_secreta, entrada)
        print(" ".join(resultado))
        print()

        if entrada == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra secreta: {palavra_secreta}")
            return

    print(f"Fim de jogo! A palavra secreta era: {palavra_secreta}")


if __name__ == "__main__":
    jogar()
