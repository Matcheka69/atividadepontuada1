import os
os .system

primmeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))
media = (primmeira_nota + segunda_nota)/2

if media>= 6:
    print("\nExibindo resultados...")
    print(f"Média: {media}")
    print("Parabéns! Você foi aprovado")
elif media<= 4: 
    print("\nExibindo resultados...")
    print(f"Média: {media}")
    print("Você está na recuperação.")
else:
    print("\nExibindo resultados...")
    print(f"Média: {media}")
    print("Você foi aprovado!")