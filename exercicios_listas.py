# lista = ["1", "2", "3", "4", "5"]
# for i in lista:
#     print(i)

# nota = [7.0, 7.5, 9.0, 8.5, 6.0, 6.9]
# soma = 0
# for i in nota:
#     soma = soma + i
#
# media = soma / len(nota)
# print(media)

total_altura = 0
total_maior_que_13 = 0
total_abaixo_da_media = 0

idade_alturas = [
    {
        "idade": 15,
        "altura": 1.72
    },
    {
        "idade": 14,
        "altura": 1.68
    },
    {
        "idade": 17,
        "altura": 1.76
    }
]

for item in idade_alturas:
    if item["idade"] > 13:
        total_maior_que_13 == 1

    total_altura = item["altura"]

media = total_altura / len(idade_alturas)

for item in idade_alturas:
    if item["idade"] > 13 and item["altura"]