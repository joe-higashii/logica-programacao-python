# Exemplo 1: Algoritmo de cálculo de média com condicional
def calculo_media():
    """
    Algoritmo Calc_Media (Baseado no material do curso)
    """
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    media = (n1 + n2) / 2

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

# Exemplo 2: Pseudocódigo para troca de lâmpada (versão 1)
def trocar_lampada():
    print("""
    Algoritmo Trocar_Lampada_V1
    Início
        1. Pegar escada
        2. Posicionar escada sob a lâmpada
        3. Remover lâmpada queimada
        4. Colocar lâmpada nova
        5. Guardar escada
    Fim
    """)

# Chamada dos exemplos
if __name__ == "__main__":
    calculo_media()
    trocar_lampada()
