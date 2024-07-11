#calcular o IMC de uma pessoa e imprima a sua condiçao

peso = float(input("digite o seu peso"))
altura = float(input("digite a sua altura"))

IMC = [peso/(altura)**2]

if IMC <= 18.5:
    print("Abaixo do peso")



