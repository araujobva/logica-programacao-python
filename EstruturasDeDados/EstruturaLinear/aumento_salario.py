# Problema: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

salario = input("Digite o salário atual >> ")
salario = float(salario)
novoSalario = salario + (salario * 0.25)
print("O salário com o aumento é de R$ ", novoSalario)

