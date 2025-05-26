# 03-estruturas-controle/repeticao.py

"""
Estruturas de Repetição (Laços ou Loops)

Permitem executar um bloco de código várias vezes. As principais em Python
são `for` (geralmente para um número conhecido de iterações ou para iterar
sobre coleções) e `while` (quando a repetição depende de uma condição que
pode mudar durante a execução).
"""

print("--- Demonstração de Estruturas de Repetição ---")

# Exemplo 1: Laço `for` com `range()` (Contador Definido)
print("\n--- Exemplo 1: `for` com `range()` ---")
print("Contando de 0 a 4:")
for i in range(5):  # range(5) gera números de 0 a 4
    print(f"Iteração número: {i}")

print("\nContando de 1 a 5:")
for i in range(1, 6): # range(1, 6) gera números de 1 a 5
    print(f"Item: {i}")

print("\nContando de 10 a 0, de 2 em 2 (regressivo):")
for i in range(10, -1, -2): # range(inicio, fim_exclusive, passo)
    print(f"Contagem regressiva: {i}")

# Exemplo 2: Laço `for` para iterar sobre uma lista (Coleção)
print("\n--- Exemplo 2: `for` com lista de frutas ---")
# Este exemplo é frequentemente citado em materiais introdutórios.
frutas = ["Maçã", "Banana", "Laranja", "Uva"]
print("Minhas frutas favoritas:")
for fruta in frutas:
    print(f"- {fruta}")

# Exemplo 3: Laço `while` (Teste no Início)
print("\n--- Exemplo 3: `while` ---")
contador = 0
print("Usando `while` para contar até 3 (inclusive):")
while contador <= 3:
    print(f"Valor do contador (while): {contador}")
    contador += 1  # Importante: atualizar a variável de controle para evitar loop infinito!

# Exemplo 4: `while` com `break` (Interrupção do laço)
print("\n--- Exemplo 4: `while` com `break` ---")
# O material do curso pode apresentar um exemplo de validação de entrada ou soma.
soma_positivos = 0
print("Digite números para somar. Digite um número negativo para parar.")
while True:  # Loop potencialmente infinito, controlado pelo `break`
    try:
        num_str = input("Digite um número: ")
        num = int(num_str)
        if num < 0:
            print("Número negativo digitado. Encerrando a soma.")
            break  # Sai imediatamente do laço `while`
        soma_positivos += num
        print(f"Soma parcial: {soma_positivos}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print(f"Soma total dos números positivos: {soma_positivos}")

# Exemplo 5: `while` com `continue` (Pular para a próxima iteração)
print("\n--- Exemplo 5: `while` com `continue` ---")
print("Imprimindo apenas números ímpares de 0 a 9 usando `continue`:")
numero_atual = -1
while numero_atual < 9:
    numero_atual += 1
    if numero_atual % 2 == 0:  # Se o número for par
        continue  # Pula o `print` e vai para a próxima iteração
    print(f"Número ímpar: {numero_atual}")

print("\n--- Fim da Demonstração de Repetição ---")

"""
Explicação:
- `for ... in range(start, stop, step)`: Usado para repetir um bloco de código um
  número conhecido de vezes. `start` é opcional (padrão 0), `step` é opcional (padrão 1).
  O loop vai até `stop - 1`.
- `for ... in colecao`: Itera sobre os itens de uma sequência (lista, tupla, string, etc.).
- `while condicao:`: Executa o bloco de código repetidamente enquanto a `condicao` for
  verdadeira. A condição é verificada antes de cada iteração. É crucial que algo
  dentro do loop possa, eventualmente, tornar a condição falsa, ou usar `break`.
- `break`: Termina o loop mais interno (`for` ou `while`) imediatamente.
- `continue`: Pula o restante do código dentro do loop para a iteração atual e
  passa para a próxima iteração.
"""
