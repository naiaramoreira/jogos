import forca
import adivinhacao

def escolhe_jogo():
    print('*********************************')
    print("*********Escolha o jogo!*********")
    print('*********************************')

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()