from datetime import date

data_atual = date.today()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

print(type(dia_atual))

inicio_aulas = input("Digite o inicio das aulas")
inicio_aulas = inicio_aulas.split("/")
#print(inicio_aulas)
inicio_aulas_dia = int(inicio_aulas[0])
inicio_aulas_mes = int(inicio_aulas[1])
inicio_aulas_ano = int(inicio_aulas[2])

#print(inicio_aulas_dia)
dias_faltando = inicio_aulas_dia - dia_atual
print(f"Faltam {dias_faltando} para o inicio das aulas")