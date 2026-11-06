# Problema: Faça um programa que receba o número de horas trabalhadas e o
# valor do salário-mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:
# a) A hora trabalhada vale a metade do salário-mínimo.
# b) O salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
# c) O imposto equivale a 3% do salário bruto.
# d) O salário a receber equivale ao salário bruto menos o imposto.

numeros_horas_trabalhadas = input("Digite o número de horas trabalhadas >> ")
numeros_horas_trabalhadas = float(numeros_horas_trabalhadas)
valor_salario_minimo = input("Digite o valor do salário mínimo R$ ")
valor_salario_minimo = float(valor_salario_minimo)
valor_hora_trabalhada = valor_salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * numeros_horas_trabalhadas
valor_imposto = valor_salario_bruto * 0.03
salario = valor_salario_bruto - valor_imposto
print("O salário a receber é de R$ {} reais.".format(salario))
