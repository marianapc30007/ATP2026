#CORRIDA PARA O 100

import random

#INSTRUÇÕES JOGADA COMPUTADOR (independente de modo 1 ou modo 2)
def jogada_computador(total):

    objetivo = ((total -1)// 11 + 1) *11 + 1
    jogada = objetivo - total

    if jogada == 11: #COMPUTADOR PERDEU VANTAGEM
        return random.randint(1,10)

    return jogada 

#INSTRUÇÕES JOGADA UTILIZADOR (independente de modo)
def jogada_utilizador(total):
    máximo = min(10, 100 - total) #Não deixa ultrapassar o 100
    while True:
        try:
            jogada = int(input(f"TOTAL ATUAL: {total}. Qual a sua jogada, de 1 a 10?  "))
            if jogada in range (1, máximo + 1):
                return jogada
            else:
                print("Jogada Inválida! Número fora do intervalo de 1 a 10.")
        except ValueError:
            print("Jogada Inválida! Introduz um número de 1 a 10 inteiro!")


#INSTRUÇÕES MODO 1 
def computador_começa():
    total = 0
    print("MODO 1")

    while total < 100:
        número_pc = jogada_computador(total)
        total += número_pc #ADICIONA O NÚMERO DO COMPUTADOR AO TOTAL
        print (f" O computador jogou {número_pc}. Total: {total}")
    
        if total == 100:
            print("O computador atingiu o 100 e venceu!")
            break

        número_utilizador = jogada_utilizador(total)
        total += número_utilizador  #ADICIONA O NÚMERO DO UTLIZADOR AO TOTAL
        print(f"Jogaste {número_utilizador}. O total agora é {total}")



#INSTRUÇÕES MODO 2
def jogador_começa():
    total = 0
    print("MODO 2")

    while total < 100:
        número_utilizador = jogada_utilizador(total)
        total += número_utilizador #ADICIONA O NÚMERO DO UTILIZADOR AO TOTAL
        print (f" Voçê jogou {número_utilizador}. Total: {total}")
            
        if total == 100:
            print("Parabéns, atingiu o 100 e venceu!")
            break
        
        número_pc = jogada_computador(total)
        total += número_pc  #ADICIONA O NÚMERO DO PC AO TOTAL
        print(f"O computador jogou {número_pc}. O total agora é {total}")
        
        if total == 100:
            print("O computador atingiu o 100, perdeu!")
            break

        
def menu():
    while True:
        print("       JOGO -- CORRIDA PARA O 100       ")
        print ("1. MODO 1 - COMPUTADOR INICIA PRIMEIRA JOGADA ")
        print ("2. MODO 2 - JOGADOR INICIA PRIMEIRA JOGADA ")
        print ("0. SAIR")

        opção = input("ESCOLHE A TUA OPÇÃO: 1, 2 OU 0: ")

        if opção == "1":
            computador_começa()
        elif opção == "2":
            jogador_começa()
        elif opção == "0":
            print("Até à próxima !")
            break
        else:
            print ("Opção inválida! Escolha uma das opções (1,2 ou 0)")

menu()