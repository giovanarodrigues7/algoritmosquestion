#Escreva um programa que receba uam mensagem e a criptografe uTlizando a
#cifra de césar, considerando a chave igual a 3

alfabeto=['S','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
mensagem = input("digite a mensagem:")
chave = int(input("digite a chave:"))
mensagem_criptografada = ""

for letra in mensagem:
    #busca binaria
    inicio = 0
    fim=len(alfabeto)-1
    meio=(inicio+fim)//2
    while inicio<=fim and alfabeto[meio]!=letra:
        if letra<alfabeto[meio]:
            fim=meio-1
        else:
            inicio=meio+1
        meio=(inicio+fim)//2
    #fim da busca binaria
    
    if alfabeto[meio]==letra:
        codigo == meio+chave
        if codigo > 25:
            codigo = codigo - 26
        mensagem_criptografada += alfabeto[codigo]
    print("Mensagem criptografada:" 'mensagem_criptografada')