# Problema: Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada. 
# Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo, sem se preocupar com a altura do usuário.
 
altura_degrau = float(input("Digite a altura de cada degrau em centímetos >> "))
altura_desejada = float(input("Digite a altura que pretende chegar em centímetros >> "))
quantidade_degrau = altura_desejada / altura_degrau
print("O usuário deverá subir {} degraus para chegar em {} centímetros".format(quantidade_degrau, altura_desejada)) 



