from random import randint

sorteio = int(randint(1, 100))

while True:
    numero = int(input("Digite um numero: "))
    if numero > sorteio:
        print("O número que voce digitou é maior que o soteado")
    elif numero < sorteio:
        print("O número que voce digitou é menor que o soteado")
    elif numero == sorteio:
        print("Voce acetou, parabens!")
        break