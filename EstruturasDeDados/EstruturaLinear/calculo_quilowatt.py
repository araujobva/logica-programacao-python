# Problema: Sabe-se que o valor de 1 quilowatt corresponde a 1/5 (um quinto) do salário mínimo.
# O programa deve receber:
# - o valor do salário mínimo
# - a quantidade de quilowatts consumidos por uma residência.

# O programa deve calcular e mostrar:

# a) O valor em reais de cada quilowatt.
#    Para isso, basta dividir o salário mínimo por 5.

# b) O valor total a ser pago pela residência.
#    Esse valor é obtido multiplicando o preço de um quilowatt
#    pela quantidade de quilowatts consumidos.

# c) O valor final com desconto de 15%.
#    Primeiro calcula-se o valor total e depois aplica-se
#    um desconto de 15% sobre esse valor.

valor_salario = float(input("Digite o valor do salário mínimo R$ "))
quantidade_quilowatts = float(input("Digite a quantidade de quilowatts gasta >>> "))
valor_quilowatts = valor_salario / 5
valor_total_pagar = valor_quilowatts * quantidade_quilowatts
valor_total_pagar_desconto = valor_total_pagar - (valor_total_pagar * 0.15)
print("O valor de cada quilowatt é de R$ ",valor_quilowatts)
print("O valor total a ser pago pela residẽncia é de R$ ",valor_total_pagar)
print("O valor final com desconto de 15% é de R$ ",valor_total_pagar_desconto)
