# 04-tipos-dados/operadores.py

"""
Demonstração de Operadores em Python

Conceitos Abordados:
- Operadores Aritméticos
- Operadores de Comparação
- Operadores Lógicos
- Precedência de Operadores
"""

# Operadores Aritméticos
a = 15
b = 4

print("### Operadores Aritméticos ###")
print(f"{a} + {b} = {a + b}")  # Adição
print(f"{a} - {b} = {a - b}")  # Subtração
print(f"{a} * {b} = {a * b}")  # Multiplicação
print(f"{a} / {b} = {a / b}")  # Divisão Real
print(f"{a} // {b} = {a // b}")  # Divisão Inteira
print(f"{a} % {b} = {a % b}")  # Módulo
print(f"{a} ** {b} = {a ** b}")  # Exponenciação

# Operadores de Comparação
x = 10
y = 5

print("\n### Operadores de Comparação ###")
print(f"{x} > {y}? {x > y}")  # Maior que
print(f"{x} < {y}? {x < y}")  # Menor que
print(f"{x} == {y}? {x == y}")  # Igualdade
print(f"{x} != {y}? {x != y}")  # Diferença
print(f"{x} >= {y}? {x >= y}")  # Maior ou igual
print(f"{x} <= {y}? {x <= y}")  # Menor ou igual

# Operadores Lógicos
tempo_bom = True
feriado = False

print("\n### Operadores Lógicos ###")
print(f"Sair de casa? {tempo_bom and not feriado}")
print(f"Choverá ou é feriado? {not tempo_bom or feriado}")

# Precedência de Operadores
expressao = 10 + 5 * 3 ** 2 / (4 - 2)
print("\n### Precedência ###")
print("Expressão: 10 + 5 * 3 ** 2 / (4 - 2)")
print(f"Resultado: {expressao}")
print("Ordem: Parênteses > Expoente > Mult/Div > Add/Sub")

"""
Ordem de Precedência (da maior para menor):
1. Parênteses ()
2. Expoente **
3. Multiplicação *, Divisão /, Módulo %
4. Adição +, Subtração -
5. Operadores de Comparação
6. Operadores Lógicos (not, and, or)
"""
