# Problema: Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a) A idade dessa pessoa em anos.
# b) Quantos anos essa pessoa terá em 2050.
# c) A idade dessa pessoa em meses.
# d) A idade dessa pessoa em dias.
# e) A idade dessa pessoa em semanas.

anoNascimento = float(input("Digite o ano de nascimento >>> "))
anoAtual = float(input("Digite o ano atual >>> "))
idadeAnos = anoAtual - anoNascimento
idade_2050 = 2050 - anoNascimento
idade_meses = 12 * idadeAnos
idade_dias = 365 * idadeAnos
idade_semanas = 48 * idadeAnos
print("A idade atual dessa pessoa é de ", idadeAnos)
print("A idade dessa pessoa em 2050 será de ", idade_2050)
print("Essa pessoa tem ",idade_meses," meses")
print("Essa pessoa possui ",idade_dias," dias de vida")
print("Essa pessoa possui ",idade_semanas," semanas de vida")

