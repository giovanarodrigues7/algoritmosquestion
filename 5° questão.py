#5) Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3%
#ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de
#2% ao ano, escreva um programa, que imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.

A = 5000000
B = 7000000
anos = 0

porcA = A % 3
porcB = B % 2

while A < B:
    anos += anos + 1
    A = A - porcA
    B = B - porcA
    

print("demorou",anos,", o país A tem",A,"habitantes, e o país B tem", B,"de habitantes")