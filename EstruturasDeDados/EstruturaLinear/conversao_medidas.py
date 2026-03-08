# Problema: Sabe-se que:
# 1 pé = 12 polegadas
# 1 jarda = 3 pés
# 1 milha = 1.760 jardas
# Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
# a) Polegadas.
# b) Jardas.
# c) Milhas.

pes = float(input("Digite a medida em pés >>> "))
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1.760
print("Polegadas >>> ",polegadas)
print("Jardas >>> ",jardas)
print("Milhas >>> ",milhas)
