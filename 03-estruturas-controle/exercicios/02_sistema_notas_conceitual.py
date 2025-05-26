# 03-estruturas-controle/exercicios/02_sistema_notas_conceitual.py

"""
Exercício 2: Sistema de Notas Conceitual

Objetivo: Implementar um sistema que atribui um conceito (A, B, C, D, F)
a uma nota numérica fornecida, utilizando uma estrutura de decisão encadeada
(`if-elif-else`). Este é um problema clássico para ilustrar múltiplas condições.
"""

print("--- Sistema de Atribuição de Conceitos ---")

# Entrada de dados
try:
    nota_str = input("Digite a nota do aluno (0 a 100): ") # Supomos escala 0-100 como no exemplo
    nota = float(nota_str)

    # Processamento e Decisão Encadeada
    conceito = "" # Inicializa a variável conceito

    if not (0 <= nota <= 100):
        conceito = "Nota inválida. Por favor, insira um valor entre 0 e 100."
    elif nota >= 90:
        conceito = "A (Excelente)"
    elif nota >= 80: # Já sabemos que é < 90 por não ter entrado no if anterior
        conceito = "B (Muito Bom)"
    elif nota >= 70: # Já sabemos que é < 80
        conceito = "C (Bom)"
    elif nota >= 60: # Já sabemos que é < 70
        conceito = "D (Regular)"
    else: # Se chegou aqui, a nota é < 60 (e >= 0, se não caiu no primeiro if)
        conceito = "F (Insuficiente/Reprovado)"

    # Saída de dados
    print(f"Para a nota {nota:.1f}, o conceito é: {conceito}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número válido para a nota.")

print("--- Fim do Programa ---")

"""
Explicação da Lógica:
1.  O programa solicita a nota numérica do aluno.
2.  A entrada é convertida para `float` para permitir notas com casas decimais.
    Um `try-except` trata entradas não numéricas.
3.  A estrutura `if-elif-else` é usada para determinar o conceito:
    - O primeiro `if` verifica se a nota está fora do intervalo válido (0-100).
    - Cada `elif` subsequente testa uma faixa de notas, da maior para a menor.
      A ordem é importante aqui. Uma vez que uma condição `elif` é verdadeira,
      as demais são ignoradas. Por exemplo, se `nota` é 85, ela satisfaz `nota >= 80`,
      o conceito "B" é atribuído, e os `elif` para 70 e 60 não são nem testados.
    - O `else` final captura todas as notas válidas que não se encaixaram nas
      categorias anteriores (neste caso, notas abaixo de 60).
4.  O conceito correspondente é exibido.

Este exercício é um exemplo clássico de como usar `if-elif-else` para implementar
uma lógica de múltipla escolha baseada em faixas de valores.
"""
