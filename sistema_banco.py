menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saque=valor > saldo # caso o valor digitado seja maior que o saldo disponível

        execedeu_limite= valor > limite # caso o valor digitado seja maior que R$500,00

        excedeu_saques=numero_saques >= LIMITE_SAQUES # Verificar se o usuários fez mais de três saques

        # AS VERIFICAÇÕES ABAIXO SÃO FEITAS EM ORDEM, SEGUINDO A LÓGICA DO PROGRAMA 

        if excedeu_saque: # caso o valor digitado seja maior que o saldo disponível
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite: # caso o valor digitado seja maior que R$500,00
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES: # caso o usuário tenha feito mais de três saques
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:  # VALOR DO SAQUE DESEJADO PELO CLIENTE DO BANCO
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso! Efetuado {numero_saques} saque(s) diários.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("Extrato")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")


    elif opcao == "4":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
