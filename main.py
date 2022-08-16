nome_completo = input("Digite o seu nome completo:")
print(f"Ola {nome_completo}")

nome_completo = nome_completo.upper()
print(f"Seu nome completo maisculo é: {nome_completo}")

nome_completo = nome_completo.lower()
print(f"Seu nome completo minusculo é: {nome_completo}")

print(f"O tamanho do seu nome completo é: {len(nome_completo)}")

nome_splitado = nome_completo.split()
print(f"Seu nome completo separado é: {nome_splitado}")

# ha resolver
f = nome_splitado
print(f[1])

# join elements of text with space
print(f"Seu nome completo sem espaco tem o tamanho de: {len(''.join(nome_splitado))}")