#Escreva um progama que calcule o imposto de renda a parTr de um salário de 
#um funcionário a parTr de da tabela abaixo:
#Sálario IPRF

#Ate 1.500,00 5%
#Acima de 1500,00 até 3.000,00 8%
#Acima de 3.000,00 até 10.000,00 15%
#Acima de 15.000,00 27%

#O programa deverá ao fim imprimir o valor deo imposto devido, o saláriio bruto 
#e o salário com desconto. O programa ainda deverá se repeTr até que o 
#usuário deseje encerra-lo


def calcular_imposto(salario):
    if salario <= 1500:
        aliquota = 0.05
    elif salario <= 3000:
        aliquota = 0.08
    elif salario <= 10000:
        aliquota = 0.15
    else:
        aliquota = 0.27

    imposto_devido = salario * aliquota
    salario_com_desconto = salario - imposto_devido

    print(f"Salário bruto: R${salario:.2f}")
    print(f"Imposto devido: R${imposto_devido:.2f}")
    print(f"Salário com desconto: R${salario_com_desconto:.2f}")

while True:
    try:
        salario_funcionario = float(input("Digite o salário do funcionário: R$"))
        calcular_imposto(salario_funcionario)
        continuar = input("Deseja calcular para outro funcionário? (S/N): ").strip().lower()
        if continuar != 's':
            break
    except ValueError:
        print("Valor inválido. Digite um número válido.")