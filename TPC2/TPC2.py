#JOGO ADIVINHA O NÚMERO

import random

# 1. MODO 1 : É O JOGADOR A ADIVINHAR

def jogo_jogador_adivinha():
    print("Jogo 1: Adivinha o número!")
    numero_computador = random.randint(0, 100)
    tentativas = 0

    while True:
        
        entrada = input("Adivinha um número (0 a 100):")
        
        try:
            palpite = int(entrada)
        except ValueError:
            print("Apenas é válido com números inteiros!")
            continue #REINICIA SEM CONTAR TENTATIVAS

        #VERIFICAÇÃO LIMITES
        if palpite<0 or palpite>100:
            print("O número está fora dos limites!")
            continue #REINICIA SEM CONTAR TENTATIVAS

        tentativas += 1

        if palpite < numero_computador:
            print("O número do computador é maior!")
        elif palpite > numero_computador:
            print ("O número do computador é menor!")
        else:
            print (f"Parabéns! Acertaste o número do computador em {tentativas} tentativas!")
            break   #Faz o jogador voltar ao menu após completar o jogo


# 2. JOGO 2: É O COMPUTADOR A ADIVINHAR
def jogo_computador_adivinha():
    print("Jogo 2: O computador adivinha o teu número!")
    print("Pensa num número entre 0 e 100...")

    lim_min = 0
    lim_max = 100
    tentativas = 0

    import random 

    while lim_min <= lim_max:
        palpite = random.randint(lim_min, lim_max) #PALPITES DO COMPUTADOR
        tentativas += 1

        print(f"O computador acha que o número que pensaste é {palpite}")
        resposta = input("Responde com '+' (maior), '-'(menor) ou '=' (acertou):")

        if resposta == '+':
            lim_min = palpite + 1
            tentativas +=1
        elif resposta == '-':
            lim_max = palpite -1
            tentativas +=1
        elif resposta == "=":
            print (f"O computador acertou o teu número em {tentativas} tentativa(s)!")
            break 
        else:
            print("Resposta inválida! Insere apenas '+', '-' ou '='.")
        tentativas -= 1


# 3. DEFINIÇÕES DO MENU
def menu():
    while True:
        print("JOGO: ADIVINHA O NÚMERO")
        print("1. MODO 1: Tu adivinhas o número do computador!")
        print("2. MODO 2: O computador adivinha o teu número!")
        print("0. SAIR")
        
        opção = input("Escolhe a tua opção: 1, 2 ou 0: ")

        if opção == "1":
                jogo_jogador_adivinha()
        elif opção == "2":
                jogo_computador_adivinha()
        elif opção == "0":
                print("Até à próxima!")
                break #Encerra o programa
        else:
                print("OPÇÃO INVÁLIDA! Insere um menu ou a opção SAIR")


#4 INICIAR O PROGRAMA

menu()