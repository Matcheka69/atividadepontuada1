import os 
os.system("clear")

produto = input("Digite o nome do produto: ")
quantidade = int(input("dDigite a quantidade que deseja: "))
valor = float(input("Digite o valor do produto: "))

total = quantidade * valor
if quantidade <= 5:
    desconto = 0.2
elif quantidade <= 10:
    desconto = 0.3
else:
    desconto = 0.5
desconto_final = total * desconto
valor_final = total - desconto_final

print(f"\nProduto: {produto}")
print(f"Total: R$ {total:.2f}")
print(f"Seu desconto é: R$ { desconto_final:.2f}")
print(f" Total a ser pago: R$ {valor_final:.2f}")