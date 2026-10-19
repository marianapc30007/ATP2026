# Aplicação para manipulação de listas de inteiros

import random

def menu():
    print("   MENU   ")
    print("(1) CRIAR LISTA")
    print("(2) LER LISTA")
    print("(3) SOMA")
    print("(4) MÉDIA")
    print("(5) MAIOR")
    print("(6) MENOR")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) SAIR")

#LISTA ALEATORIA 
def criar_lista():
    lista = []
    válido = False

    while válido == False:
        try:
            n = int(input("Quantos elementos deseja que a lista tenha ? "))
            if n > 0:
                válido = True
            else:
                print("O número tem de ser maior que 0.")
        except ValueError:
            print("Valor inválido!")
            
    for elemento in range(n):
        elemento = random.randint(1,100)
        lista.append(elemento)
    return lista

#LÊ LISTA - INPUT: a lista que eu quero. OUTPUT: lista guardada
def ler_lista():
    lista = []
    válido = False

    while válido == False:
        try:
            n = int(input("Quantos elementos deseja que a lista tenha ? "))
            if n > 0:
                válido = True
            else:
                print("O número tem de ser maior que 0.")
        except ValueError:
            print("Valor inválido!")

    contador = 0
    while contador < n: #em vez do range
        try:
            elemento = int(input(f"Introduza o {contador + 1 } elemento: "))

            if elemento > 1 and elemento < 100:
                lista.append(elemento)
                contador = contador + 1
            else:
                print("Opção inválida! Tem de estar entre 0 e 100")
                elemento = int(input(f"Introduza o {contador + 1 } elemento: "))
        except ValueError:
            print("A resposta tem de ser um número inteiro.")

    return lista

def soma_lista(lista_interna):
    total = 0
    for elemento in lista_interna:
        total = total + elemento
    return total

def media_lista(lista_interna): 
    return soma_lista(lista_interna) / len(lista_interna)

def maior_elemento(lista_interna):
    maior = lista_interna[0] #1 elemento lista e depois compara com os seguintes
    for elemento in lista_interna:
        if maior < elemento:
            maior = elemento
    return maior

def menor_elemento(lista_interna):
    menor = lista_interna[0] 
    for elemento in lista_interna:
        if menor > elemento:
            menor = elemento
    return menor

def esta_ordenadacresc(lista_interna):
    if lista_interna == sorted (lista_interna):
        print("Sim, a lista está ordenada por ordem crescente.")
    else:
        print("Não, a lista não está ordenada por ordem crescente.")

def esta_ordenadadecresc(lista_interna):
    i = 0
    resultado = True
    while i < len(lista_interna) - 1 and resultado == True:
            if lista_interna[i] < lista_interna[i+1]:
                resultado = False
            else:
                i = i + 1   # passa para proximo elemento
    
    if resultado == True:
        print("Sim, a lista está ordenada por ordem decrescente.")
    else:
        print("Não, a lista não está ordenada por ordem decrescente.")

    
def procurar_elemento(lista_interna,elemento):
    i = 0
    resultado = -1
    while i < len(lista_interna) and elemento != lista_interna[i]:
        i = i + 1
    if i < len(lista_interna):
        resultado = i
    return resultado



#INSTRUÇÕES MENU
lista_interna = []
exibir_menu = True

while exibir_menu:
        menu()
        opção = input("Escolhe um dos menus.")

        if opção == "1":
            lista_interna = criar_lista()
            print(f"Lista criada com sucesso: {lista_interna} ")

        elif opção == "2":
            lista_interna = ler_lista()
            print(f"Lista criada com sucesso: {lista_interna} ")

        elif opção == "3":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                resultado = soma_lista(lista_interna)
                print(f"A soma da lista é {resultado}")

        elif opção == "4":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                resultado = media_lista(lista_interna)
                print(f"A média da lista é {resultado}")

        elif opção == "5":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                resultado = maior_elemento(lista_interna)
                print(f"O maior elemento da lista é {resultado}")

        elif opção == "6":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                resultado = menor_elemento(lista_interna)
                print(f"O menor elemento da lista é {resultado}")

        elif opção == "7":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                esta_ordenadacresc(lista_interna)

        elif opção == "8":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                esta_ordenadadecresc(lista_interna)

        elif opção == "9":
            if len(lista_interna) == 0:
                print("A lista está vazia.")
            else:
                try:
                    número = int(input("Qual o elemento a procurar ?"))
                    resultado = procurar_elemento(lista_interna, número)
                    if resultado == -1:
                        print("Elemento não encontrado.")
                    else:
                        print(f"Posição do elemento: {resultado}")
                except ValueError:
                    print("Valor inválido!")

        elif opção == "0":
            print(f"Fim da aplicação. Lista guardada: {lista_interna}")
            exibir_menu = False

        else:
            print("Opção inválida!")

