# 05-estruturas-complexas/tuplas.py

"""
Tuplas em Python: Coleções Imutáveis

Características Principais:
- Ordenadas e indexadas
- Imutáveis (segurança para chaves)
- Mais eficientes em memória que listas
- Uso comum: registros heterogêneos
"""

# Criação e Operações Básicas
print("=== TUPLAS BÁSICAS ===")
coordenadas = (-23.5505, -46.6333)
cores_rgb = (255, 128, 0)
dados_pessoa = ("Maria", 34, 1.68, True)

print(f"Tipo coordenadas: {type(coordenadas)}")
print(f"Tamanho: {len(dados_pessoa)} elementos")

# Acesso e Desempacotamento
nome, idade, altura, ativo = dados_pessoa
print(f"\nNome: {nome}, Altura: {altura}m")

# Tuplas como Chaves de Dicionário
localizacoes = {
    (35.6895, 139.6917): "Tóquio",
    (40.7128, -74.0060): "Nova York"
}
print(f"\nLocalização: {localizacoes[(35.6895, 139.6917)]}")

# Named Tuples (Registros Leves)
from collections import namedtuple
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'profissao'])
fulano = Pessoa("João", 28, "Engenheiro")

print("\n=== NAMED TUPLE ===")
print(f"Nome: {fulano.nome}, Profissão: {fulano.profissao}")

# Comparação de Desempenho vs Listas
print("\n=== BENCHMARK TUPLA vs LISTA ===")
import sys
from timeit import timeit

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(f"Tamanho lista: {sys.getsizeof(lista)} bytes")
print(f"Tamanho tupla: {sys.getsizeof(tupla)} bytes")

def acesso_lista():
    return lista[2]

def acesso_tupla():
    return tupla[2]

print(f"\nAcesso lista: {timeit(acesso_lista):.6f}s")
print(f"Acesso tupla: {timeit(acesso_tupla):.6f}s")
