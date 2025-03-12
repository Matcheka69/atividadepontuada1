import os
os.system

#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na te

primeiro_valor= float(input("Digite o primeiro valor: "))
segundo_valor= float(input("Digite o segundo valor:" ))

soma= primeiro_valor + segundo_valor
produto= primeiro_valor * segundo_valor

if primeiro_valor==segundo_valor:   
    print(f"soma:{soma}")

if primeiro_valor != segundo_valor:
    print(f"produto:{produto}")

   
