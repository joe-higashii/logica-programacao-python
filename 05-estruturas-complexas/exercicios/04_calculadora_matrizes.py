# 05-estruturas-complexas/exercicios/04_calculadora_matrizes.py

"""
Calculadora de Matrizes com NumPy

Objetivo: Demonstrar operações matriciais avançadas usando NumPy.
"""

import numpy as np

def criar_matriz() -> np.ndarray:
    """Cria uma matriz a partir da entrada do usuário."""
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    
    print("Digite os elementos linha por linha (separados por espaço):")
    elementos = []
    for i in range(linhas):
        while True:
            linha = input(f"Linha {i+1}: ").split()
            if len(linha) == colunas:
                try:
                    elementos.append([float(x) for x in linha])
                    break
                except ValueError:
                    print("Entrada inválida. Use números.")
            else:
                print(f"Erro: Esperava {colunas} elementos.")
    
    return np.array(elementos)

def operacoes_matriciais() -> None:
    """Menu principal de operações matriciais."""
    print("=== Calculadora de Matrizes ===")
    print("Matriz A:")
    a = criar_matriz()
    print("\nMatriz A criada:")
    print(a)
    
    while True:
        print("\nOperações Disponíveis:")
        print("1. Adicionar Matriz B")
        print("2. Multiplicar por Matriz B")
        print("3. Transposta")
        print("4. Determinante")
        print("5. Inversa")
        print("6. Sair")
        
        opcao = input("Escolha uma operação: ")
        
        if opcao == '1':
            print("\nMatriz B:")
            b = criar_matriz()
            try:
                resultado = a + b
                print("\nResultado A + B:")
                print(resultado)
            except ValueError:
                print("Erro: Dimensões incompatíveis para adição.")
        
        elif opcao == '2':
            print("\nMatriz B:")
            b = criar_matriz()
            try:
                resultado = np.matmul(a, b)
                print("\nResultado A × B:")
                print(resultado)
            except ValueError:
                print("Erro: Dimensões incompatíveis para multiplicação.")
        
        elif opcao == '3':
            print("\nTransposta de A:")
            print(a.T)
        
        elif opcao == '4':
            if a.shape[0] != a.shape[1]:
                print("Erro: Matriz deve ser quadrada.")
            else:
                det = np.linalg.det(a)
                print(f"\nDeterminante: {det:.2f}")
        
        elif opcao == '5':
            try:
                inversa = np.linalg.inv(a)
                print("\nMatriz Inversa:")
                print(inversa)
            except np.linalg.LinAlgError:
                print("Erro: Matriz singular (determinante zero).")
        
        elif opcao == '6':
            print("Encerrando calculadora...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    operacoes_matriciais()
