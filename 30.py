# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
def verificar_aprovacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f"Parabéns! Você foi aprovado com média {media:.2f}."
    else:
        return f"Infelizmente, você foi reprovado com média {media:.2f}."
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado = verificar_aprovacao(nota1, nota2, nota3)
print(resultado)