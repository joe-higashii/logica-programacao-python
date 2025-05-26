# 05-estruturas-complexas/listas.py

"""
Listas em Python: Coleções Mutáveis e Dinâmicas

Características Principais:
- Ordenadas e indexadas
- Mutáveis (alteração in-place)
- Aceitam elementos heterogêneos
- Complexidade de operações comuns:
  - Append: O(1)
  - Insert: O(n)
  - Search: O(n)
"""

# Criação e Operações Básicas
print("=== LISTAS BÁSICAS ===")
frutas = ["maçã", "banana", "laranja"]
numeros = [7, 23, 42, 3.14]
misturado = [True, "Python", 42, ['a', 'b']]

print(f"Frutas: {frutas}")
print(f"Tipo: {type(frutas)}")
print(f"Tamanho: {len(frutas)} elementos")

# Operações de Indexação e Slicing
primeiro = frutas[0]             # Acesso O(1)
ultimo = frutas[-1]
sub_lista = numeros[1:3]         # Slicing O(k)

print(f"\nPrimeiro elemento: {primeiro}")
print(f"Último elemento: {ultimo}")
print(f"Sub-lista: {sub_lista}")

# Métodos Essenciais
frutas.append("abacaxi")         # O(1)
frutas.insert(1, "manga")        # O(n)
frutas.remove("banana")          # O(n)
item_removido = frutas.pop(2)    # O(n)

print(f"\nLista após modificações: {frutas}")
print(f"Item removido: {item_removido}")

# List Comprehensions (Filtro e Transformação)
quadrados = [x**2 for x in numeros if x > 10]
print(f"\nQuadrados de números >10: {quadrados}")

# Ordenação e Cópia
numeros.sort()                   # Ordenação in-place O(n log n)
copia_frutas = frutas.copy()     # Shallow copy O(n)

print(f"\nNúmeros ordenados: {numeros}")
print(f"Cópia da lista: {copia_frutas}")

# Análise de Desempenho (Exemplo Prático)
print("\n=== ANÁLISE DE COMPLEXIDADE ===")
from timeit import timeit

def testar_append():
    lista = []
    for i in range(1000):
        lista.append(i)

def testar_insert():
    lista = []
    for i in range(1000):
        lista.insert(0, i)

print(f"Append 1000 elementos: {timeit(testar_append, number=1000):.4f}s")
print(f"Insert 1000 elementos: {timeit(testar_insert, number=1000):.4f}s")
