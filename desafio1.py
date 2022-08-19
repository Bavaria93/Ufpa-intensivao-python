import requests

res = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
print(res)
res_json = res.json()
#print(res_json)
cotacao_dolar = float(res_json["USDBRL"]["bid"])
print(cotacao_dolar)
cotacao_euro = float(res_json["EURBRL"]["bid"])
print(cotacao_euro)

valor_real = float(input("Quanto você tem em real: "))
dolar_usuario = valor_real / cotacao_dolar
euro_usuario = valor_real / cotacao_euro
print(f"Valor convertido em dolar é: {dolar_usuario:.4f}")
print(f"Valor convertido em euro é: {euro_usuario:.4f}")