import os
os.system ("clear")

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.


nome= (input("Digite seu nome: "))
sexo= (input("Digite seu sexo: (M para masculino e F para feminino) "))
estado_civil=(input("Digite seu estado civil: "))


if sexo== "F" and estado_civil == "casado":

    tempo_de_casamento= input("Há quanto tempo você é casada?")
    print ("\nexibindo resultados:")
    print (f"nome: {nome}")
    print (f"sexo: {sexo}")
    print (f"estado_civil: {estado_civil}")
    print (f"Há quanto tempo está casada: {tempo_de_casamento} anos ")

else:
    print ("\nexibindo resultados:")
    print (f"nome: {nome}")
    print (f"sexo: {sexo}")
    print (f"estado_civil: {estado_civil}")


