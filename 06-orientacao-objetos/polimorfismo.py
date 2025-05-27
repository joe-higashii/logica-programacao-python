# 06-orientacao-objetos/polimorfismo.py

"""
Módulo de Demonstração: Polimorfismo em Python

Polimorfismo (do grego "muitas formas") é a capacidade de objetos de diferentes
classes responderem ao mesmo método de maneiras diferentes. Em Python, isso é
frequentemente alcançado através do "Duck Typing": se um objeto implementa
os métodos esperados, ele pode ser usado em um contexto polimórfico,
independentemente de sua classe ou herança.
"""

print("--- Demonstração de Polimorfismo ---")

# --- Definindo Classes com um Método em Comum ---
class Pato:
    def falar(self):
        return "Quack! Quack!"

    def mover(self):
        return "Nadando graciosamente."

class Cachorro:
    def falar(self):
        return "Au! Au!"

    def mover(self):
        return "Correndo e abanando o rabo."

class Gato:
    def falar(self):
        return "Miau!" # Gatos também falam [6]

    def mover(self):
        return "Andando sorrateiramente."

class Pessoa:
    def falar(self):
        return "Olá, como vai você?"

    def mover(self):
        return "Caminhando pela rua."

# --- Função que Demonstra Polimorfismo ---
def comunicar_com_entidade(entidade):
    """
    Esta função espera que a 'entidade' tenha um método 'falar'.
    Não importa qual é a classe da entidade, desde que ela "saiba falar".
    """
    print(f"A entidade diz: {entidade.falar()}")

def descrever_movimento(entidade):
    """
    Esta função espera que a 'entidade' tenha um método 'mover'.
    """
    print(f"A entidade está se movendo: {entidade.mover()}")


print("\n--- Demonstração com a função comunicar_com_entidade ---")
pato = Pato()
cachorro = Cachorro()
gato = Gato()
pessoa = Pessoa()

entidades_falantes = [pato, cachorro, gato, pessoa]

for entidade in entidades_falantes:
    # A função comunicar_com_entidade não se importa com o tipo exato do objeto,
    # apenas que ele tenha o método falar().
    comunicar_com_entidade(entidade)

print("\n--- Demonstração com a função descrever_movimento ---")
entidades_moveis = [pato, cachorro, gato, pessoa]

for entidade in entidades_moveis:
    descrever_movimento(entidade)


# --- Polimorfismo com Operadores (Exemplo com +) ---
# O operador '+' se comporta de forma polimórfica com diferentes tipos:
print("\n--- Polimorfismo com Operadores ---")
print(f"Soma de inteiros: 5 + 3 = {5 + 3}")
print(f"Concatenação de strings: 'Olá' + ' ' + 'Mundo' = {'Olá' + ' ' + 'Mundo'}")
print(f"Concatenação de listas: [1, 2] + [3, 4] = {[1, 2] + [3, 4]}")
# Cada tipo implementa o método especial `__add__` de forma diferente.


# --- Polimorfismo e Herança (Exemplo Clássico) ---
# Embora Duck Typing seja comum em Python, polimorfismo também funciona com herança.
class FormaGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        # Classes filhas devem implementar este método
        raise NotImplementedError("Subclasses devem implementar o método area()")

    def descrever(self):
        return f"Eu sou uma forma geométrica chamada {self.nome}."

class Retangulo(FormaGeometrica):
    def __init__(self, nome, largura, altura):
        super().__init__(nome)
        self.largura = largura
        self.altura = altura

    def area(self): # Sobrescreve o método area da classe pai
        return self.largura * self.altura

    def descrever(self): # Sobrescreve
        desc_pai = super().descrever()
        return f"{desc_pai} Sou um retângulo com área {self.area()}."

class Circulo(FormaGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def area(self): # Sobrescreve o método area
        return math.pi * (self.raio ** 2)

    def descrever(self): # Sobrescreve
        desc_pai = super().descrever()
        return f"{desc_pai} Sou um círculo com área {self.area():.2f}."

# Função que usa o polimorfismo das formas
def imprimir_detalhes_da_forma(forma):
    print(forma.descrever()) # Chama o método descrever (que chama area) específico da forma

print("\n--- Polimorfismo com Herança (Formas Geométricas) ---")
formas = [
    Retangulo("Ret A", 10, 5),
    Circulo("Circ B", 7),
    Retangulo("Ret C", 3, 8),
    Circulo("Circ D", 4.5)
]

for forma_obj in formas:
    imprimir_detalhes_da_forma(forma_obj)
    # print(f"A área da forma '{forma_obj.nome}' é: {forma_obj.area():.2f}") # Chamada direta do método polimórfico


print("\n--- Fim da Demonstração de Polimorfismo ---")
