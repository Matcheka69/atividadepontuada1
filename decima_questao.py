import os 
os.system("clear")

tipo = input("Digite o tipo de combústivel (A- álcool, 6- gasolina) :")
litros = float (input("Digite a quantidade de litros vendidos: "))

match tipo:
    case "A":
        preço_litro = 3.79
        desconto = 0.2 if litros <= 25 else 0.4
    case "G":            
        preço_litro = 6.59
        desconto = 0.3 if litros <= 25 else 0.5
    case _:
        print("Opção invalida.")

valor = litros * preço_litro
valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"\nTotal a pagar: R$ {valor_final:.2f}")