#A locadora de carros precisa da sua ajuda para cobrar seus serviços.
#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e
#R$0,20 por Km rodado.


def calcular_preco_aluguel(km_percorridos, dias_aluguel):
    preco_por_dia = 90
    preco_por_km = 0.20

    custo_dias = preco_por_dia * dias_aluguel
    custo_km = preco_por_km * km_percorridos

    preco_total = custo_dias + custo_km
    return preco_total

try:
    km_percorridos = float(input("Quantos quilômetros foram percorridos? "))
    dias_aluguel = int(input("Por quantos dias o carro foi alugado? "))

    preco_total = calcular_preco_aluguel(km_percorridos, dias_aluguel)
    print(f"Preço total a pagar: R$ {preco_total:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")