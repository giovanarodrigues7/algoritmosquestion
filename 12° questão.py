#Um banco concederá um crédito especial aos seus clientes, variável
#com o saldo médio no último ano. Faça um algoritmo que leia o saldo
#médio de um cliente e calcule o valor do crédito de acordo com a tabela
#abaixo. Mostre uma mensagem informando o saldo médio e o valor do
#crédito.

#Saldo médio Percentual
#de 0 a 200 nenhum crédito
#de 201 a 400 20% do valor do saldo médio
#de 401 a 600 30% do valor do saldo médio
#acima de 601 40% do valor do saldo médio



# Solicita o saldo médio do cliente
saldo_medio = float(input("Digite o saldo médio do cliente: "))

# Calcula o valor do crédito de acordo com a tabela
if saldo_medio >= 0 and saldo_medio <= 200:
    valor_credito = 0
elif saldo_medio <= 400:
    valor_credito = saldo_medio * 0.20
elif saldo_medio <= 600:
    valor_credito = saldo_medio * 0.30
else:
    valor_credito = saldo_medio * 0.40

# Exibe o resultado
print(f"Saldo médio: R${saldo_medio:.2f}")
print(f"Valor do crédito: R${valor_credito:.2f}")