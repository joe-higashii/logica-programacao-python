# 05-estruturas-complexas/exercicios/02_sistema_estoque_tuplas.py

"""
Sistema de Gerenciamento de Estoque com Tuplas

Objetivo: Demonstrar o uso de tuplas imutáveis para registro de produtos e
operações de estoque seguras.
"""

from collections import namedtuple
from typing import Tuple, Dict

# Definindo uma namedtuple para representar produtos
Produto = namedtuple('Produto', ['id', 'nome', 'quantidade', 'preco'])

estoque: Dict[int, Produto] = {}
historico: Tuple[Produto, ...] = ()

def exibir_menu() -> None:
    """Exibe o menu de opções do sistema."""
    print("\n=== Sistema de Estoque ===")
    print("1. Adicionar Produto")
    print("2. Atualizar Estoque")
    print("3. Gerar Relatório")
    print("4. Histórico de Alterações")
    print("5. Sair")

def adicionar_produto() -> None:
    """Adiciona um novo produto ao estoque usando tupla."""
    global estoque, historico
    try:
        prod_id = int(input("ID do Produto: "))
        if prod_id in estoque:
            print("Erro: ID já existe!")
            return
            
        nome = input("Nome: ")
        quant = int(input("Quantidade Inicial: "))
        preco = float(input("Preço Unitário: "))
        
        novo_produto = Produto(prod_id, nome, quant, preco)
        estoque[prod_id] = novo_produto
        historico += (novo_produto,)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Use números para ID, quantidade e preço.")

def atualizar_estoque() -> None:
    """Atualiza a quantidade em estoque de forma imutável."""
    global estoque, historico
    try:
        prod_id = int(input("ID do Produto: "))
        if prod_id not in estoque:
            print("Erro: Produto não encontrado!")
            return
            
        operacao = input("Operação ([+]Adicionar/[-]Remover): ")
        quantidade = int(input("Quantidade: "))
        
        produto = estoque[prod_id]
        nova_quant = produto.quantidade + quantidade if operacao == '+' else produto.quantidade - quantidade
        
        if nova_quant < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return
            
        # Cria nova tupla com valores atualizados
        produto_atualizado = produto._replace(quantidade=nova_quant)
        estoque[prod_id] = produto_atualizado
        historico += (produto_atualizado,)
        print("Estoque atualizado!")
    except ValueError:
        print("Entrada inválida. Use números para ID e quantidade.")

def gerar_relatorio() -> None:
    """Gera relatório formatado do estoque."""
    print("\n=== Relatório de Estoque ===")
    print(f"{'ID':<5} {'Nome':<20} {'Quantidade':<10} {'Preço':<10}")
    for prod in estoque.values():
        print(f"{prod.id:<5} {prod.nome:<20} {prod.quantidade:<10} R${prod.preco:.2f}")

def exibir_historico() -> None:
    """Exibe o histórico de alterações imutável."""
    print("\n=== Histórico de Alterações ===")
    for i, versao in enumerate(historico, 1):
        print(f"Alteração {i}: {versao.nome} - Quant: {versao.quantidade}")

def main() -> None:
    """Função principal do sistema."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            atualizar_estoque()
        elif opcao == '3':
            gerar_relatorio()
        elif opcao == '4':
            exibir_historico()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
