# 04-tipos-dados/tipos_primitivos.py

"""
Tipos de Dados em Python

Classificação:
- Imutáveis: int, float, bool, str, tuple
- Mutáveis: list, dict, set

Características:
- Imutáveis: Não podem ser alterados após criação
- Mutáveis: Podem ser modificados in-place
"""

# Tipos Imutáveis
print("### Tipos Imutáveis ###")

# Inteiro
numero = 500
print(f"Inteiro: {numero} | Tipo: {type(numero)}")

# Float
pi = 3.14159
print(f"Float: {pi} | Tipo: {type(pi)}")

# String
mensagem = "Python é incrível!"
print(f"String: {mensagem} | Tipo: {type(mensagem)}")

# Booleano
ativo = True
print(f"Booleano: {ativo} | Tipo: {type(ativo)}")

# Tuple
coordenadas = (23.5, 46.2)
print(f"Tuple: {coordenadas} | Tipo: {type(coordenadas)}")

# Tipos Mutáveis
print("\n### Tipos Mutáveis ###")

# List
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print(f"Lista: {frutas} | Tipo: {type(frutas)}")

# Dict
produto = {"nome": "Teclado", "preço": 150.0, "estoque": 50}
produto["preço"] = 135.90
print(f"Dicionário: {produto} | Tipo: {type(produto)}")

# Set
numeros = {1, 2, 3, 4, 4, 3}  # Duplicados são removidos
numeros.add(5)
print(f"Set: {numeros} | Tipo: {type(numeros)}")

"""
Diferença Chave:
- Imutáveis: Qualquer operação cria novo objeto
- Mutáveis: Permitem modificações sem criar novo objeto
"""
