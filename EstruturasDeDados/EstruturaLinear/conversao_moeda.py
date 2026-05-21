"""
Problema:
Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui.

Essa pessoa vai passar por vários países e precisa converter seu dinheiro para:
- dólar
- marco alemão
- libra esterlina

Sabe-se que:
- 1 dólar = R$ 1,80
- 1 marco alemão = R$ 2,00
- 1 libra esterlina = R$ 1,57

O programa deve realizar as conversões e exibir os resultados.
"""

valorTotal = float(input("Digite o valor total R$ "))
dolar = valorTotal / 1.80
quantDolar = f"Quantidade de dólar é de {dolar}"
marco = valorTotal / 2.00
quantMarco = f"Quantidade de marco alemão é de {marco}"
libra = valorTotal / 1.57
quantLibra = f"Quantidade de libras esterlina é de {libra}"
print(dolar)
print(marco)
print(libra)

