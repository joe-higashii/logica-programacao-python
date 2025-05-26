# Implementação do fluxograma de média com loop
def calcular_medias():
    while True:
        n1 = float(input("Nota 1 (ou -1 para sair): "))
        if n1 == -1:
            break
        n2 = float(input("Nota 2: "))
        media = (n1 + n2) / 2
        print(f"Média: {media:.1f} | Status: {'Aprovado' if media >=7 else 'Reprovado'}")
