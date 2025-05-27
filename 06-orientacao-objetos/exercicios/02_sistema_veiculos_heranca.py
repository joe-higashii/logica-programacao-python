# 06-orientacao-objetos/exercicios/02_sistema_veiculos_heranca.py

"""
Exercício 2: Sistema de Veículos com Herança

Objetivo: Modelar um sistema com uma classe base `Veiculo` e subclasses
como `Carro` e `Motocicleta`, demonstrando herança, sobrescrita de métodos
e uso de `super()`.
"""

class Veiculo:
    """Classe base para todos os tipos de veículos."""
    def __init__(self, marca, modelo, cor, ano_fabricacao):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.ligado = False
        self.velocidade_atual = 0
        print(f"Veículo base {self.marca} {self.modelo} criado.")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            if self.velocidade_atual == 0:
                self.ligado = False
                print(f"{self.marca} {self.modelo} desligado.")
            else:
                print(f"Não é seguro desligar. {self.marca} {self.modelo} está a {self.velocidade_atual} km/h.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def acelerar(self, incremento_velocidade):
        if self.ligado:
            self.velocidade_atual += incremento_velocidade
            print(f"{self.marca} {self.modelo} acelerou para {self.velocidade_atual} km/h.")
        else:
            print(f"Não pode acelerar. {self.marca} {self.modelo} está desligado.")

    def frear(self, decremento_velocidade):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= decremento_velocidade
            if self.velocidade_atual < 0:
                self.velocidade_atual = 0
            print(f"{self.marca} {self.modelo} freou para {self.velocidade_atual} km/h.")
        else:
            print(f"{self.marca} {self.modelo} já está parado.")

    def exibir_status(self):
        status_motor = "Ligado" if self.ligado else "Desligado"
        print(f"\n--- Status de {self.marca} {self.modelo} ({self.ano_fabricacao}) ---")
        print(f"Cor: {self.cor}")
        print(f"Motor: {status_motor}")
        print(f"Velocidade: {self.velocidade_atual} km/h")

class Carro(Veiculo):
    """Subclasse Carro, herda de Veiculo."""
    def __init__(self, marca, modelo, cor, ano_fabricacao, num_portas, tipo_cambio):
        # Chama o construtor da classe pai (Veiculo)
        super().__init__(marca, modelo, cor, ano_fabricacao)
        self.num_portas = num_portas       # Atributo específico de Carro
        self.tipo_cambio = tipo_cambio     # Atributo específico de Carro
        self.ar_condicionado_ligado = False
        print(f"Carro específico {self.marca} {self.modelo} com {self.num_portas} portas criado.")

    # Sobrescrita do método exibir_status para adicionar detalhes do carro
    def exibir_status(self):
        super().exibir_status() # Chama o método da classe pai para imprimir informações base
        print(f"Número de Portas: {self.num_portas}")
        print(f"Tipo de Câmbio: {self.tipo_cambio}")
        status_ar = "Ligado" if self.ar_condicionado_ligado else "Desligado"
        print(f"Ar Condicionado: {status_ar}")

    def ligar_ar_condicionado(self):
        if self.ligado:
            if not self.ar_condicionado_ligado:
                self.ar_condicionado_ligado = True
                print(f"Ar condicionado do {self.marca} {self.modelo} ligado.")
            else:
                print("Ar condicionado já está ligado.")
        else:
            print(f"Motor do {self.marca} {self.modelo} precisa estar ligado para usar o ar.")

class Motocicleta(Veiculo):
    """Subclasse Motocicleta, herda de Veiculo."""
    def __init__(self, marca, modelo, cor, ano_fabricacao, cilindradas, tem_bau):
        super().__init__(marca, modelo, cor, ano_fabricacao)
        self.cilindradas = cilindradas  # Atributo específico
        self.tem_bau = tem_bau          # Atributo específico
        print(f"Motocicleta específica {self.marca} {self.modelo} de {self.cilindradas}cc criada.")

    # Sobrescrita
    def exibir_status(self):
        super().exibir_status()
        print(f"Cilindradas: {self.cilindradas}cc")
        status_bau = "Sim" if self.tem_bau else "Não"
        print(f"Possui Baú: {status_bau}")

    # Sobrescrita de acelerar para adicionar um comportamento específico
    def acelerar(self, incremento_velocidade):
        if self.ligado:
            super().acelerar(incremento_velocidade) # Chama a lógica base de acelerar
            if self.velocidade_atual > 80:
                print(f"Emoção! {self.marca} {self.modelo} está voando baixo!")
        else:
            print(f"Não pode acelerar. {self.marca} {self.modelo} está desligado.")


# --- Demonstração ---
meu_hb20 = Carro("Hyundai", "HB20", "Prata", 2022, 4, "Automático")
minha_lander = Motocicleta("Yamaha", "Lander 250", "Azul", 2023, 250, True)

meu_hb20.ligar()
meu_hb20.acelerar(50)
meu_hb20.ligar_ar_condicionado()
meu_hb20.exibir_status()
meu_hb20.desligar() # Não deve desligar pois está em movimento

meu_hb20.frear(50)
meu_hb20.desligar() # Agora deve desligar
meu_hb20.exibir_status()

minha_lander.ligar()
minha_lander.acelerar(90) # Deve mostrar a mensagem adicional
minha_lander.exibir_status()
minha_lander.frear(90)
minha_lander.desligar()
minha_lander.exibir_status()

"""
Explicação:
1.  `Veiculo` é a classe base com atributos e métodos comuns a todos os veículos.
2.  `Carro` e `Motocicleta` herdam de `Veiculo` usando `class NomeSubclasse(Veiculo):`.
3.  O construtor `__init__` das subclasses chama `super().__init__(...)` para
    garantir que o construtor da classe pai seja executado, inicializando os atributos herdados.
4.  As subclasses adicionam seus próprios atributos (`num_portas`, `cilindradas`).
5.  O método `exibir_status` é sobrescrito nas subclasses para incluir informações
    específicas, mas ainda reutiliza a funcionalidade da classe pai chamando
    `super().exibir_status()`.
6.  O método `acelerar` na `Motocicleta` também é sobrescrito para adicionar um comportamento
    especial, além de chamar a lógica base com `super().acelerar()`.
"""
