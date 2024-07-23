#Em uma cerTficação são feitos são feitos 5 exames (I, II, III, IV e V). Escreva um
#programa que leia as notas destes exames e imprima a classificação do aluno,
#sabendo que a média é 7.0.
#Classificação: A – passou em todos os exames;
#B – passou em I, II e IV, mas não em III ou V;
#C – passou em I e II, III ou IV, mas não em V.
#Reprovado – outras situações



# Solicita as notas dos exames
nota_I = float(input("Digite a nota do exame I: "))
nota_II = float(input("Digite a nota do exame II: "))
nota_III = float(input("Digite a nota do exame III: "))
nota_IV = float(input("Digite a nota do exame IV: "))
nota_V = float(input("Digite a nota do exame V: "))

# Calcula a média das notas
media = (nota_I + nota_II + nota_III + nota_IV + nota_V) / 5

# Determina a classificação do aluno
if media == 7.0:
    print("Classificação: A - passou em todos os exames")
elif nota_I >= 7.0 and nota_II >= 7.0 and nota_IV >= 7.0:
    print("Classificação: B - passou em I, II e IV, mas não em III ou V")
elif (nota_I >= 7.0 and nota_II >= 7.0) or (nota_I >= 7.0 and nota_IV >= 7.0) or (nota_II >= 7.0 and nota_IV >= 7.0):
    print("Classificação: C - passou em I e II, III ou IV, mas não em V")
else:
    print("Classificação: Reprovado - outras situações")