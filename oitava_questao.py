import os
os.system("clear")

opçao= input("""
Olá, bem-vindo a feirinha de cd, aqui vai a tabela de cores
Verde
Azul
Amarelo
Vermelho
Digite a opção desejada:
""")

match opçao:
    case "Verde":
        print("Olá o valor do cd verde é 10,00R$.")
    case "Azul":
        print(" o valor do cd azul é 20,00R$.")
    case "Amarelo":
        print ("Olá o valor do cd amarelo é 30,00R$.")
    case "Vermelho":
        print ("Olá o valor do cd vermelho é 40,00R$.")
