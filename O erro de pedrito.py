print("-------CALCULADORA DE MÉDIA PONDERADA-------")

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))

peso_das_notas =float(input("Qual a nota média para passar?: "))

media1 = (nota1 * peso_das_notas) 
media2 = (nota2 * peso_das_notas) 
media3 = (nota3 * peso_das_notas) 

media_final = (media1 + media2 + media3)/(peso_das_notas*3)

print(f'A sua média pondenrada final é: {media_final}')

if media_final >= 6:
    print("Parabéns, você passou!")

else:
    print("Que pena você não passou!")



