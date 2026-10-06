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

#LISTA ALEATORIA NÚMEROS INPUT: quantidade números . OUTPUT: lista criada
def criar_lista(N):
    lista = []
    n = int(input("Quantos elementos deseja que a lista tenha ? "))
    for elemento in range(n):
        elemento = random.randint(1,100)
        lista.append(elemento)
    return lista


#LÊ LISTA - INPUT: a lista que eu quero. OUTPUT: lista guardada
def ler_lista():
    lista = []
    n = int(input("Quantos elementos deseja que a lista tenha ? "))
    contador = 0
    while contador < n: #em vez do range
        elemento = int(input(f"Introduza o {contador + 1 } elemento: "))
        lista.append(elemento)
        contador = contador + 1
    return lista

def soma_lista(lista_interna):
    total = 0
    for elemento in lista_interna:
        total = total + elemento
    return total

def media_lista(lista_interna):
    média = 0
    for elemento in lista_interna:
        média = soma_lista / len(lista_interna) 
    return média

def maior_elemento(lista_interna):
    maior = lista[0] #1 elemento lista e depois compara com os seguintes
    for elemento in lista_interna:
        if maior > elemento:
            maior = elemento
    return maior

def menor_elemento(lista_interna):
    menor = lista[0] 
    for elemento in lista_interna:
        if menor < elemento:
            menor = elemento
    return menor


#FALTA APRENDER ORDENAR LISTA E VER SE LISTA ESTÁ VAZIA -- DEPOIS ACABAR TPC

#INSTRUÇÕES MENU
opção = input("Escolhe um dos menus.")

if opção == "1":
    lista_interna = criar_lista()
    print(f"Lista criada com sucesso: {lista_interna} ")
if opção == "2":
    lista_interna = ler_lista()
    print(f"Lista criada com sucesso: {lista_interna} ")