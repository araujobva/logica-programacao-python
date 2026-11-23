# Problema: Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual. 
# Mostre o cargo, o valor do aumento e seu novo salário.
# Os cargos estão abaixo:
# NOTA: Se o código digitado não for válido, informe ao usuário.
# - Código 1: Cargo Escriturário, percentual de aumento de 50%.
# - Código 2: Cargo Secretário, percentual de aumento de 35%.
# - Código 3: Cargo Caixa, percentual de aumento de 20%.

codigo = float(input("Digite o codigo do cargo >> "))
if codigo == 1:
    salario = float(input("Digite o salário atual >> "))
    salario = salario + (salario * 0.5)
    print("O cargo é Escrituário, o valor de aumento é de 50% e o seu novo salário é R$ {}".format(salario))
elif codigo == 2:
    salario = float(input("Digite o salário atual >> "))
    salario = salario + (salario * 0.35)
    print("O cargo é Secretário, o valor do aumento é de 35% e o seu novo salário é de R$ {}".format(salario))
elif codigo == 3:
    salario = float(input("Digite o salário atual >> "))
    salario = salario + (salario + 0.2)
    print("O cargo é Caixa, o valor do aumento é de 20% e o seu novo salário é de R$ {}".format(salario))
else:
    print("ERRO! O codigo digitado não é válido!")