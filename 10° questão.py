#calcular o IMC de uma pessoa e imprima a sua condiçao

peso = int(input("digite o seu peso"))
altura = float(input("digite a sua altura"))

IMC = (peso/altura **2 )

if IMC < 18.5:
    print("Abaixo do peso")
if IMC > 18.6 and IMC < 25.0:
    print("Peso ideal, parabéns")
if IMC > 25.0 and IMC < 29.9:
    print("Levemente acima do peso")
if IMC > 30.0 and IMC < 34.9:
    print("Obesidade grau I")
if IMC > 35.0 and IMC < 39.9:
    print("Obesidade grau II (severa)")
if IMC > 40:
    print("Obesidade grau III (mórbida)")
