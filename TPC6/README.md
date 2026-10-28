
tabExemplo = [((2022, 1, 20), 2.0, 16.0, 0.0),
              ((2022, 1, 21), 1.0, 13.0, 0.2),
              ((2022, 1, 22), 7.0, 17.0, 0.01)]

 
def lerInteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Escreva um número inteiro.")
 
 
def lerReal(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Escreva um número (ex: 12.5).")
 
 
def diasDoMes(ano, mes):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 29
    else:
        return 28
 
 
def tabelaVazia(tabMeteo):
    if len(tabMeteo) == 0:
        print("A tabela está vazia! Crie ou carregue uma tabela primeiro.")
        return True
    return False
 

 
def criarTab():
    n = lerInteiro("Quantos dias quer registar? ")
    while n < 1:
        print("Tem de registar pelo menos 1 dia.")
        n = lerInteiro("Quantos dias quer registar? ")
 
    tab = []
    for i in range(1, n + 1):
        print(f"\n--- Dia {i} de {n} ---")
 
        ano = lerInteiro("Ano: ")
        while ano < 1:
            print("Ano inválido.")
            ano = lerInteiro("Ano: ")
 
        mes = lerInteiro("Mês (1-12): ")
        while mes < 1 or mes > 12:
            print("Mês inválido.")
            mes = lerInteiro("Mês (1-12): ")
 
        maxDia = diasDoMes(ano, mes)
        dia = lerInteiro(f"Dia (1-{maxDia}): ")
        while dia < 1 or dia > maxDia:
            print("Dia inválido.")
            dia = lerInteiro(f"Dia (1-{maxDia}): ")
 
        tmin = lerReal("Temperatura mínima (ºC): ")
        tmax = lerReal("Temperatura máxima (ºC): ")
        while tmax < tmin:
            print("A máxima não pode ser inferior à mínima.")
            tmax = lerReal("Temperatura máxima (ºC): ")
 
        prec = lerReal("Precipitação (mm): ")
        while prec < 0:
            print("A precipitação não pode ser negativa.")
            prec = lerReal("Precipitação (mm): ")
 
        tab.append(((ano, mes, dia), tmin, tmax, prec))
    return tab

 
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
        line = line.strip()          # tira o \n do fim
        if line == "":               # ignora linhas em branco
            continue
        campos = line.split("|")
        data = campos[0]
        tmin = campos[1]
        tmax = campos[2]
        prec = campos[3]
        ano, mes, dia = data.split("-")
        res.append(((int(ano), int(mes), int(dia)),
                    float(tmin), float(tmax), float(prec)))
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
 
 
def grafTabMeteo(t):
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        print("A biblioteca matplotlib não está instalada.")
        print("Instale-a com:  pip install matplotlib")
        return
 
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    y_min = [tmin for data, tmin, tmax, prec in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    y_prec = [prec for data, tmin, tmax, prec in t]
 
    # Gráfico 1: temperaturas
    plt.plot(x, y_min, color="blue", marker="o", label="Tmin (ºC)")
    plt.plot(x, y_max, color="red", marker="o", label="Tmax (ºC)")
    plt.title("Temperatura mínima e máxima")
    plt.xlabel("Data")
    plt.ylabel("ºC")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
 
    # Gráfico 2: precipitação
    plt.bar(x, y_prec, color="green", label="Precipitação (mm)")
    plt.title("Precipitação")
    plt.xlabel("Data")
    plt.ylabel("mm")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    return
 
def formataData(data):
    ano, mes, dia = data
    return f"{dia:02d}/{mes:02d}/{ano}"
 
 
def mostraTabela(tabMeteo):
    print(f"\n{'Data':<12}{'Tmin':>8}{'Tmax':>8}{'Prec(mm)':>10}")
    print("-" * 38)
    for data, tmin, tmax, prec in tabMeteo:
        print(f"{formataData(data):<12}{tmin:>8.1f}{tmax:>8.1f}{prec:>10.2f}")
 
 
def mostraPares(pares, unidade):
    for data, valor in pares:
        print(f"  {formataData(data)} -> {valor:.2f} {unidade}")
 
 
def mostraMenu():
    print("""
===== ANÁLISE DE TABELAS METEOROLÓGICAS =====
 1) Criar uma nova tabela (introduzir dados)
 2) Carregar tabela de um ficheiro
 3) Guardar tabela num ficheiro
 4) Mostrar a tabela atual
 5) Temperatura média de cada dia
 6) Temperatura mínima mais baixa
 7) Amplitude térmica de cada dia
 8) Dia com maior precipitação
 9) Dias com precipitação superior a um limite
10) Maior período consecutivo com precipitação abaixo de um limite
11) Gráficos (temperaturas e precipitação)
 0) Sair
""")
 
 
def principal():
    tab = tabExemplo       # começa com a tabela de exemplo
    print("Bem-vindo! Foi carregada uma tabela de exemplo (opção 4 para ver).")
 
    opcao = -1
    while opcao != 0:
        mostraMenu()
        opcao = lerInteiro("Opção: ")
 
        if opcao == 0:
            print("A terminar a aplicação. Até à próxima!")
 
        elif opcao == 1:
            tab = criarTab()
            print("\nTabela criada com sucesso!")
 
        elif opcao == 2:
            nome = input("Nome do ficheiro (ex: meteorologia.txt): ")
            try:
                tab = carregaTabMeteo(nome)
                print(f"Tabela carregada ({len(tab)} dias).")
            except FileNotFoundError:
                print("Ficheiro não encontrado.")
            except (ValueError, IndexError):
                print("O ficheiro não tem o formato esperado.")
 
        elif opcao == 3:
            if not tabelaVazia(tab):
                nome = input("Nome do ficheiro (ex: meteorologia.txt): ")
                guardaTabMeteo(tab, nome)
                print(f"Tabela guardada em '{nome}'.")
 
        elif opcao == 4:
            if not tabelaVazia(tab):
                mostraTabela(tab)
 
        elif opcao == 5:
            if not tabelaVazia(tab):
                print("\nTemperatura média de cada dia:")
                mostraPares(medias(tab), "ºC")
 
        elif opcao == 6:
            if not tabelaVazia(tab):
                print(f"\nTemperatura mínima mais baixa: {minMin(tab):.1f} ºC")
 
        elif opcao == 7:
            if not tabelaVazia(tab):
                print("\nAmplitude térmica de cada dia:")
                mostraPares(amplTerm(tab), "ºC")
 
        elif opcao == 8:
            if not tabelaVazia(tab):
                data, valor = maxChuva(tab)
                print(f"\nMaior precipitação: {valor} mm no dia {formataData(data)}")
 
        elif opcao == 9:
            if not tabelaVazia(tab):
                p = lerReal("Limite de precipitação (mm): ")
                lista = diasChuvosos(tab, p)
                if len(lista) == 0:
                    print(f"\nNenhum dia teve precipitação superior a {p} mm.")
                else:
                    print(f"\nDias com precipitação superior a {p} mm:")
                    mostraPares(lista, "mm")
 
        elif opcao == 10:
            if not tabelaVazia(tab):
                p = lerReal("Limite de precipitação (mm): ")
                n = maxPeriodoCalor(tab, p)
                print(f"\nMaior nº de dias consecutivos com precipitação "
                      f"abaixo de {p} mm: {n}")
 
        elif opcao == 11:
            if not tabelaVazia(tab):
                grafTabMeteo(tab)
 
        else:
            print("Opção inválida! Tente novamente.")

    principal()
 
