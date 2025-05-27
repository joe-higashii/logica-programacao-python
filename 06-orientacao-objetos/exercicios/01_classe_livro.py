# 06-orientacao-objetos/exercicios/01_classe_livro.py

"""
Exercício 1: Classe Livro

Objetivo: Criar uma classe simples para representar um Livro,
com atributos básicos e um método para exibir suas informações.
"""

class Livro:
    """
    Representa um livro com título, autor e número de páginas.
    """
    # Atributo de classe (opcional para este exercício, mas bom para lembrar)
    tipo_material = "Impresso ou Digital"

    def __init__(self, titulo, autor, num_paginas):
        """
        Construtor da classe Livro.
        Inicializa os atributos de instância: titulo, autor, num_paginas.
        """
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.capitulo_atual = 1 # Um atributo adicional com valor padrão

        print(f"Livro '{self.titulo}' criado.")

    def exibir_informacoes(self):
        """
        Exibe as informações formatadas do livro.
        """
        print("\n--- Detalhes do Livro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.num_paginas}")
        print(f"Tipo de Material: {Livro.tipo_material}") # Acessando atributo de classe
        print(f"Leitura atual no Capítulo: {self.capitulo_atual}")

    def avancar_capitulo(self, paginas_lidas_no_capitulo=0):
        """
        Avança para o próximo capítulo e, opcionalmente, registra páginas lidas.
        """
        self.capitulo_atual += 1
        print(f"'{self.titulo}' avançou para o capítulo {self.capitulo_atual}.")
        if paginas_lidas_no_capitulo > 0:
            print(f"Você leu {paginas_lidas_no_capitulo} páginas neste capítulo.")

# --- Demonstração da Classe Livro ---
# Criando instâncias (objetos) da classe Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
livro2 = Livro("Python para Análise de Dados", "Wes McKinney", 500)

# Exibindo informações dos livros
livro1.exibir_informacoes()
livro2.exibir_informacoes()

# Usando outros métodos
livro1.avancar_capitulo()
livro2.avancar_capitulo(paginas_lidas_no_capitulo=30)

livro1.exibir_informacoes() # Para ver o capítulo atualizado

"""
Explicação:
1.  A classe `Livro` é definida com o método `__init__` (construtor) que
    recebe `titulo`, `autor`, e `num_paginas` para inicializar os atributos
    de cada objeto livro.
2.  `tipo_material` é um atributo de classe, compartilhado por todos os livros.
3.  O método `exibir_informacoes` imprime os detalhes do livro de forma organizada.
4.  O método `avancar_capitulo` modifica o atributo de instância `capitulo_atual`.
5.  São criados dois objetos `livro1` e `livro2`, cada um com seus próprios dados.
6.  Os métodos são chamados nesses objetos para demonstrar seu comportamento.
"""
