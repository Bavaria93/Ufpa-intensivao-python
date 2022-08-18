# Exercicio 1
# for i in range(11):
#     print(i)

# Exercicio 1
contador = 0
total =0
for i in range(0, 100):
    if contador < 10:
        if i % 2 != 0 and i > 5:
            total += i
            contador += 1
            print(i, contador)