Inicio = """

[1] Deposito
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
cont = 0

while True:
    opcao = input(Inicio)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: "))

        if valor_deposito >= 0:
            
            saldo += valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print(f"Saldo atual: {saldo}")
        print("Deposito Efetuado")
        
    elif opcao == "2":
        valor_saque = int(input("Digite valor que deseja sacar: "))
                
        
        if cont < LIMITE_SAQUES:
            
            if valor_saque > 0:
                
                if valor_saque <= saldo:
                    
                    if valor_saque <= limite:
                        
                        saldo -= valor_saque
                        extrato += f"Saque: R$ {valor_saque:.2f}\n"
                        print("Saque efetuado!")
                        cont += 1
                        
                    else:
                        print("Valor excede o limite!")
                else:
                    print("Saldo insuficiente!")
            else:
                print("Valor invalido, digite um valor positivo!")
        else:
            print("Numero limite de saques excedido!")
        print("Processo Finalizado")
        
    elif opcao == "3":
        print("\n____________________Extrato____________________")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("_______________________________________________")

    elif opcao == "0":
        break
    
    else:
        print("Operção Invalida.")
