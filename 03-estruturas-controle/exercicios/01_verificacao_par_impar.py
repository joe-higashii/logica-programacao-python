# 03-estruturas-controle/exercicios/01_verificacao_par_impar.py

"""
Exercício 1: Verificação de Número Par ou Ímpar

Objetivo: Utilizar uma estrutura de decisão simples (`if-else`) para
determinar se um número inteiro fornecido pelo usuário é par ou ímpar.
"""

print("--- Verificador de Número Par ou Ímpar ---")

# Entrada de dados
try:
    numero_str = input("Digite um número inteiro: ")
    numero = int(numero_str)

    # Processamento e Decisão
    # Um número é par se o resto da sua divisão por 2 for igual a 0.
    # O operador % (módulo) retorna o resto de uma divisão.
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Ímpar"

    # Saída de dados
    print(f"O número {numero} é {resultado}.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro válido.")

print("--- Fim do Programa ---")

"""
Explicação da Lógica:
1.  O programa solicita ao usuário que digite um número inteiro.
2.  A entrada (que é uma string) é convertida para um inteiro usando `int()`.
    Um bloco `try-except ValueError` é usado para tratar o caso em que o usuário
    digita algo que não pode ser convertido para um inteiro.
3.  A estrutura de decisão `if-else` é usada:
    - A condição `numero % 2 == 0` verifica se o resto da divisão do número por 2 é zero.
    - Se for zero, o número é par, e a variável `resultado` recebe a string "Par".
    - Caso contrário (se o resto não for zero), o número é ímpar, e `resultado` recebe "Ímpar".
4.  O resultado é exibido ao usuário.

Este exercício demonstra um uso fundamental da estrutura `if-else` para tomar
uma decisão baseada em uma condição matemática simples.
"""
