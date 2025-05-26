# 04-tipos-dados/variaveis_constantes.py

"""
Demonstração de Variáveis e Constantes em Python

Conceitos:
- Variáveis: Contêineres mutáveis para armazenar dados
- Constantes: Valores que não devem ser alterados (convenção)
- Regras de Nomenclatura (PEP 8):
  - Snake_case para variáveis e funções
  - UPPER_CASE para constantes
  - Sem caracteres especiais ou espaços
"""

# Exemplo 1: Declaração Básica
nome_produto = "Notebook Gamer"  # string
preco = 4599.90  # float
estoque = 150  # int
disponivel = True  # bool

print("### Valores Iniciais ###")
print(f"Nome: {nome_produto} | Tipo: {type(nome_produto)}")
print(f"Preço: R$ {preco} | Tipo: {type(preco)}")
print(f"Estoque: {estoque} unidades | Tipo: {type(estoque)}")
print(f"Disponível: {disponivel} | Tipo: {type(disponivel)}")

# Exemplo 2: Tipagem Dinâmica
variavel_dinamica = 100
print("\n### Tipagem Dinâmica ###")
print(f"Valor inicial: {variavel_dinamica} | Tipo: {type(variavel_dinamica)}")

variavel_dinamica = "Agora sou uma string!"
print(f"Novo valor: {variavel_dinamica} | Tipo: {type(variavel_dinamica)}")

# Exemplo 3: Constantes (Convenção)
TAXA_JUROS = 0.015  # Uso de uppercase para constantes
DIAS_UTEIS = 22
MENSAGEM_ERRO = "Operação não permitida"

print("\n### Constantes ###")
print(f"Taxa: {TAXA_JUROS * 100}%")
print(f"Dias Úteis: {DIAS_UTEIS}")
print(f"Erro: {MENSAGEM_ERRO}")

# Tentativa de Reatribuição (não recomendado)
# Em Python, constantes são apenas uma convenção. Reatribuir uma constante, como abaixo, é possível,
# mas deve ser evitado para manter a clareza e a consistência do código.
nova_taxa_juros = 0.02  # Simulação de uma nova taxa, sem alterar a constante original
print(f"\nNova Taxa (simulada, não recomendado alterar constantes): {nova_taxa_juros}")

"""
Observações:
1. Python não possui constantes verdadeiras, apenas convenções
2. Para "constantes" mais seguras, usar classes ou módulos
3. A reatribuição de 'constantes' é possível, mas deve ser evitada
"""
