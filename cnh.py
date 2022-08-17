idade = int(input("Digite sua idade: "))
sim = 1
nao = 2
cnh = int(input("Você possui CNH: "))
print(cnh)
if idade < 18 or idade >= 18 and cnh == nao:
    print("Vai pra casa")
else:
    if idade >= 18 and cnh == sim:
        print("Você pode se inscrever no curso")