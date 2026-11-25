# Problema: Faça um programa que receba:
# - O código do estado de origem da carga de um caminhão, supondo que a digitação
#   do código do estado seja sempre válida, ou seja, um número inteiro entre 1 e 5.
# - O peso da carga do caminhão em toneladas.
# - O código da carga, supondo que a digitação do código da carga seja sempre
#   válida, ou seja, um número inteiro entre 10 e 40.

# ----------------
# Código do estado
# ----------------
# - Se o código do estado for 1, o imposto será de 35%.
# - Se o código do estado for 2, o imposto será de 25%.
# - Se o código do estado for 3, o imposto será de 15%.
# - Se o código do estado for 4, o imposto será de 5%.
# - Se o código do estado for 5, o imposto será isento.

# ---------------
# Código da carga
# ---------------
# - De 10 a 20 toneladas, o preço do quilo será de R$ 100,00.
# - De 21 a 30 toneladas, o preço do quilo será de R$ 250,00.
# - De 31 a 40 toneladas, o preço do quilo será de R$ 340,00.

# Calcule e mostre:
# - O peso da carga do caminhão convertido em quilos.
# - O preço da carga do caminhão.
# - O valor do imposto, sabendo-se que o imposto é cobrado sobre o preço da
#   carga do caminhão e que depende do estado de origem.
# - O valor total transportado pelo caminhão (carga mais imposto).

codigoEstado = float(input("Digite a código de origem (estado) da carga (entre 1 e 5) >> "))
peso = float(input("Digite o peso em toneladas da carga >> "))
codigoCarga = float(input("Digite o codigo da carga (entre 10 e 40) >> "))
valorCarga = float(input("Digite o valor da carga R$ "))
valorImposto = 0
if(codigoEstado == 1):
    valorImposto = 0.35
elif(codigoEstado == 2):
    valorImposto = 0.25
elif(codigoEstado == 3):
    valorImposto = 0.15
elif(codigoEstado == 4):
    valorImposto = 0.5
elif(codigoEstado == 5):
    valorImposto = 0
print(f"O peso da carga do caminhão em quilos é de >> {peso * 1000}")
print("O valor da carga do caminhão é de R$ {}".format(valorCarga))
print("O valor do imposto a ser pago é de R$ {}".format(valorImposto))
print(f"O valor total transportado pelo caminhão é de R$ {valorImposto + valorCarga}")

            

