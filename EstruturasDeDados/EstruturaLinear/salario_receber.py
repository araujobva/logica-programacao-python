# Problema: Faça um programa que receba o salário-base de um funcionário,
# calcule e mostre o salário a receber, sabendo-se que esse funcionário
# tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.

salario_base = float(input("Digite o salário base R$ "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_final = (salario_base + gratificacao) - imposto
print("O salário final a receber é de R$ {} ".format(salario_final))
