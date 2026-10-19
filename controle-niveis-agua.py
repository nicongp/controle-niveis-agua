import colorama
from colorama import Fore, Style

# Avisa o Windows para ligar o sistema de cores no terminal
colorama.init()

# Lista guardando apenas as mensagens, do nível 1 ao 5
mensagens = [
    "Muito baixo (crítico)", 
    "Baixo", 
    "Médio", 
    "Alto", 
    "Muito alto (alerta)"
]

# Função simples para descobrir qual cor usar
def escolhe_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

print("--- Monitoramento do Reservatório ---\n")

# Variável para ajudar a contar em qual nível estamos
nivel_atual = 1

# Passa por cada mensagem dentro da nossa lista
for texto in mensagens:
    # Pega a cor certa pra esse nível usando a nossa função
    cor = escolhe_cor(nivel_atual)
    
    # Imprime a cor, o texto e no final usa o RESET_ALL para não manchar o resto do terminal
    print(f"{cor}Nível {nivel_atual}: {texto}{Style.RESET_ALL}")
    
    # Soma 1 para ir pro próximo nível na próxima volta do laço
    nivel_atual = nivel_atual + 1

print("\n--- Simulação finalizada ---")