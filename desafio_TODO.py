import textwrap

def menu ():
    menu = """\n
    ***************Menu***************
     [d]\tDepositar
     [s]\tSacar
     [e]\tExtrato
     [nc]\tNova Conta
     [lc]\tListar Contas
     [nu]\tNvo Usuário
     [q]\tSair
    \n"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+=valor
        extrato+= f"Depósito: \tR$ {valor:.2f}\n"
        extrato+= f"Saldo: \t\tR$ {saldo:.2f}\n"
        print('\n=== Depósito efetuado com sucesso! ===')
    else:
        print("\n=== A Operação falho! o valor informado é inválido! ===")

    return saldo,extrato

def saque (*, saldo, valor, extrato, limite, numero_saques,LIMITE_SAQUES):      #O asterisco é para usar argumentos de forma nomeada
    excedeu_saldo= valor>saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('\n=== Operação falhou! Você não tem saldo suficiente. ===')

    elif excedeu_limite:
        print('\n=== Operação falhou! O valor do saque foi excede o limite! ===')

    elif excedeu_saques:
        print('\n=== Operação falho! O Número de saques excedido! ===')

    elif valor >0:
        saldo-= valor
        extrato+= f"Saque: \t\rR$ {valor:.2f}\n"
        numero_saques+=1
        print("\n===Saque realizado com sucesso! ===")

    else:
        print("\n=== A Operação falhou! O valor informado é inválido!")

    return saldo,extrato 

def exibir_extrato (saldo,/,*,extrato) :
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


    return

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente os números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n Usuário já existente com esse CPF")
        return

    nome = input("Informe eu nome completo: ")
    data_nascimento = input("Informe sua data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço(logradouro, Nº - Bairro - cidade/sigla Estado: ")

    usuarios.append({"nome:": nome, "Data de Nascimento:": data_nascimento,"cpf:": cpf ,"endereço:":endereco}) #estrutura de dicionário

    print("=== Usuário criado com sucesso ===")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario (cpf,usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia:": agencia, "numero da conta:": numero_conta, "usuario:": usuario}

    print("\n=== Ususario não encontrado, fluxo de criação de conta encerrado! ===")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))




def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 3500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
            if valor > 0 and saldo >= 0 and valor <= limite and numero_saques < LIMITE_SAQUES:
                numero_saques += 1

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print("=== Conta criada com sucesso! ===")

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()