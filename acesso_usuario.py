usuario = input("Nome do Usuario: ")
senha = input("Senha do Usuario: ")

usuario_bd = "Raphael Câmara"
senha_bd = "12345678"

if usuario == usuario_bd and senha == senha_bd:
    print("Acesso autorizado")
elif usuario != usuario_bd and senha != senha_bd:
    print("Acesso negado")