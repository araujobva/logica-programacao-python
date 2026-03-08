# Problema:
# O custo ao consumidor de um carro novo é a soma do preço de fábrica
# com o percentual de lucro do distribuidor e dos impostos aplicados
# ao preço de fábrica.
#
# Faça um programa que receba:
# - O preço de fábrica de um veículo
# - O percentual de lucro do distribuidor
# - O percentual de impostos
#
# Calcule e mostre:
# a) O valor correspondente ao lucro do distribuidor.
# b) O valor correspondente aos impostos.
# c) O preço final do veículo.

valorFabrica = float(input("Digite o valor de preço de fábrica R$ "))
percentualLucro = float(input("Digite o percentual de lucro >>> "))
percentualLucro = percentualLucro / 100
percentualImposto = float(input("Digite o percentual de imposto >>> "))
percentualImposto = percentualImposto / 100
print("O valor de lucro do distribuidor é de R$ ",valorFabrica * percentualImposto)
valorTotalImposto = (valorFabrica * percentualLucro) + (valorFabrica * percentualImposto)
print("O valor do dois impostos é de R$ ",valorTotalImposto)
print("O preço final do veículo é de R$ ",valorTotalImposto + valorFabrica)