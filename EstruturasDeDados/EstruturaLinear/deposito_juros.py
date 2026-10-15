# Problema: Faça um programa que receba o valor da poupança, o valor de um depósito e a porcentagem do rendimento
# da poupança, calcule e mostre o valor da poupança com o seu futuro rendimento.

valor_poupanca = float(input("Digite o valor da poupança R$ "))
valor_deposito = float(input("Digite o valor do depósito R$ "))
porcentagem_rendimento = float(input("Digite o valor de porcentagem do rendimento >> "))
porcentagem_rendimento = porcentagem_rendimento / 100
valor_final = valor_poupanca + valor_deposito
valor_final = valor_final + (valor_final * porcentagem_rendimento)
print("O valor final da poupança é de R$ ",valor_final)
