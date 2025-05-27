# 06-orientacao-objetos/classes_objetos.py

"""
Módulo de Demonstração: Classes e Objetos em Python

Este arquivo explora a definição de classes, a criação de objetos (instâncias),
o uso de construtores (__init__), atributos de instância, atributos de classe,
métodos de instância, métodos de classe e métodos estáticos.
"""

print("--- Demonstração de Classes e Objetos ---")

class Cachorro: # Por convenção, nomes de classes começam com letra maiúscula (CamelCase) [9]
    """
    Esta classe representa um cachorro.
    Classes são como um blueprint ou um molde para criar objetos.
    """

    # Atributo de Classe:
    # É compartilhado por todas as instâncias (objetos) desta classe.
    # Geralmente define características ou comportamentos comuns a todos os objetos da classe.
    especie = "Canis familiaris"
    patas = 4

    def __init__(self, nome_do_cao, raca_do_cao, idade_do_cao):
        """
        Este é o método construtor da classe. É chamado automaticamente
        quando um novo objeto (instância) da classe é criado.
        'self' é uma referência à instância que está sendo criada.
        Ele permite que acessemos os atributos e métodos da instância.

        Atributos de Instância:
        São específicos para cada objeto criado a partir da classe.
        São definidos dentro do __init__ (ou outros métodos de instância) usando 'self'.
        """
        print(f"Objeto Cachorro '{nome_do_cao}' está sendo criado...")
        self.nome = nome_do_cao    # Atributo de instância
        self.raca = raca_do_cao    # Atributo de instância
        self.idade = idade_do_cao  # Atributo de instância
        self.truques = []          # Atributo de instância, inicializado como lista vazia [9]

    # Método de Instância:
    # Opera sobre uma instância específica da classe (o objeto).
    # Precisa do 'self' como primeiro parâmetro para acessar os atributos e
    # outros métodos da instância.
    def latir(self, vezes=1):
        """Faz o cachorro latir."""
        latido = f"{self.nome} ({self.raca}) diz: Au!"
        for _ in range(vezes):
            print(latido)

    def buscar_bola(self):
        """Simula o cachorro buscando uma bola."""
        print(f"{self.nome} correu e pegou a bola!")

    def adicionar_truque(self, truque):
        """Adiciona um truque à lista de truques do cachorro."""
        self.truques.append(truque)
        print(f"{self.nome} aprendeu um novo truque: {truque}!")

    def exibir_informacoes(self):
        """Exibe informações sobre o cachorro."""
        print(f"\n--- Informações de {self.nome} ---")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade} anos")
        print(f"Espécie: {self.especie}") # Acessando atributo de classe
        print(f"Número de patas: {Cachorro.patas}") # Outra forma de acessar atributo de classe
        if self.truques:
            print(f"Truques: {', '.join(self.truques)}")
        else:
            print(f"{self.nome} ainda não aprendeu truques.")

    # Método de Classe (@classmethod):
    # É um método que está ligado à classe e não à instância específica do objeto.
    # Recebe a classe em si como primeiro argumento (convencionalmente chamado 'cls').
    # Pode modificar o estado da classe (atributos de classe) ou criar instâncias da classe.
    @classmethod
    def alterar_especie(cls, nova_especie):
        """Altera o atributo de classe 'especie' para todos os cachorros."""
        print(f"A espécie de todos os cachorros foi alterada de '{cls.especie}' para '{nova_especie}'.")
        cls.especie = nova_especie

    @classmethod
    def criar_cachorro_anonimo(cls, raca):
        """Um 'factory method' que cria uma instância de Cachorro com nome padrão."""
        print(f"Criando um cachorro anônimo da raça {raca}...")
        return cls(nome_do_cao="Cão Sem Nome", raca_do_cao=raca, idade_do_cao=0)

    # Método Estático (@staticmethod):
    # Não está ligado nem à instância nem à classe. Funciona como uma função normal,
    # mas está definida dentro do escopo da classe (geralmente por organização ou
    # porque tem alguma relação lógica com a classe).
    # Não recebe 'self' nem 'cls' automaticamente.
    @staticmethod
    def eh_mamifero():
        """Retorna se cachorros são mamíferos (informação geral)."""
        return True

    @staticmethod
    def som_padrao_latido():
        return "Au Au!"

# --- Criando Objetos (Instâncias da Classe Cachorro) ---
print("\n--- Instanciando Objetos ---")
# Quando chamamos Cachorro(...), o método __init__ é executado.
cao1 = Cachorro(nome_do_cao="Rex", raca_do_cao="Labrador", idade_do_cao=3)
cao2 = Cachorro(nome_do_cao="Mel", raca_do_cao="Poodle", idade_do_cao=5)

# --- Acessando Atributos e Chamando Métodos de Instância ---
print("\n--- Usando Métodos de Instância ---")
cao1.latir()
cao2.latir(vezes=2)

cao1.adicionar_truque("Sentar")
cao1.adicionar_truque("Rolar")
cao2.adicionar_truque("Fingir de morto")

cao1.exibir_informacoes()
cao2.exibir_informacoes()

# --- Acessando e Modificando Atributos de Classe ---
print("\n--- Usando Métodos de Classe e Atributos de Classe ---")
print(f"Espécie original de todos os cachorros (via cao1): {cao1.especie}")
print(f"Espécie original de todos os cachorros (via classe): {Cachorro.especie}")

Cachorro.alterar_especie("Canis lupus familiaris") # Chamando método de classe

# A mudança no atributo de classe reflete em todas as instâncias
print(f"Nova espécie de cao1: {cao1.especie}")
print(f"Nova espécie de cao2: {cao2.especie}")

# Criando uma instância usando um método de classe (factory method)
cao_anonimo = Cachorro.criar_cachorro_anonimo(raca="Vira-lata")
cao_anonimo.exibir_informacoes()

# --- Chamando Métodos Estáticos ---
print("\n--- Usando Métodos Estáticos ---")
if Cachorro.eh_mamifero():
    print("Cachorros são mamíferos.")
print(f"O som padrão de um latido é: {Cachorro.som_padrao_latido()}")


# --- Demonstração de que atributos de instância são únicos ---
print("\n--- Atributos de Instância vs. Classe ---")
cao_brincalhao = Cachorro("Totó", "Beagle", 2)
cao_preguicoso = Cachorro("Soneca", "Basset Hound", 7)

cao_brincalhao.adicionar_truque("Dar a pata")
# cao_preguicoso não tem o truque "Dar a pata"
cao_brincalhao.exibir_informacoes()
cao_preguicoso.exibir_informacoes()

print(f"ID do objeto cao_brincalhao.truques: {id(cao_brincalhao.truques)}")
print(f"ID do objeto cao_preguicoso.truques: {id(cao_preguicoso.truques)}")
# Os IDs são diferentes, mostrando que cada instância tem sua própria lista de truques.

# Atributo de classe é compartilhado
print(f"Espécie de Totó: {cao_brincalhao.especie} (ID: {id(cao_brincalhao.especie)})")
print(f"Espécie de Soneca: {cao_preguicoso.especie} (ID: {id(cao_preguicoso.especie)})")
# Os IDs da string 'especie' podem ser os mesmos devido à otimização de strings imutáveis em Python,
# mas o ponto principal é que o valor é o mesmo e vem do mesmo local (atributo de classe).

print("\n--- Fim da Demonstração de Classes e Objetos ---")
