import random

def jogar():


    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Regras de pontuação:")
    print("Você começa com 1000 pontos.")
    print("A cada tentativa errada perde pontos")
    print("com base na distância do número secreto de seu chute.")

    print("Qual nível de dificuldade?")
    print("(1)  Fácil  -> 10 tentativas")
    print("(2)  Médio  ->  7 tentativas")
    print("(3) Difícil ->  5 tentativas")
    print("*********************************")
    nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 7
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        print("Informe uma dificuldade.")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Informe um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Acertou! Sua pontuação é {}".format(pontos))
            break
        else:
            if(maior):
                print("Errou! O número informado é maior do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
                if(rodada == total_de_tentativas):
                    print("O número secreto era", numero_secreto)
            elif(menor):
                print("Errou! O número informado é menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
                if(rodada == total_de_tentativas):
                    print("O número secreto era", numero_secreto)

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()