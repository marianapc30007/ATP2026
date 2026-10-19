# TPC5 : Aplicação para a gestão de alunos

# aluno = (nome, id, [notaTPC, notaProj, notaTeste])
# turma = [aluno]

def menu():
    print("       Gestão Alunos -- Aplicação        ")
    print("1. Criar uma turma")
    print("2. Inserir um aluno na turma")
    print("3. Listar a turma")
    print("4. Consultar um aluno por id")
    print("8.Guardar a turma em ficheiro")
    print("9. Carregar uma turma dum ficheiro")
    print("0. Sair da aplicação")

# CRIAR A TURMA COM NENHUM ALUNO
def criar_turma():
    return []     

# EVITAR ERRO DE ALUNO REPETIDO
def aluno_valido(turma,id_aluno):
    existe = False
    for aluno in turma:
        if aluno[1] == id_aluno:
            existe = True
    return existe

# DEFINIR A NOTA DOS TESTES
def nota(número):
    while True:
        try:
            n = float(input(número))
            if 0 <= n <= 20:
                return n
            else:
                print("A nota deve ser um número entre 0 e 20.")
        except ValueError:
            print("As notas introduzidas devem ser números válidos.")


# CRIAR ALUNO E INTRODUZI LOS NA LISTA VAZIA
def inserir_aluno(turma):  # input - recebe a turma
    nome = input("Nome:  ")
    id_aluno = input("ID:  ")

    if aluno_valido(turma, id_aluno) == True:
        print(f"Já existe um aluno registado com o ID:{id_aluno}.")
    else:

        nota_tpc = nota("Nota do TPC: ")
        nota_projeto = nota("Nota do Projeto: ")
        nota_teste = nota("Nota do Teste: ")

        aluno = (nome, id_aluno, [nota_tpc, nota_projeto, nota_teste])
        turma.append(aluno)
        print("Aluno inserido com sucesso!")
    return turma

def listar_turma(turma):
    if len(turma) == 0:
        print("A lista está vazia.")
    for aluno in turma:
        nome, id_aluno, notas = aluno
        print(f"{id_aluno} | {nome} | Notas: TPC: {notas[0]}, Projeto: {notas[1]}, Teste: {notas[2]} ")

def consultar_aluno(turma):
    id_aluno = input("ID do aluno: ")
    encontrado = False
    for aluno in turma:
        if aluno [1] == id_aluno:
            nome, id_aluno, notas = aluno
            print(f"Nome: {nome}, ID: {id_aluno}, Notas: TPC: {notas[0]}, Projeto: {notas[1]}, Teste: {notas[2]}")
            encontrado = True
    if encontrado ==False:
        print("Aluno não encontrado")

def guardar_Turma(turma,fnome):
    file = open(fnome, "w")
    for aluno in turma:
        nome, id_aluno, notas = aluno
        file.write(f"{nome} | {id_aluno} | {notas[0]}@{notas[1]}@{notas[2]}\n")
    file.close()
    print(f"len({turma}) alunos guardados em {fnome}.")

def carregar_turma(fnome):
    turma = []
    try:
        file = open(fnome, "r")
    except FileNotFoundError:
        print("Ficheiro não encontrado!")
        return turma
    for line in file:
        campos = line.strip().split("|")
        nome = campos[0].strip()
        id_aluno = campos[1].strip()
        notas = campos[2].strip().split("@")
        aluno = (nome, id_aluno, [float(notas[0]), float(notas[1]), float(notas[2])])
        turma.append(aluno)
    file.close()
    print(f"{len(turma)} alunos carregados em {fnome}")
    return turma

turma = []
exibir_menu = True

while exibir_menu:
        menu()
        opção = input("Opção Menu: ")
        válido = True

        if opção == "1":
            while válido == True:
                if len(turma)!= 0:
                    confirmar = input("Tem a certeza que quer apagar a turma criada? (Sim /Não)  ")
                    if confirmar == "Sim" or confirmar == "sim":
                        print("Turma nova criada com sucesso")
                        turma = criar_turma()
                        válido = False
                    elif confirmar == "Não" or confirmar == "não":
                        turma = criar_turma()
                        print("Operação cancelada com sucesso")
                        válido = False
                    else:
                        print("Introduza a resposta (Sim) ou (Não)")
                else:
                    turma = criar_turma()
                    print("Turma criada com sucesso!")
                    válido = False


        elif opção == "2":
            turma = inserir_aluno(turma)

        elif opção == "3":
           listar_turma(turma)

        elif opção == "4":
            consultar_aluno(turma)

        elif opção == "8":
            guardar_Turma(turma, "turma.txt")
        
        elif opção == "9":
            turma = carregar_turma("turma.txt")
            print("Turma carregada")

        elif opção == "0":
            print("Até à próxima")
            exibir_menu = False

        else:
            print("Opção inválida. Introduza um dos menus.")







