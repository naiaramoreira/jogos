import random

def jogar():
    print('*********************************')
    print("Bem vindo ao jogo de Adivinhação!")
    print('*********************************')

    #numero_secreto = round(random.random() * 100) # 0.0 - 1.0
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while rodada <= total_de_tentativas:
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {}!".format(rodada, total_de_tentativas))
        chute = input("Digite seu número entre 1 e 100: ")

        chute   = int(chute)
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        # total_de_tentativas -= total_de_tentativas
        # rodada = rodada + 1

    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()
