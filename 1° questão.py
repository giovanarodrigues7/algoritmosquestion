##Faça um programa que calcule o fatorial de todos os numeros impares dentre os 10 primeiros da sequência de Fibonacci.

# Função para gerar a sequência de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Função para calcular o fatorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# Gerar os 10 primeiros números da sequência de Fibonacci
fib_sequence = fibonacci(10)

# Filtrar os números ímpares e calcular o fatorial
odd_factorials = {num: factorial(num) for num in fib_sequence if num % 2 != 0}

# Exibir os resultados
for num, fact in odd_factorials.items():
    print(f"Fatorial de {num} é {fact}")