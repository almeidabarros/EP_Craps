# Jogo Craps
# Nomes: Ana Barros e Luana Abramoff
# Data: 2/4/2020
# Interpretação do jogo: O jogador começa sempre pela fase Come Out. Nessa fase, ele tem quatro opções de tipo de aposta (Pass Line Bet, Field, Any Craps e Twelve), sendo 
# que cada uma desses tipo de aposta tem suas regras. Se o jogador escolhe a Pass Line Bet, exite um conjunto de resultado dos dados que o leva automaticamente para uma fase
# Point especial, que está diretamente conectada com o resultado dos dados da fase anterior (Come Out). Se na Come Out o jogador escolher qualquer outro tipo de aposta (Field, Any Craps ou Twelve)
# ou nao entrar na condiçao específica da Pass Line Bet, ele segue para a fase Point normal, onde tem tres tipos de aposta disponível (Field, Any Craps e Twelve)

import random 

simounao = True
quantidadeinicial = 100

while simounao and quantidadeinicial != 0:
    pointnormal=True
    simounao = input("Você quer apostar ou sair? ")
    if simounao == "sair":
        simounao = False
        break 
    print("Fase: Come Out")
    print("Opções: Pass Line Bet, Field, Any Craps, Twelve")
    aposta_comeout = input("Qual tipo de aposta você deseja fazer? ")
    valordaaposta = int(input("Quanto você deseja apostar? "))
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    somapoint = dado1 + dado2
    print("A soma dos dados foi {0}".format(somapoint))
    if aposta_comeout == "Pass Line Bet":
        if somapoint == 7 or somapoint ==11:
            quantidadeinicial += valordaaposta
            print("Você ganhou!")
            print("A quantidade de fichas é {0}".format(quantidadeinicial))
        elif somapoint == 2 or somapoint == 3 or somapoint == 12:
            quantidadeinicial -= valordaaposta
            print("Você perdeu")
            print("A quantidade de fichas é {0}".format(quantidadeinicial))
        else:
            print("Você foi para a fase Point.")
            pointnormal=False
            dado3 = random.randint(1,6)
            dado4 = random.randint(1,6)
            soma = dado3 + dado4
            while soma!=7 and soma!=somapoint:
                dado3 = random.randint(1,6)
                dado4 = random.randint(1,6)
                soma = dado3 + dado4
                print("A nova soma foi {0}.".format(soma))
            if soma == 7:
                quantidadeinicial = 0
                print("Você perdeu")
                break
            elif soma == somapoint:
                quantidadeinicial += valordaaposta
                print("Você ganhou!")
                print("A quantidade de fichas é {0}".format(quantidadeinicial))    

