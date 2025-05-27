# 06-orientacao-objetos/exercicios/04_conta_bancaria_encapsulada.py

"""
Exercício 4: Classe ContaBancaria com Encapsulamento

Objetivo: Desenvolver uma classe `ContaBancaria` com saldo encapsulado,
utilizando propriedades (getters e setters com @property) para controlar
o acesso e as modificações ao saldo, garantindo que ele não possa ser
negativo ou modificado indevidamente.
"""

class ContaBancaria:
    """
    Representa uma conta bancária com saldo encapsulado.
    Utiliza @property para getters e setters.
    """
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta  # Atributo público
        self.titular = titular            # Atributo público

        # Atributo interno "protegido" para o saldo.
        # A validação inicial do saldo é feita aqui.
        if not isinstance(saldo_inicial, (int, float)):
            raise TypeError("Saldo inicial deve ser um valor numérico.")
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self._saldo = saldo_inicial # O underscore indica que é "protegido"

        print(f"Conta {self.numero_conta} de {self.titular} criada com saldo R${self._saldo:.2f}.")

    # Getter para a propriedade 'saldo'
    @property
    def saldo(self):
        """Retorna o valor do saldo da conta."""
        # Poderia adicionar lógica aqui, como logging de acesso
        # print(f"(Acesso ao saldo de {self.titular})")
        return self._saldo

    # Setter para a propriedade 'saldo'
    # Este setter é intencionalmente restritivo para ilustrar controle.
    # Em um sistema real, o saldo seria alterado por métodos como depositar/sacar.
    @saldo.setter
    def saldo(self, novo_valor):
        """
        Permite a alteração do saldo, mas com restrições.
        Normalmente, o saldo não é definido diretamente assim, mas sim através
        de operações de depósito e saque. Este setter demonstra o controle.
        """
        print(f"[AVISO] Tentativa de alteração direta do saldo para R${novo_valor:.2f}.")
        if not isinstance(novo_valor, (int, float)):
            raise TypeError("O novo valor do saldo deve ser numérico.")
        if novo_valor < 0:
            print("Não é permitido definir um saldo negativo diretamente. Operação cancelada.")
            return # Impede a alteração
        
        # Em um cenário mais complexo, poderia haver uma verificação de permissão
        # ou registro de auditoria aqui antes de permitir a alteração direta.
        print("Alteração direta de saldo não é a prática padrão. Use depositar/sacar.")
        self._saldo = novo_valor


    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if not isinstance(valor, (int, float)):
            print("Erro: Valor de depósito deve ser numérico.")
            return False
        if valor <= 0:
            print("Erro: Valor de depósito deve ser positivo.")
            return False

        self._saldo += valor # Altera o atributo interno diretamente
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        return True

    def sacar(self, valor):
        """Realiza um saque da conta."""
        if not isinstance(valor, (int, float)):
            print("Erro: Valor de saque deve ser numérico.")
            return False
        if valor <= 0:
            print("Erro: Valor de saque deve ser positivo.")
            return False
        if valor > self._saldo: # Acessa o saldo interno para comparação
            print(f"Erro: Saldo insuficiente (R${self.saldo:.2f}) para sacar R${valor:.2f}.")
            return False

        self._saldo -= valor # Altera o atributo interno
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        return True

    def exibir_extrato(self):
        """Exibe o extrato simplificado da conta."""
        print(f"\n--- Extrato Conta {self.numero_conta} ---")
        print(f"Titular: {self.titular}")
        # Usa a propriedade @property saldo para buscar o valor
        print(f"Saldo Disponível: R${self.saldo:.2f}")


# --- Demonstração da Classe ContaBancaria ---
try:
    conta1 = ContaBancaria("12345-6", "João da Silva", 1500.00)
    conta2 = ContaBancaria("98765-4", "Maria Oliveira") # Saldo inicial padrão 0.0

    conta1.exibir_extrato()
    conta2.exibir_extrato()

    print("\n--- Operações na Conta de João ---")
    conta1.depositar(500.75)
    conta1.sacar(300.25)
    conta1.sacar(2000.00) # Tentativa de saque maior que o saldo

    print("\n--- Operações na Conta de Maria ---")
    conta2.depositar(1000)
    conta2.depositar(-50) # Depósito inválido
    conta2.sacar(0)     # Saque inválido

    # Acessando o saldo através da propriedade (chama o getter)
    print(f"\nSaldo de João (via propriedade): R${conta1.saldo:.2f}")

    # Tentando definir o saldo diretamente (chama o setter)
    print("\n--- Tentando alterar saldo diretamente ---")
    try:
        conta1.saldo = 50.00 # O setter deve emitir um aviso ou impedir
        conta1.exibir_extrato()
        conta1.saldo = -200.00 # O setter deve impedir
        conta1.exibir_extrato()
    except (ValueError, TypeError) as e_setter:
        print(f"Erro ao tentar usar o setter: {e_setter}")


    # Tentando criar conta com saldo inicial inválido
    print("\n--- Tentando criar conta com saldo inicial inválido ---")
    try:
        conta_invalida = ContaBancaria("00000-0", "Teste Inválido", -100)
    except ValueError as e:
        print(f"Erro ao criar conta: {e}")

    # Tentando acessar o atributo _saldo diretamente (possível, mas quebra encapsulamento)
    print("\n--- Acesso direto ao atributo _saldo (não recomendado) ---")
    print(f"Saldo interno de João (antes): R${conta1._saldo:.2f}")
    conta1._saldo = -5000.00 # Modificando diretamente, burlando validações dos métodos
    print(f"Saldo interno de João (depois da alteração direta e indevida): R${conta1._saldo:.2f}")
    conta1.exibir_extrato() # O extrato refletirá o saldo negativo

except (ValueError, TypeError) as e_main:
    print(f"Ocorreu um erro principal: {e_main}")


"""
Explicação:
1.  A classe `ContaBancaria` possui atributos públicos (`numero_conta`, `titular`)
    e um atributo "protegido" (`_saldo`) para armazenar o saldo.
2.  A propriedade `@property def saldo(self):` atua como um getter. Quando
    acessamos `objeto_conta.saldo`, este método é chamado.
3.  O método `@saldo.setter def saldo(self, novo_valor):` atua como um setter.
    Quando tentamos atribuir um valor (`objeto_conta.saldo = X`), este método
    é chamado, permitindo validações. No exemplo, ele emite avisos e impede
    a definição de saldos negativos diretamente.
4.  Os métodos `depositar` e `sacar` manipulam `self._saldo` diretamente, mas
    incluem suas próprias validações, que são a forma correta de alterar o saldo.
5.  O exemplo demonstra como as propriedades fornecem uma interface controlada
    para o atributo `_saldo`, mesmo que o acesso direto a `_saldo` ainda seja
    tecnicamente possível em Python (reforçando que encapsulamento é uma convenção
    forte, mas não uma barreira intransponível como em algumas outras linguagens).
"""
# Fim do código