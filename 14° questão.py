#Escreva um programa que encontre os números primos é uma tarefa
#difícil. Faça um programa que gera uma lista dos números primos
#existentes entre 1 e um número inteiro informado pelo usuário.


def is_prime(num):
    """Verifica se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_list(limit):
    """Gera uma lista de números primos até o limite informado."""
    prime_list = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

try:
    user_input = int(input("Digite um número inteiro: "))
    prime_numbers = generate_prime_list(user_input)
    print(f"Números primos até {user_input}: {prime_numbers}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")