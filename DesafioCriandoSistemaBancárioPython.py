LIMITE_DIARIO = 1500
LIMITE_SAQUE = 3
saldoAtual = saldoInicial = 2000
valorDepositado = []
valorSacado = []
valorMaxDeposito = 10000

def sacar(valorSaque):
    global saldoAtual, valorSacado
    if valorSaque <= saldoAtual and len(valorSacado) < LIMITE_SAQUE and sum(valorSacado) + valorSaque <= LIMITE_DIARIO:
        saldoAtual -= valorSaque
        valorSacado.append(valorSaque)
        print("Saque realizado com sucesso")
    else:
        print("Operação inválida")

def depositar(valorDeposito):
    global saldoAtual, valorDepositado
    saldoAtual += valorDeposito
    valorDepositado.append(valorDeposito)
    print("Deposito realizado com sucesso")

def extrato():
    print(f"Saldo Inicial: {saldoInicial}")
    print(f"Valores sacados: {valorSacado}")
    print(f"Valores depositados: {valorDepositado}")
    print(f"Saldo Atual: {saldoAtual}")

while True:
    menu = int(input('''Digite a Opcao desejada:
             (1) Saque
             (2) Deposito
             (3) Extrato
             (0) Sair             
             '''))

    if menu == 1:
        valorSaque = float(input("Digite o valor para saque: "))
        if valorSaque <= 500:
            sacar(valorSaque)
        else:
            print("Valor deve ser Menor ou igual a 500.")

    elif menu == 2:
        valorDeposito = float(input("Digite o valor para deposito: "))
        if valorDeposito <= valorMaxDeposito and valorDeposito > 0:
            depositar(valorDeposito)
        else:
            print(f"Operação inválida")

    elif menu == 3:
        extrato()

    elif menu == 0:
        break

    else:
        print("Digite uma opcao valida")
