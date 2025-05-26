# 03-estruturas-controle/exercicios/04_soma_com_condicao_parada.py

"""
Exercício 4: Soma de Números com Condição de Parada (Sentinela)

Objetivo: Desenvolver um programa que permite ao usuário digitar vários números
e os soma. O programa deve parar de solicitar números e exibir a soma total
quando o usuário digitar um número específico (por exemplo, 0 ou um número negativo).
Utilizar uma estrutura de repetição `while` e, opcionalmente, `break`.
"""

print("--- Soma de Números (digite 0 para parar) ---")

soma_total = 0
contador_numeros = 0

# Loop `while True` cria um laço que, a princípio, seria infinito.
# A condição de parada será controlada internamente com `break`.
while True:
    try:
        entrada_str = input(f"Digite o {contador_numeros + 1}º número (ou 0 para sair): ")
        numero_atual = float(entrada_str)

        # Condição de parada (sentinela)
        if numero_atual == 0:
            print("Número 0 digitado. Encerrando a soma.")
            break  # Interrompe o laço `while`

        # Processamento
        soma_total += numero_atual
        contador_numeros += 1
        print(f"Número adicionado. Soma parcial: {soma_total:.2f}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

# Saída de dados final
print("\n--- Resultado Final ---")
if contador_numeros > 0:
    media = soma_total / contador_numeros
    print(f"Você digitou {contador_numeros} número(s).")
    print(f"A soma total dos números é: {soma_total:.2f}")
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número foi digitado (além do 0 para sair).")

print("--- Fim do Programa ---")

"""
Explicação da Lógica:
1.  Inicializamos `soma_total` e `contador_numeros` com 0.
2.  Usamos um laço `while True:`. Este tipo de laço continuará executando
    indefinidamente, a menos que uma instrução `break` seja encontrada.
3.  Dentro do laço:
    - O programa solicita um número ao usuário.
    - A entrada é convertida para `float`. Um `try-except` trata entradas inválidas.
    - Verificamos a condição de parada: `if numero_atual == 0:`. Se o usuário
      digitar 0 (nosso valor sentinela), a instrução `break` é executada,
      fazendo com que o programa saia do laço `while` imediatamente.
    - Se o número não for o sentinela, ele é adicionado à `soma_total`, o
      `contador_numeros` é incrementado, e a soma parcial é exibida.
4.  Após o laço ser interrompido (pelo `break`), o programa exibe os resultados
    finais: o número de valores digitados, a soma total e a média (se algum número
    válido foi inserido).

Este exercício ilustra como o laço `while` é útil quando o número de iterações
não é conhecido de antemão e depende de uma condição que pode ser alterada
durante a execução do laço ou de uma entrada específica do usuário (sentinela).
O `break` é fundamental para controlar a saída de laços `while True`.
"""
