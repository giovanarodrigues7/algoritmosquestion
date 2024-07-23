#Escreva um programa que cria uma lista de duas dicmensões uTlizando List
#Comprehsion e imprima a diagonal principal desta lista


# Criação da matriz 3x3 utilizando List Comprehension
matriz = [[i + j for i in range(3)] for j in range(3)]

# Imprime a matriz
for linha in matriz:
    print(linha)

# Imprime a diagonal principal
print("Diagonal principal:")
for i in range(3):
    print(matriz[i][i])