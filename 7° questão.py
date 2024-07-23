#Escreva um programa em python que leia um lista de 20 inteiros, calcule e
#imprima:
#a. A moda dos elementos na lista (elemento mais freqüente).
#b. A mediana dos elementos no array (elemento central)
#c. A média.



# Solicita os 20 inteiros
lista = []
for _ in range(20):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

# Calcula a média
media = sum(lista) / len(lista)

# Calcula a moda (elemento mais frequente)
frequencias = {}
for elemento in lista:
    if elemento in frequencias:
        frequencias[elemento] += 1
    else:
        frequencias[elemento] = 1

moda = max(frequencias, key=frequencias.get)

# Ordena a lista para calcular a mediana
lista.sort()
tamanho = len(lista)
if tamanho % 2 == 0:
    mediana = (lista[tamanho // 2 - 1] + lista[tamanho // 2]) / 2
else:
    mediana = lista[tamanho // 2]

# Exibe os resultados
print(f"Média: {media:.2f}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")