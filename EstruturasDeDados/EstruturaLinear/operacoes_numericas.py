# Problema: Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
# a) O número digitado ao quadrado.
# b) O número digitado ao cubo.
# c) A raiz quadrada do número digitado.

import math

valor = float(input("Digite um número positivo maior que zero >> "))
quadrado = valor * valor
cubo = valor * valor * valor
raiz_quadrada = math.sqrt(valor)
print("O valor digitado ao quadrado é {}".format(quadrado))
print("O valor digitado ao cubo é de {}".format(cubo))
print("A raiz quadrada do valor é de ",raiz_quadrada)

