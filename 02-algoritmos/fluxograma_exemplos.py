# Exemplo 1: Fluxograma de decisão para aprovação
def fluxograma_aprovacao():
    print("""
    [Início]
      |
      V
    Leia N1, N2
      |
      V
    Média = (N1 + N2)/2
      |
      V
    +----[Média >= 7]----+
    |                    |
    V                    V
  "Aprovado"         "Reprovado"
      |                    |
      +--------+-----------+
               |
               V
            [Fim]
    """)

# Exemplo 2: Fluxograma para soma de 1 a 100
def fluxograma_soma():
    print("""
    [Início]
      |
      V
    Soma = 0
    Contador = 1
      |
      V
    +--[Contador <= 100]--+
    |                     |
    V                     |
  Soma += Contador        |
    |                     |
    V                     |
  Contador +=1            |
    |                     |
    +---------------------+
               |
               V
          Escreva Soma
               |
               V
            [Fim]
    """)

if __name__ == "__main__":
    fluxograma_aprovacao()
    fluxograma_soma()
