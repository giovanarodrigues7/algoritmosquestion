#Crie um programa que idenTfique se uma palavra é um palíndromo

def verificar_palavra(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False
resultado = verificar_palavra(str(input("digite a palavra")))
print(resultado)
