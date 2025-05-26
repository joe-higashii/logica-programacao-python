# 05-estruturas-complexas/pilhas_filas.py

"""
Implementação de Pilhas e Filas

Características:
- Pilha (LIFO): Último a entrar é o primeiro a sair
- Fila (FIFO): Primeiro a entrar é o primeiro a sair
"""

from collections import deque

# Implementação de Pilha
print("=== PILHA COM LISTA ===")
class PilhaLista:
    def __init__(self):
        self._itens = []
    
    def empilhar(self, item):
        self._itens.append(item)
    
    def desempilhar(self):
        if not self.esta_vazia():
            return self._itens.pop()
        raise IndexError("Pilha vazia")
    
    def topo(self):
        return self._itens[-1] if self._itens else None
    
    def esta_vazia(self):
        return len(self._itens) == 0

pilha = PilhaLista()
pilha.empilhar('A')
pilha.empilhar('B')
print(f"Topo: {pilha.topo()}")
print(f"Desempilhado: {pilha.desempilhar()}")

# Implementação de Fila com deque
print("\n=== FILA COM DEQUE ===")
fila = deque(maxlen=5)
for i in range(1, 6):
    fila.append(i)
    print(f"Fila após adicionar {i}: {list(fila)}")

print(f"\nPróximo da fila: {fila.popleft()}")
print(f"Fila após remoção: {list(fila)}")

# Comparação de Desempenho
print("\n=== BENCHMARK DE IMPLEMENTAÇÕES ===")
from timeit import timeit

def testar_pilha_lista():
    p = PilhaLista()
    for i in range(1000):
        p.empilhar(i)
    for _ in range(1000):
        p.desempilhar()

def testar_pilha_deque():
    d = deque()
    for i in range(1000):
        d.append(i)
    for _ in range(1000):
        d.pop()

print(f"Pilha com lista: {timeit(testar_pilha_lista, number=1000):.4f}s")
print(f"Pilha com deque: {timeit(testar_pilha_deque, number=1000):.4f}s")
