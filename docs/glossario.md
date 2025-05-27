# 📖 Glossário de Termos Técnicos Essenciais

Este glossário define termos chave utilizados ao longo do curso de Lógica de Programação com Python, desenvolvimento de software e metodologias ágeis. Ele serve como um guia de referência rápida para consolidar seu entendimento.

---

## 🅰️ A

* **Abstração:**
    O processo de ocultar detalhes complexos de implementação, expondo apenas as funcionalidades essenciais. Um dos pilares da Programação Orientada a Objetos (POO).

* **Algoritmo:**
    Uma sequência finita, bem definida e ordenada de instruções ou regras lógicas para resolver um problema específico ou realizar uma tarefa.

* **Argumento:**
    Um valor que é passado para uma função ou método quando este é invocado (chamado).

* **Array (Vetor):**
    Uma estrutura de dados que armazena uma coleção de elementos, tipicamente do mesmo tipo, em posições de memória contíguas, acessíveis por um índice numérico. Em Python, listas (`list`) são frequentemente usadas de forma similar, mas são mais flexíveis. Para arrays no sentido mais estrito (tipo fixo, memória contígua otimizada), utiliza-se o módulo `array` ou bibliotecas como NumPy.

* **Atributo (POO):**
    Uma variável associada a um objeto (instância) ou a uma classe, que armazena dados (características ou estado). Pode ser um *atributo de instância* (específico do objeto) ou um *atributo de classe* (compartilhado por todas as instâncias da classe).

* **Atribuição:**
    O ato de dar ou associar um valor a uma variável (ex: `idade = 30`).

## 🅱️ B

* **Backlog (Product Backlog / Sprint Backlog - Scrum):**
    Uma lista priorizada de trabalho a ser feito. O *Product Backlog* é uma lista dinâmica de todos os requisitos, funcionalidades e melhorias para um produto. O *Sprint Backlog* contém as tarefas e itens do Product Backlog selecionados para serem realizados durante uma Sprint específica.

* **Big O Notation (Notação Big O):**
    Uma notação matemática usada para descrever a complexidade assintótica (o limite superior do comportamento) de algoritmos em termos de tempo de execução ou uso de espaço de memória, à medida que o tamanho da entrada do algoritmo cresce.

* **Booleano (`bool`):**
    Um tipo de dado fundamental que pode ter apenas dois valores possíveis: Verdadeiro (`True`) ou Falso (`False`). Usado para representar valores lógicos e em operações condicionais.

* **Branch (Git):**
    Uma linha independente de desenvolvimento dentro de um repositório Git. Permite que desenvolvedores trabalhem em diferentes funcionalidades, correções ou experimentos de forma isolada, sem afetar a linha principal de desenvolvimento (comumente chamada de `main` ou `master`) até que as alterações sejam mescladas (merge).

* **`break`:**
    Uma instrução de controle em programação que interrompe imediatamente a execução do laço (loop) mais interno em que se encontra (seja `for` ou `while`).

* **Bug:**
    Um erro, falha ou defeito em um programa de computador que faz com que ele produza um resultado incorreto, inesperado, ou se comporte de maneira não intencional.

## ©️ C

* **Classe (POO):**
    Um modelo, blueprint ou molde para criar objetos. Define um conjunto de atributos (dados) e métodos (comportamentos) que os objetos criados a partir dela (instâncias) terão.

* **Commit (Git):**
    Uma "fotografia" ou um instantâneo das alterações feitas nos arquivos de um projeto em um determinado momento. Cada commit é armazenado no histórico do repositório Git com uma mensagem descritiva.

* **Compilação:**
    O processo de traduzir código-fonte escrito em uma linguagem de programação de alto nível (compreensível por humanos) para uma linguagem de baixo nível (como código de máquina ou bytecode) que o computador pode executar diretamente ou através de uma máquina virtual. Python é primariamente uma linguagem interpretada, mas o código fonte é primeiro compilado para bytecode (`.pyc`), que é então executado pelo interpretador Python.

* **Complexidade de Algoritmo:**
    Uma medida de quantos recursos (principalmente tempo de processamento ou espaço de memória) um algoritmo consome em relação ao tamanho de sua entrada de dados.

* **Condicional (Estrutura de Decisão):**
    Uma estrutura de programação (como `if`, `elif`, `else`) que permite que diferentes blocos de código sejam executados com base em uma ou mais condições serem verdadeiras ou falsas.

* **Constante:**
    Um valor que, uma vez definido, não deve ser alterado durante a execução do programa. Em Python, a criação de constantes é uma convenção, geralmente indicando-as com nomes em letras MAIÚSCULAS (ex: `TAXA_DE_JUROS = 0.05`).

* **Construtor (POO):**
    Um método especial dentro de uma classe (em Python, nomeado `__init__`) que é chamado automaticamente quando um novo objeto (instância) dessa classe é criado. É usado principalmente para inicializar os atributos do objeto.

* **`continue`:**
    Uma instrução de controle que interrompe a iteração atual de um laço (loop `for` ou `while`) e passa imediatamente para a próxima iteração do laço, ignorando o restante do código no bloco da iteração atual.

## 💎 D

* **Daily Scrum (Scrum):**
    Uma reunião diária curta e time-boxed (geralmente 15 minutos) para o Time de Desenvolvimento sincronizar atividades, inspecionar o progresso em direção à Meta da Sprint e adaptar o Sprint Backlog conforme necessário.

* **Debugging (Depuração):**
    O processo sistemático de encontrar, diagnosticar e corrigir bugs (erros) em um programa de computador.

* **Decomposição:**
    A técnica de dividir um problema complexo ou um sistema em partes menores, mais simples e mais gerenciáveis, facilitando a análise, o desenvolvimento e a manutenção.

* **Definition of Done (DoD - Scrum):**
    Um entendimento compartilhado e formalizado pelo Time Scrum sobre todos os critérios que um item do Product Backlog deve atender para ser considerado completo e potencialmente liberável. Garante a qualidade e a transparência do Incremento.

* **Dicionário (`dict` - Python):**
    Uma estrutura de dados embutida em Python que armazena uma coleção de pares chave-valor. As chaves devem ser únicas e imutáveis, e são usadas para acessar os valores correspondentes de forma eficiente.

* **Duck Typing:**
    Um conceito em linguagens dinamicamente tipadas como Python, onde o tipo ou a classe de um objeto é menos importante do que os métodos que ele define e os comportamentos que ele exibe. A ideia é: "Se anda como um pato e grasna como um pato, então deve ser um pato." O foco está na interface (métodos e propriedades) que um objeto suporta, não em sua herança.

## 💅 E

* **Encapsulamento (POO):**
    Um dos pilares da Programação Orientada a Objetos. É o princípio de agrupar dados (atributos) e os métodos que os manipulam dentro de uma unidade coesa (a classe), e restringir o acesso direto a alguns dos componentes internos do objeto, protegendo seus dados e expondo apenas o necessário através de uma interface pública.

* **Estrutura de Dados:**
    Uma forma particular de organizar, gerenciar e armazenar dados em um computador para que possam ser acessados e modificados eficientemente. Exemplos incluem listas, dicionários, tuplas, pilhas, filas, árvores, grafos, etc.

* **Estrutura de Repetição (Laço/Loop):**
    Uma estrutura de programação (como `for` ou `while`) que permite que um bloco de código seja executado repetidamente enquanto uma determinada condição for satisfeita ou por um número específico de vezes.

## 🎏 F

* **FIFO (First-In, First-Out):**
    "Primeiro a Entrar, Primeiro a Sair". Um princípio de processamento de dados onde o primeiro item a ser adicionado a uma estrutura é o primeiro a ser removido. Característico de uma **Fila**.

* **Fluxograma:**
    Uma representação gráfica de um algoritmo, processo ou fluxo de trabalho, usando símbolos padronizados para ilustrar a sequência de etapas, decisões, entradas e saídas.

* **Framework:**
    Um conjunto de ferramentas, bibliotecas, padrões e convenções que fornece uma estrutura ou esqueleto para desenvolver aplicações de software. Desenvolvedores constroem suas aplicações "em cima" de um framework, que dita a arquitetura geral. (Ex: Scrum é um framework ágil; Django e Flask são frameworks web em Python).

* **Função:**
    Um bloco de código nomeado e reutilizável que realiza uma tarefa específica. Funções podem receber dados de entrada (argumentos/parâmetros) e podem retornar um valor de saída. Ajudam a organizar e modularizar o código.

## ⛽ G

* **Getter (POO):**
    Um método usado para obter (ler) o valor de um atributo encapsulado (geralmente privado ou protegido) de um objeto. Em Python, frequentemente implementado usando o decorador `@property`.

* **Git:**
    Um sistema de controle de versão distribuído, amplamente utilizado para rastrear alterações no código-fonte durante o desenvolvimento de software. Permite que múltiplos desenvolvedores colaborem em um projeto.

* **GitHub:**
    Uma plataforma baseada na web para hospedagem de repositórios Git. Oferece funcionalidades de colaboração, como rastreamento de issues, pull requests, gerenciamento de projetos e integração contínua.

## 🛏 H

* **Herança (POO):**
    Um mecanismo fundamental da Programação Orientada a Objetos pelo qual uma classe (subclasse ou classe derivada) pode herdar atributos e métodos de outra classe (superclasse ou classe base). Promove a reutilização de código e a criação de hierarquias de classes ("é um" relacionamento).

## ℹ️ I

* **IDE (Integrated Development Environment - Ambiente de Desenvolvimento Integrado):**
    Um software aplicativo que fornece um ambiente abrangente para desenvolvedores de software criarem programas. Geralmente inclui um editor de código-fonte, ferramentas de automação de build, um depurador (debugger) e, às vezes, um compilador ou interpretador. (Ex: VS Code, PyCharm, Spyder).

* **Imutável:**
    Um objeto cujo estado (valor interno) não pode ser modificado após sua criação. Se uma operação parece modificar um objeto imutável, ela na verdade cria um novo objeto com o novo valor. (Ex: números, strings e tuplas em Python são imutáveis).

* **Incremento (Scrum):**
    A soma de todos os itens do Product Backlog completados durante uma Sprint e o valor dos incrementos de todas as Sprints anteriores. Para fornecer valor, o Incremento deve ser utilizável e atender à Definition of Done.

* **Índice (Index):**
    Um valor numérico (geralmente começando em 0 em muitas linguagens, incluindo Python) que indica a posição de um elemento dentro de uma sequência ordenada (como uma lista, string ou tupla).

* **Instância (POO):**
    Um objeto específico criado a partir de uma classe. É uma concretização da classe, com seus próprios valores para os atributos definidos pela classe.

* **Interpretação:**
    O processo de executar código-fonte diretamente, traduzindo-o instrução por instrução ou em pequenos blocos, geralmente sem uma etapa de compilação prévia para código de máquina nativo. Python é uma linguagem que utiliza um interpretador.

* **Iteração:**
    Uma única execução do bloco de código dentro de um laço (loop). Também se refere a um ciclo de desenvolvimento em metodologias ágeis (como uma Sprint no Scrum), onde um conjunto de atividades é repetido para produzir um incremento de produto.

## 🛴 L

* **LIFO (Last-In, First-Out):**
    "Último a Entrar, Primeiro a Sair". Um princípio de processamento de dados onde o último item a ser adicionado a uma estrutura é o primeiro a ser removido. Característico de uma **Pilha (Stack)**.

* **Lista (`list` - Python):**
    Uma estrutura de dados embutida em Python, ordenada e mutável, que pode conter uma coleção de itens, inclusive de tipos diferentes (heterogêneos).

* **Lógica de Programação:**
    A organização coerente e estruturada de instruções, dados e estruturas de controle para que um programa de computador execute uma tarefa desejada corretamente e de forma eficiente. Envolve a habilidade de pensar de forma algorítmica.

## Ⓜ️ M

* **Manifesto Ágil:**
    Um documento fundamental, criado em 2001, que estabelece os 4 valores e os 12 princípios que guiam as metodologias ágeis de desenvolvimento de software.

* **Merge (Git):**
    O ato de integrar (combinar) alterações de diferentes branches em uma única branch. O Git tenta mesclar automaticamente as alterações, mas pode requerer intervenção manual para resolver conflitos.

* **Método (POO):**
    Uma função que está associada a um objeto ou a uma classe. Métodos definem os comportamentos dos objetos.

* **Metodologias Ágeis:**
    Um conjunto de abordagens e práticas para o desenvolvimento de software que valoriza a entrega incremental e frequente, a colaboração próxima com o cliente, a adaptação a mudanças e o foco nas pessoas e interações.

* **Módulo (Python):**
    Um arquivo contendo definições e instruções Python (variáveis, funções, classes). Permite organizar o código de forma lógica e reutilizável, podendo ser importado em outros scripts ou módulos.

* **Mutável:**
    Um objeto cujo estado (valor interno) pode ser modificado após sua criação. (Ex: listas e dicionários em Python são mutáveis).

## ♑ N

* **NumPy:**
    Uma biblioteca fundamental para computação científica e numérica em Python. Fornece suporte para arrays e matrizes multidimensionais de alta performance, juntamente com uma vasta coleção de funções matemáticas para operar nesses arrays.

## 🅾️ O

* **Objeto (POO):**
    Uma instância de uma classe. Na Programação Orientada a Objetos, um objeto representa uma entidade do mundo real ou um conceito abstrato, possuindo estado (definido por seus atributos) e comportamento (definido por seus métodos).

* **Operador:**
    Um símbolo especial ou palavra-chave que realiza uma operação em um ou mais operandos (valores ou variáveis). (Ex: operadores aritméticos como `+`, `-`, `*`, `/`; operadores de comparação como `==`, `!=`, `>`; operadores lógicos como `and`, `or`, `not`).

## 🅿️ P

* **Parâmetro:**
    Uma variável nomeada na definição de uma função ou método. Atua como um placeholder que receberá um valor (o argumento) quando a função/método for chamado.

* **Pilha (Stack):**
    Uma estrutura de dados abstrata que segue o princípio LIFO (Last-In, First-Out). As operações principais são `push` (adicionar um item ao topo) e `pop` (remover o item do topo).

* **Polimorfismo (POO):**
    "Muitas formas". Um dos pilares da Programação Orientada a Objetos. É a capacidade de objetos de diferentes classes responderem à mesma mensagem (chamada de método) de maneiras específicas, de acordo com sua própria implementação. Em Python, o Duck Typing é uma forma comum de polimorfismo.

* **Product Owner (PO - Scrum):**
    O papel no Time Scrum responsável por maximizar o valor do produto resultante do trabalho da equipe. Gerencia e prioriza o Product Backlog, representando os interesses dos stakeholders.

* **Propriedade (POO - Python):**
    Um mecanismo em Python (usando o decorador `@property` e, opcionalmente, `@<nome>.setter` e `@<nome>.deleter`) para fornecer acesso controlado a atributos de um objeto. Permite implementar getters, setters e deleters de uma forma considerada "Pythônica", tratando o acesso a atributos como se fossem atributos públicos, mas com lógica por trás.

* **Pseudocódigo:**
    Uma descrição informal de alto nível do princípio operacional de um programa de computador ou outro algoritmo. Utiliza convenções estruturais de linguagens de programação, mas é escrito em linguagem natural e é destinado à leitura humana em vez de execução por máquina.

* **Pull Request (PR - GitHub/GitLab etc.):**
    Uma proposta formal para mesclar (merge) um conjunto de alterações de uma branch para outra em um repositório hospedado (como no GitHub). Permite que outros desenvolvedores revisem o código, discutam as alterações e aprovem a integração.

* **Python:**
    Uma linguagem de programação de alto nível, interpretada, interativa e orientada a objetos, conhecida por sua sintaxe clara, legibilidade e vasta quantidade de bibliotecas.

## ®️ R

* **Recursão:**
    Uma técnica de programação onde uma função chama a si mesma para resolver um problema. A recursão geralmente quebra o problema em subproblemas menores e idênticos (ou muito similares) até atingir um caso base que pode ser resolvido diretamente.

* **Repositório (Git):**
    Um local (geralmente uma pasta no sistema de arquivos) onde todos os arquivos, o histórico de alterações e os metadados de um projeto gerenciado pelo Git são armazenados. Pode ser local ou remoto.

* **Retrospectiva da Sprint (Scrum):**
    Um evento que ocorre ao final de cada Sprint, onde o Time Scrum inspeciona seu próprio processo de trabalho e colaboração, identifica o que funcionou bem, o que pode ser melhorado, e cria um plano para implementar essas melhorias na próxima Sprint.

## 💰 S

* **Scrum:**
    Um framework ágil para desenvolver, entregar e sustentar produtos complexos. Baseia-se em ciclos iterativos e incrementais (Sprints), com papéis, eventos e artefatos definidos.

* **Scrum Master (SM - Scrum):**
    O papel no Time Scrum responsável por garantir que o Scrum seja entendido e adotado corretamente. Ajuda a remover impedimentos, facilita os eventos do Scrum e atua como um coach para a equipe e a organização em práticas ágeis.

* **`self` (POO - Python):**
    Uma referência convencional ao próprio objeto (instância) dentro dos métodos de uma classe em Python. É o primeiro parâmetro da maioria dos métodos de instância e é passado automaticamente quando o método é chamado em um objeto.

* **Sequência:**
    Uma estrutura de dados ordenada, onde os elementos são armazenados em uma ordem específica e podem ser acessados por um índice numérico. (Ex: listas, tuplas e strings em Python são tipos de sequência).

* **Setter (POO):**
    Um método usado para definir ou modificar o valor de um atributo encapsulado de um objeto, frequentemente incluindo lógica de validação ou outras ações. Em Python, implementado com o decorador `@<nome_propriedade>.setter` quando se usa propriedades.

* **Sprint (Scrum):**
    Um ciclo de desenvolvimento time-boxed (com duração fixa, geralmente de 1 a 4 semanas) durante o qual um Incremento de produto "Feito", utilizável e potencialmente liberável é criado. É o coração do Scrum.

* **Sprint Goal (Meta da Sprint - Scrum):**
    O objetivo único para a Sprint, definido pelo Time Scrum durante o Planejamento da Sprint. Fornece foco e direção para o trabalho da Sprint.

* **Sprint Planning (Planejamento da Sprint - Scrum):**
    O evento no início da Sprint onde o Time Scrum colabora para planejar o trabalho a ser realizado durante a Sprint, definindo a Meta da Sprint e selecionando os itens do Product Backlog que comporão o Sprint Backlog.

* **Sprint Review (Revisão da Sprint - Scrum):**
    Um evento informal que ocorre ao final da Sprint para inspecionar o Incremento do produto e adaptar o Product Backlog, se necessário. O Time Scrum demonstra o trabalho "Feito" aos stakeholders e discute o progresso.

* **String (`str` - Python):**
    Uma sequência imutável de caracteres Unicode, usada para representar dados textuais em Python.

* **Subclasse (POO):**
    Uma classe que herda atributos e métodos de outra classe (a superclasse). Também chamada de classe filha ou classe derivada.

* **`super()` (POO - Python):**
    Uma função embutida em Python usada para chamar métodos de uma classe pai (superclasse) a partir de uma subclasse. É útil para estender ou modificar o comportamento herdado, especialmente em construtores (`__init__`) e métodos sobrescritos.

* **Superclasse (POO):**
    Uma classe da qual outra classe (a subclasse) herda. Também chamada de classe pai ou classe base.

## 🌴 T

* **Tag (Git):**
    Um marcador ou rótulo usado para identificar um commit específico no histórico do Git. Frequentemente usado para marcar versões de lançamento de um software (ex: `v1.0.0`, `v2.1-beta`).

* **Teste de Mesa (Desk Checking):**
    Uma técnica manual e informal para verificar a lógica de um algoritmo ou trecho de código. Consiste em simular a execução do algoritmo passo a passo, acompanhando os valores das variáveis com dados de exemplo, para identificar erros lógicos.

* **Tipagem Dinâmica:**
    Um sistema de tipos em linguagens de programação onde o tipo de uma variável é verificado durante a execução do programa (runtime), não em tempo de compilação. Em linguagens dinamicamente tipadas como Python, uma variável pode referenciar objetos de diferentes tipos ao longo de sua vida.

* **Tupla (`tuple` - Python):**
    Uma estrutura de dados embutida em Python, ordenada e imutável, que pode conter uma coleção de itens, inclusive de tipos diferentes. Uma vez criada, uma tupla não pode ser alterada.

## ♈ V

* **Variável:**
    Um nome simbólico associado a um valor armazenado na memória do computador. O valor de uma variável pode ser alterado durante a execução do programa (a menos que seja uma constante por convenção ou natureza).

* **Versionamento de Código (Controle de Versão):**
    Um sistema que registra alterações em um arquivo ou conjunto de arquivos ao longo do tempo, para que versões específicas possam ser recuperadas posteriormente. Ajuda a gerenciar o histórico do projeto, facilitar a colaboração e reverter para estados anteriores. (Ex: Git).

## 〰️ W

* **`while` (Laço):**
    Uma estrutura de repetição (loop) que executa um bloco de código repetidamente enquanto uma condição especificada continuar sendo verdadeira. A condição é testada antes de cada iteração.

---

✨ Este glossário é uma ferramenta viva! Consulte-o sempre que encontrar um termo que precise ser relembrado.