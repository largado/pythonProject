import random

print("seja bem vindo!")

numero = round(random.random() * 100)
tentativas = 3
tentativaimpressa = 1


while(tentativas > 0):
    print("Tentativa", tentativaimpressa, "de 3")
    numero2 = input("digite seu número: ")

    print("vc digitou", numero2)

    numerodigitado = int(numero2)

    maior = numero < numerodigitado
    menor = numero > numerodigitado
    acertou = numero == numerodigitado

    if (acertou):
        print(" acertou")
        break
    else:
        if (menor):
            print("ERRADO! o número que vc digitou é menor!")
        elif(maior):
            print("ERRADO! o número que vc digitou é maior!!")

    tentativas = tentativas -1
    tentativaimpressa = tentativaimpressa + 1

print(" fim do jogo")
