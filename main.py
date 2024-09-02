menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Deposito")
        depositar = float(input("Qual o valor que deseja depositar: "))
        if depositar > 0:
            saldo += depositar
            extrato.append(f'Depósito: R$ {depositar:.2f}')
            print("Deposito realizado com sucesso!")
        else:
            print("Deposito não realizado, pois não é permitido depósito com valor de zero ou negativos.\nTente novamente!")
    

    elif opcao == 2:
        print("Sacar")
        sacar = float(input("Qual o valor que deseja sacar: "))

        if sacar > 0:
            if (sacar > saldo):
                print("Saque não realizado, pois não tem saldo suficiente!")
            elif (sacar > limite):
                print("Saque não realizado, pois excede o limite diário!")
            elif (numero_saques >= LIMITE_SAQUES):
                print("Saque não realizado, pois excedeu o quantidade de saques permitidos!")
            else:
                saldo -= sacar
                numero_saques += 1
                extrato.append(f'Saque:- R$ {sacar:.2f}')

        else:
            print("Saque não realizado, pois não é permitido saques com valor de zero ou negativos.\nTente novamente!")
    
    
    elif opcao == 3:
        print("Extrato")
        if len(extrato) == 0:
            print('Não existem movimentações')
        else:
            print('\n'.join(extrato))
            print(f'\n\nSALDO: R${saldo:.2f}')


    elif opcao == 0:
        print("Obrigado pela preferência!")
        break

    else:
        print("Opção inválida, tente novamente")