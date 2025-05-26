## ☕ Exercício 1: Algoritmo de Preparo de Café

**🤔 Problema:**

Descreva em pseudocódigo os passos para preparar um café, considerando:

1.  Verificação da quantidade de água na chaleira.
2.  Aquecimento da água até a temperatura ideal (ex: 100°C).
3.  Adição da quantidade correta de pó de café ao filtro.
4.  O processo de filtragem da água quente sobre o pó.

**💡 Exemplo de Solução:**

```pseudocode
Algoritmo Fazer_Cafe

Var
  agua_ml: Inteiro
  temperatura_atual: Real
  po_colheres: Inteiro

Início
  // 1. Verificação e adição de água
  Escreva("Informe a quantidade de água em ml (ex: 300): ")
  Leia(agua_ml)
  Se agua_ml <= 0 Então
    Escreva("Quantidade de água inválida. Adicionando 300ml por padrão.")
    agua_ml <- 300
  FimSe
  Escreva("Colocando ", agua_ml, "ml de água na chaleira.")

  // 2. Aquecimento da água
  temperatura_atual <- 25 // Simula temperatura ambiente inicial
  Escreva("Aquecendo a água...")
  Enquanto temperatura_atual < 100 Faça
    // Simula o aumento da temperatura
    temperatura_atual <- temperatura_atual + 10
    Escreva("Temperatura atual: ", temperatura_atual, "°C")
    // Aguardar um pouco (simulação)
  FimEnquanto
  Escreva("Água aquecida a 100°C.")

  // 3. Adição de pó ao filtro
  Escreva("Informe a quantidade de colheres de pó de café (ex: 3): ")
  Leia(po_colheres)
  Se po_colheres <= 0 Então
    Escreva("Quantidade de pó inválida. Adicionando 3 colheres por padrão.")
    po_colheres <- 3
  FimSe
  Escreva("Colocando ", po_colheres, " colheres de pó no filtro.")

  // 4. Processo de filtragem
  Escreva("Despejando a água quente sobre o pó no filtro.")
  Escreva("Coletando o café na garrafa térmica.")
  Escreva("Café pronto!")
Fim