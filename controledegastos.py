receitas = []
gastos = []

try:
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha.startswith("RECEITA"):
                valor = float(linha.split(" - ")[1])
                receitas.append(valor)

            elif linha.startswith("GASTO"):
                valor = float(linha.split(" - ")[1])
                gastos.append(valor)

except FileNotFoundError:
    pass


def salvar_dados():
    with open("dados.txt", "w") as arquivo:
        for valor in receitas:
            arquivo.write(f"RECEITA - {valor}\n")

        for valor in gastos:
            arquivo.write(f"GASTO - {valor}\n")


opcao = ""

while opcao != "0":
    print("======CONTROLE DE GASTOS======")
    print("1 - Adicionar receita")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Apagar receita")
    print("5 - Apagar gasto")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor da receita: R$ "))
        receitas.append(valor)

        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"RECEITA - {valor}\n")

        print("Receita adicionada!")

    elif opcao == "2":
        valor = float(input("Valor do gasto: R$ "))
        gastos.append(valor)

        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"GASTO - {valor}\n")

        print("Gasto adicionado!")

    elif opcao == "3":
        total_receitas = sum(receitas)
        total_gastos = sum(gastos)
        saldo = total_receitas - total_gastos

        print("R$ ", saldo)

        if saldo > 0:
            print("Saldo positivo")
        elif saldo == 0:
            print("Saldo zerado")
        else:
            print("Saldo negativo")

    elif opcao == "4":
        if len(receitas) == 0:
            print("Nenhuma receita cadastrada.")
        else:
            print("=== RECEITAS ===")

            for indice, valor in enumerate(receitas):
                print(f"{indice + 1} - R$ {valor}")

            escolha = int(input("Digite o número da receita que deseja apagar: "))

            if escolha >= 1 and escolha <= len(receitas):
                receitas.pop(escolha - 1)
                salvar_dados()
                print("Receita apagada com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        if len(gastos) == 0:
            print("Nenhum gasto cadastrado.")
        else:
            print("=== GASTOS ===")

            for indice, valor in enumerate(gastos):
                print(f"{indice + 1} - R$ {valor}")

            escolha = int(input("Digite o número do gasto que deseja apagar: "))

            if escolha >= 1 and escolha <= len(gastos):
                gastos.pop(escolha - 1)
                salvar_dados()
                print("Gasto apagado com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida")