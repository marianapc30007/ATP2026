
 

def medias(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res
 
 
def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n")
    file.close()
    return
 
 
def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:  
            data, tmin, tmax, prec, _ = line.split("|")  
            ano, mes , dia = data.split("-")    
            tuplo = ((ano, mes , dia), tmin, tmax, prec)
            res.append(tuplo)
    file.close()
    return res
 
 
def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for data, tmin, tmax, prec in tabMeteo:
        if tmin < minima:
            minima = tmin
    return minima
 
 
def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        res.append((data, tmax - tmin))
    return res
 
 
 
def maxChuva(tabMeteo):
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]
    for data, tmin, tmax, prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)
 

def diasChuvosos(tabMeteo, p):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res
 
 
def maxPeriodoCalor(tabMeteo, p):
    atual = 0
    maximo = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            atual = atual + 1
            if atual > maximo:
                maximo = atual
        else:
            atual = 0
    return maximo
 
from matplotlib import pyplot as plt
 
def grafTabMeteo(t):

        y_min = [tmin for data, tmin, tmax, prec in t]
        y_max = [tmax for data, tmin, tmax, prec in t]
        y_prec = [prec for data, tmin, tmax, prec in t]

        x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]

        plt.plot(x,y_min, color = "blue", marker = "o", label = "Tmin ºC")
        plt.show(x,y_min, color = "red", marker = "o", label = "Tmax ºC")
        plt.title("Temperatura")
        plt.legend()
        plt.grid()
        plt.show()

        plt.bar(x,y_prec, color = "green", marker = "o", label = "Precipitação(mm)")
        Plt.title("Precipitação")
        plt.show()
        return
 
def exibir_menu():
    print("     MENU PRINCIPAL      ")
    print("1: Média temperaturas")
    print("2: Guardar tabela meteriológica")
    print("3: Carregar tabela meteriológica")
    print("4: Temperatura mínima mais baixa registada")
    print("5: Amplitude térmica")
    print("6: Dia com maior precipitação")
    print("7: Dias com precipitação superior a um limite")
    print("8: Maior período de calor")
    print("9: Gráficos da temp mínima, máxima e de precipitação.")
    print("0: Sair da aplicação")

 
def principal():
    tab = tabExemplo
    print("Bem-vindo! Existe uma tabela de exemplo (clique na opção 4).")

    opcao = -1
    while opcao != 0:
        exibir_menu()
        opcao = lerInteiro("Opção: ")

    if opcao == 0:
        print("A terminar a aplicação. Até à próxima!")
    elif opcao == 1:
        print(medias(tabMeteo1))
    elif opcao == 2:
        print(guardaTabMeteo(tabMeteo1, "meteriologia.txt"))
    elif opcao == 3:
        print(carregaTabMeteo("meteriologia.txt"))
    elif opcao == 4:
        print(minMin(tabMeteo1))
    elif opcao == 5:
        print(amplTerm(tabMeteo1))
    elif opcao == 6:
        print(maxChuva(tabMeteo1))
    elif opcao == 7:
        print(diasChuvosos(tabMeteo1, 0))    
    elif opcao == 8:
        print(maxPeriodoCalor(tabMeteo1, 0.6))
    elif opcao ==9:
        print(grafTabMeteo(tabMeteo1))
    else:
        print("Opção inválida! Tente novamente.")

principal()
 
