valor_pedido = float(input("Qual o valor do pedido: "))
estado = str(input("Qual o estado: "))

imposto = 0.055 * valor_pedido
if estado == "PA":
    valor_total = valor_pedido + imposto
    print(f"O subtotal é de R${valor_pedido:.2f}")
    print(f"O imposto é de R${imposto:.2f}")
    print(f"O valor total é R${valor_total:.2f}")
else:
    print(f"O subtotal é de R${valor_pedido:.2f}")