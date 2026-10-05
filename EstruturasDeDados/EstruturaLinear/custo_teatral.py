# Problema: Faça um programa que receba o custo de um espetáculo teatral
# e o preço do convite desse espetáculo.
# Esse programa deve calcular e mostrar a quantidade de convites que
# devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.

custo_espetaculo = float(input("Digite o valor do espetáculo R$ "))
preco_convite = float(input("Digite o valor de cada convite R$ "))
quantidade_convite = custo_espetaculo / preco_convite
print("É preciso vender {} convites para pagar o valor do espetáculo".format(quantidade_convite))
