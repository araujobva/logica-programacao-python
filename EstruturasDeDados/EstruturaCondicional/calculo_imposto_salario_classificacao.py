# Problema:
# Faça um programa que apresente o menu de opções a seguir, permita ao usuário
# escolher a opção desejada, receba os dados necessários para executar a operação
# e mostre o resultado. Verifique se a opção escolhida é válida.
#
# Menu de opções:
# 1. Imposto.
# 2. Novo Salário.
# 3. Classificação.
#
# Na opção 1:
# Receber o salário de um funcionário, calcular e mostrar o valor do imposto
# usando as regras a seguir:
# - Se o salário for menor que R$ 500,00, o percentual do imposto será de 5%.
# - Se o salário for igual ou superior a R$ 500,00 e até R$ 849,00,
#   o percentual do imposto será de 10%.
# - Se o salário for igual ou superior a R$ 850,00,
#   o percentual do imposto será de 15%.
#
# Na opção 2:
# Receber o salário de um funcionário, calcular e mostrar o valor do novo salário,
# usando as regras abaixo:
# - Salários maiores que R$ 1.500,00: aumento de R$ 25,00.
# - De R$ 750,00 (inclusive) a R$ 1.500,00 (inclusive):
#   aumento de R$ 50,00.
# - De R$ 450,00 (inclusive) a R$ 750,00:
#   aumento de R$ 75,00.
# - Salários menores que R$ 450,00: aumento de R$ 100,00.
#
# Na opção 3:
# Receber o salário de um funcionário e mostrar sua classificação
# usando a tabela abaixo:
# - Salário até R$ 700,00 (inclusive): classificação "Mal remunerado".
# - Salário maior que R$ 700,00: classificação "Bem remunerado".

op = float(input("Diigite a opção desejada\n1 - Imposto\n2 - Novo Salário\n3 - Classificação\n>> "))
salario = float(input("Digite o valor do salário R$ "))
match op:
    case 1:
        if(salario < 500):
            salario = salario - (salario * 0.05)
        elif(salario >= 500 and salario <= 849):
            salario = salario - (salario * 0.10)
        elif(salario >= 850):
            salario = salario - (salario * 0.15)
        print("O valor do novo salário é de R$ {}".format(salario))
    case 2: 
        if(salario > 1.500):
            salario = salario + 25
        elif(salario >= 750 and salario <= 1.500):
            salario = salario + 500
        elif(salario >= 450 and salario < 750):
            salario = salario + 750
        elif(salario < 450):
            salario = salario + 100
        print("O valor do novo salário é de R$ {}".format(salario))
    case 3:
        if(salario <= 700):
            print("Mal remunerado")
        else:
            print("Bem remunerado")
    case _:
        print("ERRO! Opção Inválida!")

