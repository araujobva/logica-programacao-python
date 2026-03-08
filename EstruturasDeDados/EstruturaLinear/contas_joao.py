# Problema: João recebeu seu salário e precisa pagar duas contas que estão atrasadas.
# Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
# Faça um programa que calcule e mostre quanto restará do salário de João.

salario = float(input("Digite o valor do salário R$ "))
conta1 = float(input("Digite o valor da primeira conta R$ "))
conta2 = float(input("Digite o valor da segunda conta R$ "))
conta1 = conta1 + (conta1 * 0.2)
conta2 = conta2 + (conta2 * 0.2)
salario = salario - (conta1 + conta2)
print("O salário final é de R$ ",salario)
