# 03-estruturas-controle/exercicios/03_tabuada_numero.py

"""
Exercício 3: Tabuada de um Número

Objetivo: Criar um programa que solicita um número ao usuário e, em seguida,
exibe a tabuada de multiplicação desse número (de 1 a 10), utilizando
uma estrutura de repetição `for`.
"""

print("--- Gerador de Tabuada ---")

# Entrada de dados
try:
    numero_str = input("Digite um número inteiro para ver sua tabuada: ")
    numero = int(numero_str)

    print(f"\n--- Tabuada de Multiplicação do {numero} ---")

    # Processamento e Saída com Estrutura de Repetição `for`
    # O laço `for` com `range(1, 11)` irá iterar de 1 até 10.
    # A variável `i` assumirá os valores 1, 2, 3, ..., 10 em cada iteração.
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado}") # {i:2} formata para ocupar 2 espaços

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro válido.")

print("--- Fim do Programa ---")

"""
Explicação da Lógica:
1.  O programa pede ao usuário um número inteiro.
2.  A entrada é convertida para `int`. Um `try-except` lida com entradas inválidas.
3.  Um cabeçalho para a tabuada é impresso.
4.  A estrutura de repetição `for i in range(1, 11):` é utilizada:
    - `range(1, 11)` gera uma sequência de números de 1 até 10 (o segundo argumento
      do `range` é exclusivo).
    - Em cada iteração do laço, a variável `i` assume o próximo valor da sequência.
    - Dentro do laço:
        - `resultado = numero * i` calcula o produto do número fornecido pelo valor atual de `i`.
        - `print(f"{numero} x {i:2} = {resultado}")` exibe a linha da tabuada.
          A formatação `{i:2}` ajuda a alinhar os números quando `i` tem 1 ou 2 dígitos.
5.  Após o laço completar todas as iterações (de `i=1` até `i=10`), o programa termina.

Este exercício demonstra o uso do laço `for` com `range` para executar uma tarefa
(cálculo e impressão) um número definido de vezes.
"""
