# 04-tipos-dados/exercicios/02_conversao_tipos.py

"""
Exercício 2: Conversão de Tipos

Objetivo: Praticar conversões entre diferentes tipos
"""

# Entrada do usuário (sempre string)
while True:
    entrada = input("Digite um número: ")
    try:
        # Conversão para inteiro
        numero_int = int(entrada)
        print(f"Inteiro: {numero_int} | Tipo: {type(numero_int)}")

        # Conversão para float
        numero_float = float(entrada)
        print(f"Float: {numero_float} | Tipo: {type(numero_float)}")

        # Conversão para string
        texto = str(numero_float)
        print(f"String: {texto} | Tipo: {type(texto)}")

        # Conversão implícita
        resultado = numero_int + numero_float
        print(f"Resultado Implícito: {resultado} | Tipo: {type(resultado)}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
