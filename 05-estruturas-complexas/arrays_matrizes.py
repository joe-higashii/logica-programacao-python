# 05-estruturas-complexas/arrays_matrizes.py

"""
Arrays e Matrizes com NumPy

Características Principais:
- Homogêneos e eficientes em memória
- Operações vetorizadas
- Broadcasting e álgebra linear
"""

import numpy as np

print("=== ARRAYS NUMPY ===")
# Criação de Arrays
array1d = np.array([1, 2, 3, 4, 5])
array2d = np.array([[1, 2], [3, 4], [5, 6]])

print(f"Array 1D:\n{array1d}")
print(f"\nArray 2D:\n{array2d}")
print(f"\nDimensões: {array2d.shape}")

# Operações Matemáticas
print("\n=== OPERAÇÕES MATEMÁTICAS ===")
array_a = np.array([10, 20, 30])
array_b = np.array([2, 3, 4])

print(f"Soma: {array_a + array_b}")
print(f"Multiplicação: {array_a * array_b}")
print(f"Produto Escalar: {np.dot(array_a, array_b)}")

# Matrizes e Álgebra Linear
print("\n=== ÁLGEBRA LINEAR ===")
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

produto_matricial = np.matmul(matriz_a, matriz_b)
determinante = np.linalg.det(matriz_a)

print(f"Produto Matricial:\n{produto_matricial}")
print(f"Determinante: {determinante:.2f}")

# Indexação Avançada
print("\n=== INDEXAÇÃO AVANÇADA ===")
dados = np.random.randint(0, 100, size=(5,5))
print(f"Matriz Original:\n{dados}")

linhas = [1, 3]
colunas = [0, 4]
submatriz = dados[np.ix_(linhas, colunas)]
print(f"\nSubmatriz Selecionada:\n{submatriz}")
