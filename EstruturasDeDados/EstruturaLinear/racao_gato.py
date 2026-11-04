# Problema: Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos
# para os quais fornece a quantidade de ração em gramas. Faça um programa que receba
# o peso do saco de ração e a quantidade de ração fornecida para cada gato.
# Calcule e mostre quanto restará de ração no saco após cinco dias.

peso_racao = float(input("Digite quantos KGs o saco de ração comprado possui >> "))
racao_gato1 = float(input("Digite quantas gramas de ração é dado ao primeira gato >> "))
racao_gato2 = float(input("Digite quantas gramas de ração é dado ao segundo gato >> "))
racao_gato_gasta = (racao_gato1 + racao_gato2) * 5
conversao_racao = peso_racao * 1000
resto_racao = conversao_racao - racao_gato_gasta
print("Depois de 5 dias sobrará {} gramas.".format(resto_racao))


