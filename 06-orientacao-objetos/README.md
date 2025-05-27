# 🧱 Módulo 6: Programação Orientada a Objetos (POO) em Python

Bem-vindo ao Módulo 6, onde exploraremos os conceitos e práticas da Programação Orientada a Objetos (POO) utilizando Python. A POO é um paradigma de programação que organiza o código em torno de "objetos", que podem conter tanto dados (atributos) quanto código (métodos). Este módulo cobrirá os quatro pilares da POO: **Encapsulamento**, **Herança**, **Polimorfismo** e **Abstração**.

---

## 🎯 Objetivos de Aprendizagem

Ao final deste módulo, você será capaz de:

* Compreender e definir classes e instanciar objetos em Python.
* 🛠️ Utilizar construtores (`__init__`) para inicializar objetos com atributos de instância.
* 🔍 Diferenciar entre atributos de instância e atributos de classe.
* ⚙️ Implementar métodos de instância, métodos de classe (`@classmethod`) e métodos estáticos (`@staticmethod`).
* 🛡️ Aplicar o princípio do **Encapsulamento** para proteger os dados de uma classe, utilizando convenções para atributos públicos, protegidos (`_`) e privados (`__`).
* Property Usar propriedades (getters, setters, deleters com `@property`) para controlar o acesso e a modificação de atributos encapsulados.
* 🔗 Implementar a **Herança** para criar hierarquias de classes, reutilizar código e estender funcionalidades.
* ⬆️ Utilizar `super()` para chamar métodos da classe pai de forma eficaz.
* 🎭 Entender e aplicar o **Polimorfismo**, permitindo que objetos de diferentes classes respondam a uma mesma interface de métodos (Duck Typing).
* 🧩 Compreender o conceito de **Abstração** na modelagem de classes, focando nos aspectos essenciais e ocultando a complexidade desnecessária.
* 💡 Resolver problemas práticos modelando soluções com os princípios da POO.

---

## 📚 Conteúdo Abordado

Este módulo mergulha nos seguintes tópicos da Programação Orientada a Objetos:

* **Classes e Objetos:**
    * Definição de classes: o blueprint para criar objetos.
    * Instanciação de objetos: criando instâncias de uma classe.
    * O método construtor `__init__` e o parâmetro `self`.
    * Atributos de instância (específicos de cada objeto) vs. atributos de classe (compartilhados por todas as instâncias).
    * Tipos de Métodos:
        * Métodos de instância: operam em uma instância específica (`self`).
        * Métodos de classe (`@classmethod`): operam na classe em si (`cls`).
        * Métodos estáticos (`@staticmethod`): funções utilitárias relacionadas à classe, sem acesso direto a `self` ou `cls`.
    * Demonstrações em `exemplos/classes_objetos.py`.

* **Encapsulamento:**
    * O princípio de agrupar dados (atributos) e os métodos que os manipulam dentro de uma unidade (classe), protegendo os dados de acesso externo direto e não intencional.
    * Níveis de acesso em Python (convenções):
        * **Público:** Atributos e métodos acessíveis de qualquer lugar (sem prefixo).
        * **Protegido:** Atributos e métodos prefixados com um underscore (`_nome_protegido`), indicando que são para uso interno ou por subclasses (convenção, não imposto pela linguagem).
        * **Privado:** Atributos e métodos prefixados com dois underscores (`__nome_privado`), que sofrem "name mangling" (ex: `_NomeDaClasse__nome_privado`), dificultando o acesso externo direto (maior nível de proteção por convenção).
    * Uso de **propriedades (`@property`, `@nome.setter`, `@nome.deleter`)** para fornecer acesso controlado aos atributos.
    * Demonstrações em `exemplos/encapsulamento.py`.

* **Herança:**
    * O mecanismo pelo qual uma classe (subclasse ou classe derivada) pode herdar atributos e métodos de outra classe (superclasse ou classe base).
    * Benefícios: reutilização de código e criação de hierarquias de especialização.
    * Tipos: Herança simples e herança múltipla (e o Method Resolution Order - MRO).
    * **Sobrescrita de Métodos (Method Overriding):** Uma subclasse redefine um método herdado da superclasse.
    * A função `super()` para chamar construtores e métodos da(s) classe(s) pai(s).
    * Demonstrações em `exemplos/heranca.py`.

* **Polimorfismo:**
    * A capacidade de objetos de diferentes classes serem tratados através de uma interface comum, respondendo de maneiras específicas às mesmas chamadas de métodos.
    * Em Python, o polimorfismo é frequentemente alcançado através do **"Duck Typing"**: "Se anda como um pato e grasna como um pato, então deve ser um pato." (Foco no comportamento, não na herança explícita).
    * Demonstrações em `exemplos/polimorfismo.py`.

* **Abstração:**
    * O processo de ocultar os detalhes complexos de implementação e expor apenas as funcionalidades essenciais ao usuário.
    * As classes, por si só, são uma forma de abstração.
    * Foco no "o quê" um objeto faz, em vez do "como" ele faz. Este conceito é aplicado em conjunto com os outros pilares.

---

## 🛠️ Exercícios Práticos

Para aplicar os conceitos de POO, desenvolvemos os seguintes exercícios:

1.  📖 **`exercicios/01_classe_livro.py`**:
    * Criação de uma classe `Livro` com atributos básicos (título, autor, páginas) e métodos para exibir suas informações.
2.  🚗 **`exercicios/02_sistema_veiculos_heranca.py`**:
    * Modelagem de um sistema com uma classe base `Veiculo` e subclasses como `Carro` e `Motocicleta`, demonstrando herança, atributos específicos e sobrescrita de métodos (ex: `descrever()`).
3.  🎨 **`exercicios/03_formas_geometricas_polimorfismo.py`**:
    * Implementação de diferentes classes de formas geométricas (ex: `Retangulo`, `Circulo`, `Triangulo`) com um método comum `calcular_area()`, demonstrando polimorfismo ao chamar este método em uma lista de formas diversas.
4.  🏦 **`exercicios/04_conta_bancaria_encapsulada.py`**:
    * Desenvolvimento de uma classe `ContaBancaria` com saldo encapsulado (privado), utilizando propriedades (getters e setters) para controlar as operações de depósito, saque e consulta de saldo.

---

Consulte os arquivos Python de exemplo (`exemplos/`) e os exercícios (`exercicios/`) para uma imersão prática nos conceitos da Programação Orientada a Objetos!