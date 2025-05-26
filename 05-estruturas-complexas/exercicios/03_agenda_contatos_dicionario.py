# 05-estruturas-complexas/exercicios/03_agenda_contatos_dicionario.py

"""
Sistema de Agenda de Contatos com Dicionários Aninhados

Objetivo: Demonstrar o uso de dicionários aninhados para gerenciar informações
complexas de contatos.
"""

agenda: dict = {}

def formatar_telefone(numero: str) -> str:
    """Formata números de telefone para padrão (XX) XXXX-XXXX."""
    return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}" if len(numero) == 10 else numero

def adicionar_contato() -> None:
    """Adiciona um novo contato à agenda."""
    nome = input("Nome do Contato: ")
    telefones = []
    emails = []
    
    while True:
        tel = input("Telefone (enter para parar): ").strip()
        if not tel:
            break
        telefones.append(formatar_telefone(tel))
        
    while True:
        email = input("Email (enter para parar): ").strip()
        if not email:
            break
        emails.append(email.lower())
    
    agenda[nome] = {
        'telefones': telefones,
        'emails': emails,
        'favorito': False
    }
    print(f"Contato {nome} adicionado!")

def buscar_contato() -> None:
    """Busca contatos por nome ou número de telefone."""
    termo = input("Digite nome ou telefone: ").lower()
    encontrados = False
    
    for nome, info in agenda.items():
        if termo in nome.lower():
            encontrados = True
            exibir_contato(nome, info)
        else:
            for tel in info['telefones']:
                if termo in tel:
                    encontrados = True
                    exibir_contato(nome, info)
    
    if not encontrados:
        print("Nenhum contato encontrado.")

def exibir_contato(nome: str, info: dict) -> None:
    """Exibe os detalhes de um contato formatado."""
    print(f"\n=== {nome} ===")
    print("Telefones:")
    for i, tel in enumerate(info['telefones'], 1):
        print(f"  {i}. {tel}")
    
    print("\nEmails:")
    for i, email in enumerate(info['emails'], 1):
        print(f"  {i}. {email}")
    
    status = "★" if info['favorito'] else "☆"
    print(f"\nStatus: {status}")

def marcar_favorito() -> None:
    """Marca/desmarca um contato como favorito."""
    nome = input("Nome do Contato: ")
    if nome not in agenda:
        print("Contato não encontrado!")
        return
    
    agenda[nome]['favorito'] = not agenda[nome]['favorito']
    acao = "marcado" if agenda[nome]['favorito'] else "desmarcado"
    print(f"Contato {acao} como favorito!")

def listar_favoritos() -> None:
    """Lista todos os contatos marcados como favoritos."""
    print("\n=== Contatos Favoritos ===")
    for nome, info in agenda.items():
        if info['favorito']:
            print(f"★ {nome}")

def main() -> None:
    """Função principal da agenda."""
    while True:
        print("\n=== Agenda de Contatos ===")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Marcar Favorito")
        print("4. Listar Favoritos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            buscar_contato()
        elif opcao == '3':
            marcar_favorito()
        elif opcao == '4':
            listar_favoritos()
        elif opcao == '5':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
