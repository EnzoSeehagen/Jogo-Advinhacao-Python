import random

print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = random.randrange(1, 26)
total_de_tentativas = 0
rodada = 1

print("Selecione o nível de dificuldade: ")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível de dificuldade: "))

if(nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 8
else:
    total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 á 25: ")
    chute = int(chute)
    print("Você digitou ", chute)

    if(chute < 1 or chute > 25):
        print("Você deve digitar um número entre 1 á 25")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número que eu pensei")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número que eu pensei ")

print("Fim do jogo")