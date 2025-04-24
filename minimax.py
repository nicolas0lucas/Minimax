# Tabuleiro do jogo (lista com 9 posições)
tabuleiro = [" " for _ in range(9)]

# Função para mostrar o tabuleiro
def mostrar_tabuleiro():
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

# Função para verificar se alguém ganhou
def verificar_ganhador(jogador):
    # Todas as possíveis combinações para vencer
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    
    for combo in combinacoes:
        if all(tabuleiro[pos] == jogador for pos in combo):
            return True
    return False

# Função para verificar empate
def verificar_empate():
    return " " not in tabuleiro

# Função Minimax (a inteligência do computador)
def minimax(tabuleiro, profundidade, eh_maximizando):
    if verificar_ganhador("O"):  # Computador ganhou
        return 10 - profundidade
    elif verificar_ganhador("X"):  # Jogador ganhou
        return -10 + profundidade
    elif verificar_empate():  # Empate
        return 0

    if eh_maximizando:  # Vez do computador (O)
        melhor_valor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:  # Vez do jogador (X)
        melhor_valor = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para a melhor jogada do computador
def melhor_jogada():
    melhor_valor = -float("inf")
    melhor_posicao = -1
    
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
                
    return melhor_posicao

# Função principal do jogo
def jogar():
    print("Bem-vindo ao Jogo da Velha!")
    print("Você é X e o computador é O")
    print("Posições: 0-8 (esquerda para direita, de cima para baixo)")
    
    while True:
        mostrar_tabuleiro()
        
        # Vez do jogador
        while True:
            try:
                posicao = int(input("Escolha uma posição (0-8): "))
                if 0 <= posicao <= 8 and tabuleiro[posicao] == " ":
                    break
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número entre 0 e 8.")
        
        tabuleiro[posicao] = "X"
        
        # Verifica se o jogador ganhou
        if verificar_ganhador("X"):
            mostrar_tabuleiro()
            print("Parabéns! Você venceu!")
            break
            
        # Verifica empate
        if verificar_empate():
            mostrar_tabuleiro()
            print("Empate!")
            break
            
        # Vez do computador
        print("Computador está pensando...")
        posicao_computador = melhor_jogada()
        tabuleiro[posicao_computador] = "O"
        
        # Verifica se o computador ganhou
        if verificar_ganhador("O"):
            mostrar_tabuleiro()
            print("O computador venceu! Tente novamente.")
            break
            
        # Verifica empate
        if verificar_empate():
            mostrar_tabuleiro()
            print("Empate!")
            break

# Inicia o jogo
jogar()
