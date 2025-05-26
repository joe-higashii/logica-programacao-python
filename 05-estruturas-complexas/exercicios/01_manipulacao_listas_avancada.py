# 05-estruturas-complexas/exercicios/01_manipulacao_listas_avancada.py

"""
Exercício 1: Processamento de Dados com Listas

Objetivo: Implementar um sistema de análise de vendas usando operações complexas de listas.
"""
vendas = [
    {"produto": "A", "quantidade": 150, "preco": 29.90},
    {"produto": "B", "quantidade": 80, "preco": 49.90},
    {"produto": "A", "quantidade": 200, "preco": 29.90},
    {"produto": "C", "quantidade": 50, "preco": 99.90}
]

# 1. Calcular faturamento total
faturamento = sum(item['quantidade'] * item['preco'] for item in vendas)
print(f"Faturamento Total: R$ {faturamento:.2f}")

# 2. Agrupar vendas por produto
from collections import defaultdict
vendas_por_produto = defaultdict(list)
for item in vendas:
    vendas_por_produto[item['produto']].append(item)

# 3. Produto mais vendido em quantidade
produto_quantidade = {}
for produto, itens in vendas_por_produto.items():
    produto_quantidade[produto] = sum(item['quantidade'] for item in itens)

mais_vendido = max(produto_quantidade, key=produto_quantidade.get)
print(f"Produto Mais Vendido: {mais_vendido}")
