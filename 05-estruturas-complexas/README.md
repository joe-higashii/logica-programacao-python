# 🏗️ Módulo 05: Estruturas de Dados Complexas

---

## 🎯 Objetivos de Aprendizagem:

Ao final deste módulo, você será capaz de:

-   Advanced Operar com **listas** e **tuplas** de forma avançada, incluindo compreensões e métodos específicos.
-   Implementar sistemas utilizando **dicionários aninhados** para representar dados relacionais.
-   Manipular **arrays** e **matrizes** eficientemente com a biblioteca **NumPy**.
-   Construir e aplicar estruturas de dados **LIFO** (Last-In, First-Out) como **pilhas** (stacks) e **FIFO** (First-In, First-Out) como **filas** (queues).
-   Analisar a **complexidade algorítmica** básica (Big O notation) das operações em diferentes estruturas de dados.

---

## 📚 Conteúdo Principal:

1.  **Listas (`list`) - Mutáveis**
    * Operações com complexidade `O(1)` (tempo constante) vs. `O(n)` (tempo linear).
    * **List Comprehensions**: Sintaxe concisa para criar listas.
    * Métodos importantes: `sort()`, `append()`, `insert()`, `remove()`, `pop()`, `copy()`, `index()`, `count()`.

2.  **Tuplas (`tuple`) - Imutáveis**
    * Uso como chaves em **dicionários** (devido à imutabilidade).
    * **Desempacotamento** de tuplas em variáveis.
    * **Named Tuples** (`collections.namedtuple`): Tuplas com campos nomeados para maior clareza.

3.  **Dicionários (`dict`)**
    * Tratamento de **colisões de hash** (conceito fundamental, gerenciado internamente).
    * Métodos úteis: `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`.
    * **Dicionários aninhados**: Estruturação de dados complexos.

4.  **Arrays e Matrizes com NumPy**
    * Diferenças cruciais entre **listas** Python e **arrays NumPy** (tipagem homogênea, eficiência).
    * **Operações vetorizadas**: Cálculos rápidos em arrays inteiros sem loops explícitos.
    * Fundamentos de álgebra linear: criação de matrizes, operações básicas (soma, multiplicação).

5.  **Pilhas (Stacks) e Filas (Queues)**
    * Implementação usando **listas** Python (pilhas: `append()` e `pop()`; filas: `append()` e `pop(0)` - menos eficiente).
    * Uso de `collections.deque` para implementações eficientes de pilhas e filas.
    * Cenários de aplicação: histórico de navegação (pilha), buffer de dados (fila), gerenciamento de tarefas.
    * Análise de desempenho das operações (`push`, `pop`, `enqueue`, `dequeue`).

---

## 🛠️ Exercícios Práticos:

-   📦 **Sistema de Estoque Simples:** Utilização de tuplas para representar itens de estoque (imutáveis) e listas ou dicionários para gerenciar o estoque.
-   📇 **Agenda de Contatos Avançada:** Implementação com dicionários aninhados para armazenar múltiplos detalhes por contato.
-   📈 **Cálculos Matriciais Básicos:** Uso de NumPy para realizar operações em matrizes, como a soma ou multiplicação, simulando cenários como transformações em gráficos.
-   🏦 **Simulação de Fila de Atendimento:** Criação de uma fila para simular a chegada e o atendimento de clientes em um banco, utilizando `collections.deque`.

---