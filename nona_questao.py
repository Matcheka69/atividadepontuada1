import os
os.system("clear")

renda= float(input("Digite sua renda mensal:"))
valor_emprestimo = float (input("Digite o valot que gostaria de tomar emprestado: "))
prestacoes = int(input("Digite o número de prestações: "))

limite_de_emprestimo = renda * 10
prestacoes_por_mes = valor_emprestimo / prestacoes
limite_de_parcelas = renda * 0.3

if valor_emprestimo <= limite_de_emprestimo and prestacoes_por_mes <= limite_de_parcelas:
    print("Parabéns, seu empréstimo foi aprovado! ")
else:
    print("Empréstimo negado. ")