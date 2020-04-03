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
