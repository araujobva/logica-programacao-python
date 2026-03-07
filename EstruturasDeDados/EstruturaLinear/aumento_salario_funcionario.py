# Problema: Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input("Digite o salário atual do funcionário R$ "))
percentual = float(input("Digite o percentual de aumento >>> "))
percentual = percentual / 100
salarioFinal = salario + (salario * percentual)
print("O salário final com o aumento é de R$ ",salarioFinal)




