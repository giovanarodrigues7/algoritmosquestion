#Escreva um programa que leia o índice pluviométrico de cada dia do mês de
#junho e informe o dia que mais choveu, o dia que menos choveu e as médias
#pluviométricas de cada uma das duas quinzenas.


# Inicializa uma lista para armazenar os índices pluviométricos de junho
indices_pluviometricos = []

# Solicita os índices pluviométricos para cada dia do mês
for dia in range(1, 31):
    indice = float(input(f"Digite o índice pluviométrico do dia {dia} de junho: "))
    indices_pluviometricos.append(indice)

# Calcula o dia que mais choveu e o dia que menos choveu
dia_maximo = indices_pluviometricos.index(max(indices_pluviometricos)) + 1
dia_minimo = indices_pluviometricos.index(min(indices_pluviometricos)) + 1

# Calcula as médias das duas quinzenas
media_primeira_quinzena = sum(indices_pluviometricos[:15]) / 15
media_segunda_quinzena = sum(indices_pluviometricos[15:]) / 15

# Exibe os resultados
print(f"Dia que mais choveu: {dia_maximo} de junho")
print(f"Dia que menos choveu: {dia_minimo} de junho")
print(f"Média da primeira quinzena: {media_primeira_quinzena:.2f}")
print(f"Média da segunda quinzena: {media_segunda_quinzena:.2f}")