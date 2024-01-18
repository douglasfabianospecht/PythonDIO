

def sacar(*, valorSaque, totalSaque):
    global saldoAtual, valorSacado, LIMITE_SAQUE, totalSaques
    if (valorSaque <= saldoAtual):        
        if (sum(valorSacado) + valorSaque <= LIMITE_DIARIO):
            saldoAtual -= valorSaque
            valorSacado.append(valorSaque)
            print("Saque realizado com sucesso")       
        else: 
            print("limites atingidos")
    else:
        print("voce nao possui saldo")

def depositar(valorDeposito, /):
    global saldoAtual, valorDepositado
    saldoAtual += valorDeposito
    valorDepositado.append(valorDeposito)
    print("Deposito realizado com sucesso")

def extrato():
    print(f"Saldo Inicial: {saldoInicial}")
    print(f"Valores sacados: {valorSacado}")
    print(f"Valores depositados: {valorDepositado}")
    print(f"Saldo Atual: {saldoAtual}")
    
def criarUsuario(usuarios):
    cpf = input("Digite apenas os numeros do CPF: ")
    usuario = filtrarUsuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Ja existe usuario com esse CPF! @@@")
        return
    nome = input("Digite o nome do Usuario: ")
    dataNascimento = input("Digite a data de nascimento do Usuario: ")
    endereco =  input("Digite o endereco do Usuario: ")
    usuarios.append({"nome": nome, "cpf": cpf, "dataNascimento": dataNascimento,  "endereco": endereco})
   
    print("Usuario cadastrado")
    
def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Digite apenas os numeros do CPF: ")
    usuario = filtrarUsuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta Cadastrada com Sucesso")
        return {"agencia": agencia, "numeroConta": str(numeroConta), "usuario": usuario}
    print("\n@@@ Usuario nao encontrato! @@@")
    
        
def filtrarUsuario(cpf, usuarios):
    usuarioLocalizdo= [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarioLocalizdo[0] if usuarioLocalizdo else None

def listarContas(contas):
    for conta in contas:
        linha = f'''
            Agencia: \t{conta['agencia']} 
            Conta: \t{conta['numeroConta']} 
            Titular: \t{conta['usuario']['nome']}
        
        '''
        print(linha)

def main():
    LIMITE_DIARIO = 1500
    LIMITE_SAQUE = 3
    saldoAtual = saldoInicial = 2000
    valorDepositado = []
    valorSacado = []
    valorMaxDeposito = 10000
    totalSaques = 1
    usuarios=[]
    contas =[]
    AGENCIA = "0001"
    
    while True:
        menu = int(input('''Digite a Opcao desejada:
                (1) Saque
                (2) Deposito5
                (3) Extrato
                (4) Cadastrar Usuario
                (5) Cadastrar Conta 
                (6) Listar contas
                (0) Sair             
                '''))

        if menu == 1:
            #print(f"total saques externo {totalSaques}")
            if totalSaques <= LIMITE_SAQUE:            
                valorSaque = float(input("Digite o valor para saque: "))
                if valorSaque <= 500:
                    totalSaques +=1
                    sacar(valorSaque=valorSaque, totalSaque=totalSaques)            
                    #print(f"total saques interno {totalSaques}")
                else:
                    print("Valor deve ser Menor ou igual a 500.")
            else: 
                print("limites atingidos")

        elif menu == 2:
            valorDeposito = float(input("Digite o valor para deposito: "))
            if valorDeposito <= valorMaxDeposito and valorDeposito > 0:
                depositar(valorDeposito)
            else:
                print(f"Operação inválida")

        elif menu == 3:
            extrato()
        
        elif menu == 4:        
            criarUsuario(usuarios)

        elif menu == 5:        
            numeroConta = len(contas) + 1 
            conta = criarConta(AGENCIA, numeroConta, usuarios)
            if conta:
                contas.append(conta)
        
        elif menu == 6:        
            listarContas(contas)
                
        elif menu == 0:
            break

        else:
            print("Digite uma opcao valida")

main()