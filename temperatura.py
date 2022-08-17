print("Define C para converter de Fairen para Celsius")
print("Define F para converter de Celsius para Fairen")

operacao = input("Sua escolha: ")

if operacao == "C":
    tempF = int(input("temperatura Fairen: "))
    tempC = (tempF - 32) * 5 / 9
    print(f"{tempC:.2f}")
if operacao == "F":
    tempC = int(input("temperatura Celsius: "))
    tempF = (tempC * 9 / 5) + 32
    print(f"{tempF:.2f}")