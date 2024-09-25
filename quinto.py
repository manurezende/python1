nota_1 = input("digite a nota do primeiro bimestre: ")
nota_2 = input("digite a nota do segundo bimestre: ")
nota_3 = input("digite a nota do terceiro bimestre: ")
nota_4 = input("digite a nota do quarto bimestre: ")

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)
nota_4 = float(nota_4)

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 6:
    print("o aluno foi aprovado",media)

elif media <= 4:
    print("o aluno foi reprovado",media)   

else:
    print("o aluno esta recuperação",media)