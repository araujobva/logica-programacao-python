# Problema: Um trabalhador recebeu seu salário e o depositou em sua conta-corrente bancária.
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
# Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

salario_depositado = float(input("Digite o valor para depósito R$ "))
cheque_01 = float(input("Digite o valor do primeiro cheque R$ "))
cheque_02 = float(input("Digite o valor do segundo cheque R$ "))
cpmf = 0.0038
saldo_conta = 0
saldo_conta = salario_depositado - (cheque_01 + cheque_02 + cpmf * 2)
print("O saldo atual é de R$ {}".format(saldo_conta))
