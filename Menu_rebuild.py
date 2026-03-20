import os
import time
os.system("cls")
from datetime import datetime
data = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M")
sair = False
back = False

#Início do programa
name = input("Digite seu nome: ")
while True:
    print(f"""Início do atendimento de {name}: {data} as {hora}
===================  Menu  ======================
     
Código            Prato                Valor
1---------------  Picanha  ----------- R$25,00
2---------------  Lasanha  ----------- R$20,00 
3---------------  Strogonoff---------- R$18,00
4---------------  Bife Acebolado  ---- R$15,00
5---------------  Pão com Ovo  ------- R$5,00
""")
    codigo = int(input(f"O que pedira hoje {name}: "))

    match codigo:
        case 1:
            prato1 = ("Picanha")
            valor1 = float(25.00)
            print("Você escolheu Picanha")
        case 2:
            prato1 = ("Lasanha")
            valor1 = float(20.00)
            print("Você escolheu Lasanha") 
        case 3:        
            prato1 = ("Strogonoff")
            valor1 = float(18.00)
            print("Você escolheu strogonoff")
        case 4:        
            prato1 = ("Bife Acebolado")
            valor1 = float(15.00)
            print("Você escolheu Bife Acebolado")
        case 5:        
            prato1 = ("Pão com Ovo")
            valor1 = float(5.00)
            print("Você escolheu Pão com Ovo")
        case _:
            print("Codigo Invalido")
            print("Tente Novamente")
            time.sleep(2)
            continue
         
    quantidade = int(input("Quantidade: "))
    if quantidade >= 2 or quantidade == 1:
        total1 = valor1 * quantidade
    else:
        print("Numero inválido")
        print("Tente novamente")
        continue  
    os.system("cls")
    while True:
        print(f"""Pedido de: {name}
   Prato       Unidade        Valor

1- {prato1}     {quantidade}              {valor1:.2f}     

Total: R${total1:.2f}
""")
        confirmação = int(input("""Seu pedido está correto ?
1- Sim
2- Não
"""))
        if confirmação == 1:
            os.system("cls")
            print("Seguindo atendimento")
            sair = True
            break
        if confirmação == 2:
            os.system("cls")
            print("Por favor refaça o pedido")
            time.sleep(2)
            back = True
            break
        else:
            os.system("cls")
            print("Opção invalida")
            print("Tente novamente")
            time.sleep(2)
            os.system("cls")
    if sair:
        break
    if back:
        os.system("cls")
        continue
    

        
os.system("cls")
while True:          
    pedido2 = int(input("""Gostaria de pedir mais algo ?
1- Sim
2- Não
"""))

    if pedido2 == 1:
        while True:
            os.system("cls")
            print(f"""
    ===================  Menu  ======================
        
    Código            Prato                Valor
    1---------------  Picanha  ----------- R$25,00
    2---------------  Lasanha  ----------- R$20,00 
    3---------------  Strogonoff---------- R$18,00
    4---------------  Bife Acebolado  ---- R$15,00
    5---------------  Pão com Ovo  ------- R$5,00
    """)
            codigo2 = int(input("Digite seu segundo pedido: "))

            match codigo2:
                case 1:
                    prato2 = ("Picanha")
                    valor2 = float(25.00)
                    print("Você escolheu Picanha")
                case 2:        
                    prato2 = ("Lasanha")
                    valor2 = float(20.00)
                    print("Você escolheu Lasanha") 
                case 3:        
                    prato2 = ("Strogonoff")
                    valor2 = float(18.00)
                    print("Você escolheu strogonoff")
                case 4:        
                    prato2 = ("Bife Acebolado")
                    valor2 = float(15.00)
                    print("Você escolheu Bife Acebolado")
                case 5:        
                    prato2 = ("Pão com Ovo")
                    valor2 = float(5.00)
                    print("Você escolheu Pão com Ovo")
                case _:
                    print("Codigo Inválido")
                    print("Tente novamente")
                    time.sleep(2)
                    continue

            os.system("cls")        

            quantidade2 = int(input("Quantidade: "))
            if quantidade2 >= 2 or quantidade == 1:
                total2 = valor2 * quantidade2
                final = total1 + total2
            else:
                print("Quantidade Inválida")
                print("Tente novamente")
                continue
            
            while True:
                print(f"""Pedido de: {name}
    Prato       Unidade        Valor

1- {prato1}   {quantidade}              R${total1:.2f}
2- {prato2}   {quantidade2}              R${total2:.2f}          

Total: R${final:.2f}
""")
                confirmação3 = int(input("""Seu pedido está correto ?
1- Sim
2- Não
"""))
                if confirmação3 == 1:
                    os.system("cls")
                    print("Proseguindo para pagamento")
                    sair = True
                    os.system("cls")
                    break
                if confirmação3 == 2:
                    os.system("cls")
                    print("Por favor refaça o pedido")
                    time.sleep(2)
                    back = True
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Opção inválida")
                    print("Por favor tente novamente")
                    time.sleep(2)
                    os.system("cls")
                    continue
            if sair:
                break
            if back:
                continue
        
    if pedido2 == 2:
        print("Seguindo para pagamento")
        time.sleep(2)
        break
    else:
        print("Opção inválida")
        print("Tente novamente")
        time.sleep(2)
        continue
while True:
    pagamento = int(input("""Qual a forma de pagamento: 
1- Cartão Crédito
2- Cartão Débito
3- Ticket
4- Pix
5- Dinheiro
"""))
    print()

    match pagamento:
        case 1|2|3:
            os.system("cls")
            print("Finaliza o pagamento na maquina")
            break
        case 4:
            os.system("cls")
            print("""Aguarde a geração do QR code e prossiga para o pagamento.
Após a confirmação seu pedido sera enviado para
a cozinha.""")
            break
        case 5:
            os.system("cls")
            print("Dirija-se ao caixa para finalizar o pedido.")
            break
        case _:
            os.system("cls")
            print("Opção inválida")
            print("Por favor tente novamente")
            time.sleep(2)
            os.system("cls")
            continue
            
print(f"{name}, obrigado pela preferencia, volte sempre :)")

def now():
    return datetime.now().strftime("%d/%m/%Y")
def agora():
    return datetime.now().strftime("%H:%M:%S")

print(f"Atendimento encerrado: {now} as {agora}")