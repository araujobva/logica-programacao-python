# Problema: Faça um programa que receba o número de horas trabalhadas, o valor do
# salário-mínimo e o número de horas extras trabalhadas. Calcule e mostre o salário
# a receber seguindo as regras a seguir.
#
# a) A hora trabalhada vale 1/8 do salário-mínimo.
# b) A hora extra vale 1/4 do salário-mínimo.
# c) O salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
# d) A quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra.
# e) O salário a receber equivale ao salário mínimo mais o salário bruto mais a quantia a receber pelas horas extras.

horas_trabalhadas = float(input("Digite o número de horas trabalhadas >> "))
valor_salario_minimo = float(input("Digite o valor do salário mínimo R$ "))
horas_extras_trabalhadas = float(input("Digite o número de horas extras trabalhadas >> "))
valor_hora_trabalhada = valor_salario_minimo / 8
valor_extras_trabalhadas = valor_salario_minimo / 4
valor_salario_bruto = valor_hora_trabalhada * horas_trabalhadas
valor_horas_extras = valor_hora_trabalhada * horas_extras_trabalhadas
salario_final = valor_salario_minimo + valor_salario_bruto + valor_horas_extras
print("O salário final a receber é de R$ {} ".format(salario_final))


