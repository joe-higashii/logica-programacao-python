# Teste de mesa para cálculo de média
def teste_mesa_media():
    testes = [
        {"n1": 6.0, "n2": 8.0, "esperado": "Aprovado"},
        {"n1": 4.5, "n2": 3.5, "esperado": "Reprovado"},
        {"n1": 7.0, "n2": 7.0, "esperado": "Aprovado"}
    ]

    for i, teste in enumerate(testes, 1):
        media = (teste["n1"] + teste["n2"]) / 2
        resultado = "Aprovado" if media >= 7 else "Reprovado"
        print(f"Teste {i}: Entrada ({teste['n1']}, {teste['n2']}) | Esperado: {teste['esperado']} | Obtido: {resultado}")

if __name__ == "__main__":
    teste_mesa_media()
