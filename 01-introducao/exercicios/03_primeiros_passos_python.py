# 01-introducao/exercicios/03_primeiros_passos_python.py

"""
Exercício 3: Primeiros Passos com Python

Objetivo: Familiarizar-se com comandos básicos do Python, como a função `print()`,
a criação e uso de variáveis, e conectar esses aprendizados com o contexto histórico
da programação apresentado no material do curso [1].
"""

# Parte 1: Recordando a História da Programação [1]
print("--- Figuras Notáveis na História da Programação ---")
# O material do curso [1] destaca várias personalidades. Vamos citar algumas:
print("Ada Lovelace (década de 1800): Considerada a primeira programadora, por seu trabalho com a Máquina Analítica.")
print("Alan Turing (década de 1930): Propôs a Máquina de Turing, base para o conceito moderno de algoritmo e computação.")
print("Dennis Ritchie (década de 1970): Desenvolveu a linguagem de programação C.")
print("-" * 40) # Imprime uma linha para separação visual

# Parte 2: Explorando o Comando `print()` do Python
print("\n--- Explorando a Função print() ---")
# A função print() é usada para exibir informações na tela.
print("Olá, futuro programador(a) Python!") # Exibindo uma string (texto) simples.

# Podemos imprimir resultados de expressões diretamente:
print("Resultado de 5 + 3 é:", 5 + 3)

# Usando f-strings (formatted string literals) para combinar texto e variáveis/expressões:
# O 'f' antes das aspas permite embutir expressões dentro de {}
calculo_simples = 10 * 2
print(f"Uma f-string pode mostrar que 10 * 2 = {calculo_simples}.")
print("-" * 40)

# Parte 3: Trabalhando com Variáveis [1]
print("\n--- Introdução às Variáveis em Python ---")
# Uma variável é um nome onde atribuímos valores [1 - Seção 1.4.1].
# Em Python, não é necessário declarar o tipo da variável explicitamente;
# o tipo é inferido a partir do valor atribuído [1 - Figura 17].

nome_aluno = "Maria Silva"  # Variável do tipo string (str) para armazenar texto
idade_aluno = 22            # Variável do tipo inteiro (int) para armazenar números inteiros
curso_aluno = "Lógica de Programação com Python" # Outra string

# Exibindo os valores armazenados nas variáveis:
print(f"Nome do Aluno(a): {nome_aluno}")
print(f"Idade: {idade_aluno} anos")
print(f"Curso: {curso_aluno}")

# Variáveis podem ser usadas em expressões:
ano_nascimento_aproximado = 2024 - idade_aluno
print(f"{nome_aluno} nasceu aproximadamente em {ano_nascimento_aproximado}.")
print("-" * 40)

print("\nFim dos primeiros passos práticos com Python!")

"""
Explicação Adicional:

1.  História da Programação:
    Relembramos algumas figuras históricas mencionadas na seção 1.1.1 do material [1],
    utilizando `print()` para exibir essas informações.

2.  Função `print()`:
    Demonstramos como usar `print()` para:
    - Exibir texto literal (strings).
    - Mostrar o resultado de cálculos matemáticos.
    - Utilizar f-strings para uma forma mais elegante e legível de combinar texto com
      valores de variáveis ou resultados de expressões.

3.  Variáveis:
    Introduzimos o conceito de variáveis, conforme descrito na seção 1.4.1 do material [1].
    - `nome_aluno`, `curso_aluno` são exemplos de variáveis que armazenam texto (tipo `str`).
    - `idade_aluno` é um exemplo de variável que armazena um número inteiro (tipo `int`).
    - Python determina automaticamente o tipo da variável (tipagem dinâmica).
    - Mostramos como acessar os valores armazenados e como usá-los em outras expressões
      (como no cálculo do `ano_nascimento_aproximado`).

Este script serve como uma introdução prática aos comandos mais básicos e essenciais
para começar a programar em Python, sempre referenciando os conceitos do material do curso [1].
"""
