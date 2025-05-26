# 05-estruturas-complexas/exercicios/05_simulacao_fila_banco.py

"""
Simulação de Fila de Banco com Múltiplos Caixas

Objetivo: Demonstrar o uso de deque para gerenciamento eficiente de filas.
"""

from collections import deque
import random
from time import sleep
from typing import List, Tuple

class SimuladorBanco:
    def __init__(self, num_caixas: int = 3):
        self.caixas: List[deque] = [deque() for _ in range(num_caixas)]
        self.tempo_simulacao: int = 0
        self.clientes_atendidos: List[Tuple[int, int]] = []  # (tempo_chegada, tempo_atendimento)

    def proximo_cliente(self) -> None:
        """Gera um novo cliente de forma aleatória."""
        tempo_chegada = self.tempo_simulacao
        tempo_atendimento = random.randint(2, 8)
        fila = min(self.caixas, key=lambda x: len(x))
        fila.append((tempo_chegada, tempo_atendimento))
        print(f"Novo cliente chegou (Atendimento: {tempo_atendimento} min). Fila escolhida: {self.caixas.index(fila)+1}")

    def processar_caixas(self) -> None:
        """Processa todos os caixas simultaneamente."""
        for i, caixa in enumerate(self.caixas):
            if caixa:
                chegada, atendimento = caixa[0]
                tempo_na_fila = self.tempo_simulacao - chegada
                
                if tempo_na_fila >= atendimento:
                    cliente = caixa.popleft()
                    self.clientes_atendidos.append(cliente)
                    print(f"Caixa {i+1}: Cliente atendido. Tempo total: {tempo_na_fila} min")

    def executar_simulacao(self, duracao: int = 60) -> None:
        """Executa a simulação principal."""
        print("=== Início da Simulação ===")
        for _ in range(duracao):
            self.tempo_simulacao += 1
            
            # Gera novo cliente com probabilidade de 25% a cada minuto
            if random.random() < 0.25:
                self.proximo_cliente()
            
            self.processar_caixas()
            sleep(0.5)  # Pausa para visualização
        
        print("\n=== Relatório Final ===")
        total_clientes = len(self.clientes_atendidos)
        tempos_espera = [saida - chegada for chegada, saida in self.clientes_atendidos]
        
        if total_clientes > 0:
            media_espera = sum(tempos_espera) / total_clientes
            print(f"Clientes atendidos: {total_clientes}")
            print(f"Tempo médio de espera: {media_espera:.1f} min")
            print(f"Clientes restantes nas filas: {sum(len(c) for c in self.caixas)}")
        else:
            print("Nenhum cliente foi atendido.")

if __name__ == "__main__":
    simulador = SimuladorBanco(num_caixas=3)
    simulador.executar_simulacao(duracao=15)
