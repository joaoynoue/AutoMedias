notas = []

for i in range(3):
    nota = float(input("Digite sua nota: ")) 
    notas.append(nota)
    

media = sum(notas)/3
print(media)


def verificacao_de_aprovacao():
    if media < 6:
        print("Reprovado")
        
    elif media >= 8:
        print("aprovado")
    elif 6<= media <8:
        print('Recuperação')

verificacao_de_aprovacao()