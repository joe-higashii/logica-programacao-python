# 06-orientacao-objetos/exercicios/03_formas_geometricas_polimorfismo.py

"""
Exercício 3: Formas Geométricas e Polimorfismo

Objetivo: Implementar diferentes classes de formas geométricas (ex: Retangulo,
Circulo, Triangulo) que herdam de uma classe base abstrata (ou com métodos
não implementados) `Forma`. Todas as formas devem ter um método `calcular_area()`
e um método `desenhar()`, demonstrando polimorfismo.
"""
import math

class Forma:
    """
    Classe base para formas geométricas.
    Pode ser considerada uma classe abstrata (conceitualmente),
    pois seus métodos principais devem ser implementados pelas subclasses.
    """
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        print(f"Forma base '{self.nome}' de cor '{self.cor}' criada.")

    def calcular_area(self):
        """Calcula a área da forma. Deve ser implementado pela subclasse."""
        # Em uma abordagem mais formal de classe abstrata, usaríamos:
        # from abc import ABC, abstractmethod
        # e este método seria @abstractmethod
        raise NotImplementedError("Subclasses devem implementar o método calcular_area().")

    def desenhar(self):
        """Simula o desenho da forma. Deve ser implementado pela subclasse."""
        raise NotImplementedError("Subclasses devem implementar o método desenhar().")

    def exibir_descricao(self):
        """Exibe uma descrição básica da forma."""
        print(f"\n--- {self.nome} ({self.cor}) ---")
        try:
            area = self.calcular_area()
            print(f"Área: {area:.2f}")
        except NotImplementedError:
            print("Área: Cálculo não implementado.")
        try:
            self.desenhar()
        except NotImplementedError:
            print("Desenho: Não implementado.")

class Retangulo(Forma):
    def __init__(self, nome, cor, largura, altura):
        super().__init__(nome, cor)
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def desenhar(self):
        print(f"Desenhando um retângulo {self.cor} de {self.largura}x{self.altura}.")
        for _ in range(int(self.altura / 2) if self.altura >=2 else 1): # Desenho simplificado
            print("+" + "-" * int(self.largura / 2  if self.largura >=2 else 1) + "+")
            print("|" + " " * int(self.largura / 2  if self.largura >=2 else 1) + "|")
        print("+" + "-" * int(self.largura / 2  if self.largura >=2 else 1) + "+")


class Circulo(Forma):
    def __init__(self, nome, cor, raio):
        super().__init__(nome, cor)
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def desenhar(self):
        print(f"Desenhando um círculo {self.cor} de raio {self.raio}.")
        # Desenho ASCII de círculo é complexo, vamos simplificar
        print("   ***   ")
        print(" *     * ")
        print("*       *")
        print(" *     * ")
        print("   ***   ")

class Triangulo(Forma):
    # Para simplificar, vamos assumir um triângulo retângulo
    def __init__(self, nome, cor, base, altura):
        super().__init__(nome, cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

    def desenhar(self):
        print(f"Desenhando um triângulo retângulo {self.cor} com base {self.base} e altura {self.altura}.")
        # Desenho simplificado
        for i in range(1, int(self.altura / 2 if self.altura >=2 else 1) + 1):
            print("*" * i)

# --- Função que demonstra Polimorfismo ---
def processar_formas(lista_de_formas):
    """
    Processa uma lista de formas, chamando seus métodos polimórficos.
    """
    print("\n\n=== Processando Formas (Polimorfismo) ===")
    for forma in lista_de_formas:
        forma.exibir_descricao() # Chama calcular_area() e desenhar() internamente

# --- Demonstração ---
formas_geometricas = [
    Retangulo("Ret1", "Azul", 10, 5),
    Circulo("Circ1", "Vermelho", 7),
    Triangulo("Tri1", "Verde", 8, 4),
    Retangulo("Ret2", "Amarelo", 6, 3)
]

processar_formas(formas_geometricas)

# Adicionando uma forma que não implementa os métodos (para ver o NotImplementedError)
class Pentagono(Forma):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        # Não implementa calcular_area nem desenhar

print("\n--- Testando forma com métodos não implementados ---")
penta = Pentagono("Pent1", "Roxo")
# A chamada a exibir_descricao vai tentar chamar os métodos e levantar NotImplementedError
# para as partes não implementadas, o que é pego pelo try-except em exibir_descricao.
penta.exibir_descricao()

"""
Explicação:
1.  A classe `Forma` atua como uma interface ou classe base abstrata. Ela define
    os métodos `calcular_area` e `desenhar` que as subclasses devem implementar.
    `NotImplementedError` é levantado se uma subclasse não os sobrescrever.
2.  `Retangulo`, `Circulo` e `Triangulo` herdam de `Forma` e fornecem suas
    implementações específicas para `calcular_area` e `desenhar`.
3.  A função `processar_formas` recebe uma lista de objetos `Forma`. Dentro do loop,
    quando `forma.exibir_descricao()` (que por sua vez chama `forma.calcular_area()`
    e `forma.desenhar()`) é chamado, o Python automaticamente executa a versão
    correta do método pertencente à classe real do objeto (`Retangulo`, `Circulo` ou `Triangulo`).
    Isso é polimorfismo: o mesmo chamado de método (`calcular_area` ou `desenhar`)
    resulta em comportamentos diferentes dependendo do tipo do objeto.
4.  O objeto `penta` da classe `Pentagono` (que não implementa os métodos) demonstra
    o que acontece quando os métodos esperados não são fornecidos pela subclasse,
    e como o `NotImplementedError` pode ser usado (e tratado) para sinalizar isso.
"""
