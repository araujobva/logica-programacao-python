#Problema: Resolva o fatorial de forma recursiva de um valor inserido pelo usuário.

def main():
    valor = int(input("Digite um valor inteiro não negativo para encontrar o seu fatorial >> "))
    fat = fatorial(valor)
    print("O fatorial de {} é {}".format(valor, fat))

def fatorial(valor):
    if(valor == 1 or valor == 0):
        return 1
    fat = fatorial(valor - 1) * valor
    return fat

if __name__ == "__main__":
    main()