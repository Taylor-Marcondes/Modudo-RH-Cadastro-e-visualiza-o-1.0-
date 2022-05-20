provi = {}  # dicionario onde serão cadastrados os colaboradores
funcionarios = []  # lista que ira receber uma copia dos dicionario

# Separador
def cab():
    print("-" * 45)

# Menu principal, conectora para as outras funções
def menuPrincipal(msg):
    print("\33[1;33mMenu principal\33[m".center(55))
    while True:
        print("""
[1] Novo cadastro
[2] Consulta
[3] item 3
[4] item 4
[5] item 5
[6] Sair""")
        print()
        opc = int(input(msg))
        cab()
        if opc == 1:
            print(cadastro())
            break
        if opc == 2:
            print(consulta())
            cab()
            print(menuOUsair())
            break
        if opc == 3:
            pass

        while True:
            if opc < 1 or opc > 6:
                print("\033[31mErro: Escolha uma opção valida.\033[m")
                cab()
                print(menuPrincipal(msg))
            else:
                break
        if opc == 6:
            print(finalizarPrograma())
            break

# Realiza o cadastro dos funcionarios
def cadastro():
    print("\33[1;33mCadastro\33[m".center(55))
    while True:
        provi["Nome"] = input("Nome: ").title()
        provi["Departamento"] = input("Departamento: ").title()
        provi["Cargo"] = input("Cargo: ").title()
        provi["Salario"] = input("Salario: ")
        funcionarios.append(provi.copy())
        opc = input("Deseja continuar: [s/n] ").upper()
        print("-" * 45)
        if opc == "N":
            print(menuOUsair())
            break

#Consultar a tabela gerada com as informações dos colaboradores
def consulta():
    from pandas import DataFrame
    df = DataFrame(funcionarios)
    return df

# Retornar ao menu principal
def menuOUsair():
    opc = input("\033[1;36mDeseja retornar ao menu principal? [s/n] \033[m").upper()
    cab()
    if opc == "S":
        print(menuPrincipal("Qual opção desejada? "))
    else:
        print(finalizarPrograma())


# Finalizar programa
def finalizarPrograma():
    from time import sleep
    print("\n\033[35m\t\t\t\tFinalizando..\033[m")
    sleep(0.8)
    print("\n\033[35m\t>> Programa finalizado, até logo! <<\33[m\n")
    cab()
    
