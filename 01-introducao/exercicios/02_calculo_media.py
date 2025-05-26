# 01-introducao/exercicios/02_calculo_media.py

"""
Exercício 2: Implementando o Cálculo de Média em Python

Objetivo: Traduzir o pseudocódigo e a lógica do fluxograma para cálculo
de média aritmética (apresentados na Tabela 2 e Figura 4 do material do curso [1])
para a linguagem Python. Este exercício cobre os conceitos de entrada de dados,
processamento, saída de dados e estruturas de decisão.
"""

# --- Início do Algoritmo Calc_Media ---
print("--- Cálculo de Média Semestral do Aluno ---")

# Etapa de Entrada de Dados [1]
# No pseudocódigo: Leia (N1, N2)
# Em Python, usamos input() para ler dados do usuário.
# A função float() converte o texto de entrada para um número de ponto flutuante (real).
try:
    n1_str = input("Digite a primeira nota (N1): ")
    n1 = float(n1_str)

    n2_str = input("Digite a segunda nota (N2): ")
    n2 = float(n2_str)
except ValueError:
    print("Erro: Por favor, digite apenas números válidos para as notas.")
    exit() # Encerra o programa se a entrada não for um número

# Etapa de Processamento [1]
# No pseudocódigo: Media <- (N1+N2)/2
media = (n1 + n2) / 2

# Etapa de Saída de Dados [1]
# Apresentação dos resultados parciais e da média calculada.
print("\n--- Resultados ---")
print(f"Nota 1 (N1) informada: {n1:.2f}")
print(f"Nota 2 (N2) informada: {n2:.2f}")
print(f"Média calculada: {media:.2f}") # O :.2f formata o número para 2 casas decimais

# Estrutura de Decisão (baseada no fluxograma e pseudocódigo) [1]
# No pseudocódigo:
# Se Media >= 7 então
#   Escreva (“Aprovado”);
# Senão
#   Escreva (“Reprovado”);
# FimSe
if media >= 7.0:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Situação do aluno: {situacao}")

print("--- Fim do Programa ---")

"""
Explicação Adicional:
1.  Entrada de Dados:
    O programa solicita ao usuário que insira duas notas. A função `input()` captura essa entrada como texto.
    A função `float()` é crucial aqui para converter esse texto em números que podem ser usados em cálculos matemáticos.
    A declaração `Var N1, N2, Media: real;` no pseudocódigo [1] indica que essas variáveis devem armazenar números reais.
    Incluímos um bloco `try-except` para lidar com possíveis erros se o usuário digitar algo que não seja um número.

2.  Processamento:
    A média é calculada usando a expressão aritmética `(n1 + n2) / 2` e armazenada na variável `media` [1].

3.  Saída de Dados:
    O programa exibe as notas originais e a média calculada. As f-strings (formatted string literals)
    são usadas para incorporar os valores das variáveis diretamente no texto a ser impresso de forma legível.
    A formatação `:.2f` garante que os números sejam exibidos com duas casas decimais.

4.  Estrutura de Decisão:
    A instrução `if-else` do Python é usada para implementar a lógica condicional.
    Se a `media` for maior ou igual a 7.0, a `situacao` do aluno é definida como "Aprovado".
    Caso contrário (else), é definida como "Reprovado". Isso reflete diretamente a estrutura
    de decisão mostrada no pseudocódigo e no fluxograma do material do curso [1].

Este exercício demonstra o ciclo completo de processamento de dados:
Entrada (notas) -> Processamento (cálculo da média) -> Saída (resultado e situação) [1].
"""
