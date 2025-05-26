# 03-estruturas-controle/decisao.py

"""
Estruturas de Decisão (Condicionais)

Permitem que o programa escolha entre diferentes caminhos de execução
com base em certas condições. As principais em Python são `if`, `elif` e `else`.
"""

print("--- Demonstração de Estruturas de Decisão ---")

# Exemplo 1: Estrutura `if` (Decisão Simples)
print("\n--- Exemplo 1: `if` (Decisão Simples) ---")
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
else:
    if idade >= 18:
        print("Você é maior de idade.")
        # Este bloco só executa se a condição (idade >= 18) for verdadeira.

# Exemplo 2: Estrutura `if-else` (Decisão Composta)
print("\n--- Exemplo 2: `if-else` (Decisão Composta) ---")
temperatura = float(input("Digite a temperatura atual em Celsius: "))

if temperatura > 25:
    print("Está calor! Considere usar roupas leves.")
else:
    print("Não está tão calor. Um casaco pode ser útil.")
    # O bloco `else` executa se a condição do `if` (temperatura > 25) for falsa.

# Exemplo 3: Estrutura `if-elif-else` (Decisão Encadeada/Múltipla Escolha)
print("\n--- Exemplo 3: `if-elif-else` (Decisão Encadeada) ---")
# Baseado no exemplo de sistema de notas que o material do curso provavelmente tem.
nota = float(input("Digite a nota do aluno (0 a 10): "))

if 9.0 <= nota <= 10.0:
    conceito = "A (Excelente)"
elif 7.0 <= nota < 9.0:
    conceito = "B (Bom)"
elif 5.0 <= nota < 7.0:
    conceito = "C (Regular)"
elif 3.0 <= nota < 5.0:
    conceito = "D (Insuficiente)"
elif 0.0 <= nota < 3.0:
    conceito = "F (Reprovado)"
else:
    conceito = "Nota inválida! Deve ser entre 0 e 10."
    # O `else` final captura casos onde nenhuma das condições anteriores foi atendida.

print(f"Conceito do aluno: {conceito}")

# Exemplo 4: Operador Ternário (forma concisa de if-else para atribuições)
print("\n--- Exemplo 4: Operador Ternário ---")
saldo = float(input("Digite seu saldo bancário: R$ "))
status_conta = "Positivo" if saldo >= 0 else "Negativo"
print(f"Status da conta: {status_conta}")

print("\n--- Fim da Demonstração de Decisões ---")

"""
Explicação:
- `if`: Avalia uma condição. Se verdadeira, o bloco de código indentado abaixo dele é executado.
- `else`: Opcional. Se a condição do `if` (ou do último `elif`) for falsa, o bloco do `else` é executado.
- `elif` (else if): Permite testar múltiplas condições em sequência. Assim que uma condição `elif` é
  verdadeira, seu bloco é executado e as demais condições `elif` e o `else` são ignorados.
- Operador Ternário: Uma forma compacta para `if-else` que resulta em um valor, útil para atribuições.
  Sintaxe: `valor_se_verdadeiro if condicao else valor_se_falso`.
"""
