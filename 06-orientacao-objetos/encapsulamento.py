# 06-orientacao-objetos/encapsulamento.py

"""
Módulo de Demonstração: Encapsulamento em Python

Encapsulamento é o princípio de agrupar dados (atributos) e os métodos que
operam nesses dados dentro de uma única unidade (classe), e restringir o acesso
direto a alguns dos componentes internos do objeto [1, 2].
Em Python, isso é feito mais por convenção do que por imposição estrita.

Níveis de Acesso (Convenções):
- Público: Acessível de qualquer lugar (sem prefixo).
- Protegido: Prefixo de um underscore (`_atributo`). Indica que é para uso interno
  da classe ou subclasses, mas ainda pode ser acessado externamente (convenção) [5, 8].
- Privado: Prefixo de dois underscores (`__atributo`). Python realiza "name mangling"
  para `_NomeDaClasse__atributo`, tornando o acesso direto mais difícil, mas não impossível [1, 5, 7].
"""

print("--- Demonstração de Encapsulamento ---")

class Smartphone:
    """
    Classe para demonstrar encapsulamento, baseada no exemplo de DataCamp [1].
    """
    def __init__(self, marca, modelo, sistema_operacional):
        # Atributos públicos (por padrão)
        self.marca = marca
        self.modelo = modelo

        # Atributo "protegido" (convenção)
        self._numero_serie = f"{marca[:3].upper()}-{modelo[:2].upper()}-{abs(hash(sistema_operacional))%10000}"

        # Atributo "privado" (name mangling será aplicado)
        # Queremos controlar como o sistema operacional é definido.
        self.__sistema_operacional = None # Inicializa como None
        # Usaremos um setter para definir o valor inicial com validação
        self.set_sistema_operacional(sistema_operacional) # Chamando o setter no construtor

        self.__ligado = False # Outro atributo privado

    # --- Métodos Públicos ---
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print(f"{self.marca} {self.modelo} ligado. Rodando {self.__sistema_operacional}.")
            self.__autenticar_sistema() # Chamando um método privado interno
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print(f"{self.marca} {self.modelo} desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def exibir_status(self):
        status = "Ligado" if self.__ligado else "Desligado"
        print(f"Status: {self.marca} {self.modelo} está {status}.")
        if self.__ligado:
            print(f"Sistema Operacional: {self.__sistema_operacional}")

    # --- Métodos Privados (Convenção: para lógica interna) ---
    def __autenticar_sistema(self):
        """Simula uma autenticação interna do sistema."""
        # Este método não deve ser chamado de fora da classe.
        print(f"Sistema {self.__sistema_operacional} autenticado com sucesso em {self.modelo}.")

    # --- Getters e Setters Tradicionais (estilo Java/C#) para __sistema_operacional ---
    # Embora Python prefira propriedades (@property), é bom conhecer este estilo.
    def get_sistema_operacional(self):
        """Retorna o sistema operacional (getter)."""
        return self.__sistema_operacional

    def set_sistema_operacional(self, novo_so):
        """Define o sistema operacional com validação (setter)."""
        sistemas_validos = ["Android", "iOS", "KaiOS"]
        if novo_so in sistemas_validos:
            self.__sistema_operacional = novo_so
            print(f"Sistema operacional de {self.modelo} definido para {novo_so}.")
        else:
            # Ao invés de printar, em um sistema real, poderíamos levantar uma exceção.
            print(f"Erro: '{novo_so}' não é um sistema operacional válido para este smartphone.")
            # Se fosse um erro crítico no construtor, poderíamos levantar ValueError aqui.
            if self.__sistema_operacional is None: # Se ainda não tem SO válido
                 raise ValueError(f"Sistema operacional inicial '{novo_so}' inválido.")

# --- Demonstração com Smartphone ---
print("\n--- Usando a classe Smartphone ---")
try:
    meu_celular = Smartphone("TechBrand", "X100", "Android")
    meu_celular.ligar()
    meu_celular.exibir_status()
    print(f"SO atual (via getter): {meu_celular.get_sistema_operacional()}")

    # Tentativa de mudar o SO para um valor inválido usando o setter
    meu_celular.set_sistema_operacional("Windows Phone") # Deve dar erro na validação
    print(f"SO após tentativa inválida (via getter): {meu_celular.get_sistema_operacional()}")

    # Mudando para um SO válido
    meu_celular.set_sistema_operacional("iOS")
    print(f"SO após mudança válida (via getter): {meu_celular.get_sistema_operacional()}")
    meu_celular.desligar()

except ValueError as e:
    print(f"Erro ao criar smartphone: {e}")


# Acesso a atributo protegido (possível, mas não recomendado pela convenção)
print(f"\nNúmero de série (protegido): {meu_celular._numero_serie}")
meu_celular._numero_serie = "ALTERADO_EXTERNAMENTE" # Funciona, mas quebra o encapsulamento
print(f"Número de série alterado: {meu_celular._numero_serie}")


# Tentativa de acesso direto a atributo privado (resultará em AttributeError)
try:
    print(meu_celular.__sistema_operacional)
except AttributeError as e:
    print(f"\nErro ao tentar acessar __sistema_operacional diretamente: {e}")

# Acesso ao atributo "privado" usando o nome "mangled" (prova que não é realmente privado) [1]
# _NomeDaClasse__nomeAtributo
print(f"Acesso ao SO via 'name mangling': {meu_celular._Smartphone__sistema_operacional}")
meu_celular._Smartphone__ligado = True # Alterando estado interno, quebrando encapsulamento
print("Estado interno __ligado alterado externamente via name mangling.")
meu_celular.exibir_status() # Agora mostra Ligado, mesmo que não tenhamos chamado .ligar() corretamente.


# --- Classe com Propriedades (@property) ---
# Esta é a forma mais "Pythônica" de implementar getters, setters e deleters.
class ContaBancaria:
    """
    Demonstra encapsulamento com @property, @<attr>.setter, @<attr>.deleter [5, 6].
    """
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular # Atributo público
        # `_saldo` é o atributo interno "protegido" que armazena o valor real do saldo.
        # O setter da propriedade `saldo` será chamado aqui.
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self._saldo = saldo_inicial # Definindo diretamente o atributo interno pela primeira vez
                                    # ou podemos usar self.saldo = saldo_inicial (chamaria o setter)
        print(f"Conta criada para {self.titular} com saldo inicial de R${self._saldo:.2f}")

    # Getter para 'saldo'
    @property
    def saldo(self):
        """
        Propriedade 'saldo'. Este método é o getter.
        Chamado quando acessamos `conta.saldo`.
        """
        print(f"(Getter chamado para saldo de {self.titular})")
        return self._saldo

    # Setter para 'saldo'
    @saldo.setter
    def saldo(self, novo_valor):
        """
        Este método é o setter para a propriedade 'saldo'.
        Chamado quando tentamos atribuir um valor a `conta.saldo = valor`.
        """
        print(f"(Setter chamado para saldo de {self.titular} com valor {novo_valor})")
        if not isinstance(novo_valor, (int, float)):
            raise TypeError("O saldo deve ser um número.")
        if novo_valor < 0:
            raise ValueError("O saldo não pode ser definido como negativo diretamente.")
        self._saldo = novo_valor
        print(f"Saldo de {self.titular} atualizado para R${self._saldo:.2f}")

    # Deleter para 'saldo' (menos comum, mas demonstra o conceito)
    @saldo.deleter
    def saldo(self):
        """
        Este método é o deleter para a propriedade 'saldo'.
        Chamado quando usamos `del conta.saldo`.
        """
        print(f"(Deleter chamado para saldo de {self.titular})")
        print(f"Atenção: O saldo de {self.titular} está sendo zerado e a conta pode ser marcada para encerramento.")
        self._saldo = 0 # Ou outra lógica, como marcar a conta como inativa

    # Métodos públicos para operações bancárias
    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito deve ser positivo.")
            return False
        # Aqui usamos o setter implicitamente se self.saldo fosse usado,
        # ou acessamos o atributo interno diretamente para evitar a lógica do setter se não desejado.
        # Normalmente, para operações internas que modificam o estado, você pode querer
        # modificar o atributo interno diretamente se a lógica do setter não for apropriada
        # para essa operação específica (ex: setter tem validações para atribuição externa).
        # Mas se o setter contém lógica essencial, use-o: self.saldo += valor
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        return True

print("\n--- Usando a classe ContaBancaria com @property ---")
try:
    minha_conta = ContaBancaria("Ana Silva", 1000)

    # Acessando o saldo (chama o getter @property)
    print(f"Saldo atual da conta de {minha_conta.titular}: R${minha_conta.saldo:.2f}")

    # Tentando depositar e sacar
    minha_conta.depositar(500)
    minha_conta.sacar(200)
    minha_conta.sacar(2000) # Saldo insuficiente

    # Tentando definir o saldo diretamente (chama o setter @saldo.setter)
    minha_conta.saldo = 2000  # Isso chama o método @saldo.setter
    print(f"Saldo após atribuição direta: R${minha_conta.saldo:.2f}")

    # Tentativa de definir saldo negativo (deve falhar devido à validação no setter)
    try:
        minha_conta.saldo = -100
    except ValueError as e:
        print(f"Erro ao tentar definir saldo negativo: {e}")

    # Usando o deleter (chama @saldo.deleter)
    del minha_conta.saldo
    print(f"Saldo após 'del': R${minha_conta.saldo:.2f}")

except (ValueError, TypeError) as e:
    print(f"Erro ao manipular conta bancária: {e}")


print("\n--- Fim da Demonstração de Encapsulamento ---")

