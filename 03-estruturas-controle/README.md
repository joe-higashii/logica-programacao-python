# 🧱 Módulo 3: Estruturas de Controle

Bem-vindo ao Módulo 3! Aqui, vamos mergulhar nas estruturas que permitem controlar o fluxo de execução dos nossos programas. Compreender e utilizar corretamente as estruturas de sequência, decisão e repetição é crucial para construir algoritmos mais complexos e funcionais.

---

## 🎯 Objetivos de Aprendizagem

Ao final deste módulo, você será capaz de:

-   ➡️ Entender e aplicar a estrutura sequencial na construção de algoritmos.
-   ❓ Implementar estruturas de decisão (`Se-Então-Senão` / `if-elif-else`) para criar diferentes caminhos de execução baseados em condições.
-   🔄 Utilizar estruturas de repetição (`Para` / `for`, `Enquanto` / `while`) para executar blocos de código múltiplas vezes.
-   🚧 Empregar comandos de desvio como `break` e `continue` para controlar laços de repetição.
-   🧩 Resolver problemas práticos utilizando a combinação adequada dessas estruturas.

---

## 📚 Conteúdo Abordado

Este módulo explora os seguintes tópicos, fundamentais para a lógica de programação:

* **Estrutura Sequencial:**
    * A execução de instruções uma após a outra, na ordem em que aparecem no código.
    * Demonstração em `exemplos/sequencia.py`.

* **Estruturas de Decisão (Condicionais):**
    * **`Se-Então` (Simples):** Executa um bloco de código se uma condição for verdadeira.
        * Python: `if condicao:`
    * **`Se-Então-Senão` (Composta):** Executa um bloco se a condição for verdadeira, e outro bloco se for falsa.
        * Python: `if condicao: ... else: ...`
    * **`Se-Aninhado` e `Seleção Múltipla` (Encadeada):** Permite testar múltiplas condições.
        * Python: `if condicao1: ... elif condicao2: ... else: ...`
    * Demonstrações em `exemplos/decisao.py`.

* **Estruturas de Repetição (Laços ou Loops):**
    * **`Para` (Contador Definido):** Executa um bloco de código um número específico de vezes.
        * Python: `for item in iteravel:` ou `for i in range(inicio, fim, passo):`
    * **`Enquanto` (Teste no Início):** Executa um bloco de código enquanto uma condição for verdadeira, testada antes de cada iteração.
        * Python: `while condicao:`
    * **(Menção a `Repita-Até` - Teste no Final):** Executa um bloco e depois testa a condição. (Python não possui uma estrutura direta, mas pode ser simulada com `while True:` e `if ... break;`).
    * Comandos de desvio em laços:
        * `break`: Interrompe o laço imediatamente.
        * `continue`: Pula para a próxima iteração do laço.
    * Demonstrações em `exemplos/repeticao.py`.

---

## 🛠️ Exercícios Práticos

Para aplicar os conceitos, desenvolvemos os seguintes exercícios:

1.  📄 **`exercicios/01_verificacao_par_impar.py`**:
    * Utiliza uma estrutura de decisão simples (`if-else`) para verificar se um número é par ou ímpar.
2.  🎓 **`exercicios/02_sistema_notas_conceitual.py`**:
    * Aplica uma estrutura de decisão encadeada (`if-elif-else`) para classificar um aluno com base em sua nota (ex: A, B, C, D, F).
3.  🔢 **`exercicios/03_tabuada_numero.py`**:
    * Emprega uma estrutura de repetição `for` para gerar a tabuada de um número informado pelo usuário.
4.  ➕ **`exercicios/04_soma_com_condicao_parada.py`**:
    * Usa uma estrutura de repetição `while` para somar números até que um valor específico (sentinela) seja digitado, demonstrando também o uso potencial do `break`.

---

Consulte os arquivos na pasta `exercicios/` e os exemplos (`exemplos/sequencia.py`, `exemplos/decisao.py`, `exemplos/repeticao.py`) para ver a aplicação prática destes conceitos!