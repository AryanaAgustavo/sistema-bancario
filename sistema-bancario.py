menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor_depositado = float(input("Informe o valor a ser depositado: "))

        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito de R$ {valor_depositado:.2f}\n"
        else:
            print("Operação não realizada. Valor informado é inválido")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor a ser sacado: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Você já fez a quantidade de saques limite para o dia")
        elif valor_saque > saldo:
            print("Operação não concluida. Você não possui saldo suficiente")
        elif valor_saque > limite:
            print("Operação não concluida. O valor de saque excede o limite")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("Operação n]ao concluída. Valor informado é inválido.")

    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Tente novamente.")
