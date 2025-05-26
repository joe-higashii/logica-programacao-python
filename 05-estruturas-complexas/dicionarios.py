# 05-estruturas-complexas/dicionarios.py

"""
Dicionários em Python: Mapeamentos Chave-Valor

Características Principais:
- Coleções não ordenadas (Python 3.7+ ordenadas)
- Acesso O(1) via hash table
- Chaves imutáveis e únicas
- Valores heterogêneos
"""

# Criação e Operações Básicas
print("=== DICIONÁRIOS BÁSICOS ===")
pessoa = {
    "nome": "Carlos",
    "idade": 35,
    "skills": ["Python", "SQL", "Git"]
}

print(f"Chaves: {pessoa.keys()}")
print(f"Valores: {pessoa.values()}")
print(f"Idade: {pessoa.get('idade', 'N/A')}")

# Atualização e Métodos
pessoa.update({"cidade": "São Paulo", "idade": 36})
telefone = pessoa.setdefault("telefone", "11 99999-9999")

print(f"\nDados atualizados: {pessoa}")
print(f"Telefone: {telefone}")

# Dicionários Aninhados
print("\n=== DICIONÁRIOS ANINHADOS ===")
empresa = {
    "departamentos": {
        "vendas": {
            "chefe": "Maria",
            "funcionarios": 12
        },
        "ti": {
            "chefe": "Pedro",
            "funcionarios": 8
        }
    }
}

print(f"Chefe de TI: {empresa['departamentos']['ti']['chefe']}")

# Compreensão de Dicionários
quadrados = {x: x**2 for x in range(1, 6)}
print(f"\nQuadrados: {quadrados}")

# Tratamento de Colisões (Exemplo Simplificado)
print("\n=== COLISÕES DE HASH ===")
class ChavePersonalizada:
    def __init__(self, valor):
        self.valor = valor
    
    def __hash__(self):
        return hash(self.valor % 2)  # Forçando colisões
    
    def __eq__(self, outro):
        return self.valor == outro.valor

dicionario_colisao = {}
for i in range(1, 5):
    chave = ChavePersonalizada(i)
    dicionario_colisao[chave] = f"Valor {i}"

print(f"Itens com colisões: {dicionario_colisao.items()}")
