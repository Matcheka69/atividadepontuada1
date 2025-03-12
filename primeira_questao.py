import os
os.system ("clear")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário,imprima que a A + B é maior que C. 


primeiro_valor=(float(input("Digite o primeiro valor: ")))
segundo_valor=(float(input("Digite o segundo valor:" )))
terceiro_valor=(float(input("Digite o terceiro valor: ")))

soma= primeiro_valor + segundo_valor

if soma > terceiro_valor:
    print("Maior que C")

else: soma < terceiro_valor
print ("Menor que C")


