# 03-estruturas-controle/sequencia.py

"""
Estrutura Sequencial

A estrutura sequencial é a mais básica. Nela, as instruções são executadas
uma após a outra, na ordem em que são escritas no código.
Não há desvios ou repetições condicionais neste tipo puro de estrutura.
"""

print("--- Demonstração da Estrutura Sequencial ---")

# Passo 1: Entrada de dados (simulada ou real)
print("\nPasso 1: Definição de variáveis iniciais.")
nome_produto = "Notebook"
preco_custo = 2500.00
margem_lucro_percentual = 0.20  # 20%

# Passo 2: Processamento
print("Passo 2: Cálculos baseados nos dados de entrada.")
valor_lucro = preco_custo * margem_lucro_percentual
preco_venda = preco_custo + valor_lucro
imposto_sobre_venda = preco_venda * 0.05 # Suposição de 5% de imposto

# Passo 3: Saída de dados
print("Passo 3: Exibição dos resultados calculados.")
print(f"\n--- Detalhes do Produto: {nome_produto} ---")
print(f"Preço de Custo: R$ {preco_custo:.2f}")
print(f"Margem de Lucro (Valor): R$ {valor_lucro:.2f}")
print(f"Preço de Venda (Sem Imposto): R$ {preco_venda:.2f}")
print(f"Imposto sobre a Venda (5%): R$ {imposto_sobre_venda:.2f}")
print(f"Preço Final para o Consumidor: R$ {(preco_venda + imposto_sobre_venda):.2f}")

print("\n--- Fim da Demonstração Sequencial ---")

"""
Explicação:
Cada comando `print()` ou atribuição de variável é executado em ordem:
1.  As mensagens iniciais são impressas.
2.  As variáveis `nome_produto`, `preco_custo`, `margem_lucro_percentual` são definidas.
3.  Os cálculos de `valor_lucro`, `preco_venda` e `imposto_sobre_venda` são realizados sequencialmente.
4.  Finalmente, todos os resultados são impressos na tela.

Este é o fluxo natural de um script simples, e a base sobre a qual
as estruturas de decisão e repetição são construídas para adicionar lógica mais complexa.
"""
