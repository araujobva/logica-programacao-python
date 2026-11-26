#Problema: Faça um programa que receba três números obrigatoriamente inteiros, distintos e em ordem crescente, e um quarto número que não siga esta regra. Mostre, em seguida, os quatro números em ordem crescente. NOTA(Não permitir que o usuário digite os valores sem ser na ordem crescente).

print(" .... Digite 3 valores inteiros e em ordem crescente distintos ... ")
valor1 = float(input("Digite o primeiro valor >> "))
valor2 = float(input("Digite o segundo valor >> "))
if(valor2 <= valor1):
    print("ERRO! Os valores não são crescentes\nO software será fechado!")
    sys.exi()
valor3 = float(input("Digite o terceiro valor >> "))
if(valor3 <= valor2):
    print("ERRO! os valores não são crescentes\nO software será fechado!")
    sys.exit()
valor4 = float(input("Digite um valor inteiro aleatório >> "))
if(valor4 <= valor1):
   print("{} - {} - {} - {}".format(valor4, valor1, valor2, valor3))
elif(valor4 >= valor1 and valor4 <= valor2 and valor4 <= valor3):
    print("{} - {} - {} - {}".format(valor1, valor4, valor2, valor3))
elif(valor4 >= valor2 and valor4 <= valor3):
    print("{} - {} - {} - {}".format(valor1, valor2, valor4, valor3))
elif(valor4 >= valor3):
     print("{} - {} - {} - {}".format(valor1, valor2, valor3, valor4))

