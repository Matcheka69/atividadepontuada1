import os
os.system


quantidade_kg_maça = float(input("Digite a quantidade em kg de maça: "))
quantidade_kg_morango = float(input("Digite a quantidade em kg de morango: "))


preço_morango_ate5= 2.50
preço_maça_ate5= 1.80
preço_morango_acima5= 2.20
preço_maça_acima5= 1.50


if quantidade_kg_morango <= 5:
    preço_morango = quantidade_kg_morango * preço_morango_ate5
else:
    preço_morango = quantidade_kg_morango * preço_morango_acima5
if quantidade_kg_maça <= 5:
    preço_maça = quantidade_kg_maça * preço_maça_ate5
else:
    preço_maça = quantidade_kg_maça * preço_maça_acima5

valor_final = preço_morango + preço_maça
if (quantidade_kg_morango + quantidade_kg_maça)  > 10 or valor_final > 15.00:
    valor_final *= 0.9
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")