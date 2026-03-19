import os
os.system("cls")
from datetime import datetime
data = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M")

#Início do programa
name = input("Digite seu nome: ")

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
         
quantidade = int(input("Quantidade: "))
if quantidade >= 2:
    total1 = valor1 * quantidade
    os.system("cls")
    print(f"""Pedido de: {name}
   Prato       Unidade

1- {prato1}     {quantidade}       R${total1:.2f}
""")
    confirmação = int(input("""Seu pedido está correto ?
1- Sim
2- Não
"""))
    os.system("cls")
    if confirmação == 1:
        print("Seguindo atendimento")
    if confirmação == 2:
        print("Por favor refaça o pedido")
        exit()
    if confirmação == 0 or confirmação >= 3:
        print("Opção invalida") 
else:
    os.system("cls")
    quantidade = 1 
    print(f"""Pedido de: {name}
   Prato       Unidade
   
1- {prato1}     {quantidade}       R${valor1:.2f}
""")
    confirmação2 = int(input("""Seu pedido está correto ?
1- Sim
2- Não
"""))
    if confirmação2 == 1:
        print("Seguindo atendimento")
    if confirmação2 == 2:
        print("Por favor refaça o pedido")
        exit()
    if confirmação2 == 0 or confirmação2 >= 3:
        print("Opção invalida")
os.system("cls")          
pedido2 = int(input("""Gostaria de pedir mais algo ?
1- Sim
2- Não
"""))

if pedido2 == 1:
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
        print("Codigo Invalido")

os.system("cls")        

quantidade2 = int(input("Quantidade: "))
if quantidade2 >= 2:
    total2 = valor2 * quantidade2
    final = total1 + total2
    print(f"""Pedido de: {name}
   Prato       Unidade

1- {prato1}   {quantidade}          R${total1}
2- {prato2}   {quantidade2}         R${total2}          

Total: R${final}
""")

else:
    os.system("cls")
    quantidade = 1
    final = total1 + valor2 
    print(f"""Pedido de: {name}
   Prato       Unidade

1- {prato1}   {quantidade}          R${total1}
2- {prato2}   {quantidade2}         R${valor2}          

Total: R${final}""")
print()

confirmação3 = int(input("""Seu pedido está correto ?
1- Sim
2- Não
"""))
if confirmação3 == 1:
    print("Proseguindo para pagamento")
if confirmação3 == 2:
    print("Por favor refaça o pedido")
if confirmação3 == 0 or confirmação3 >= 3:
    print("Número invalido")
    exit()
if pedido2 == 2:
    print("Seguindo para pagamento")
if pedido2 == 0 or pedido2 >= 3:
    print("Opção invalida")
        
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
        print("Finaliza o pagamento na maquina")
    case 4:
        print("""Aguarde a geração do QR code e prossiga para o pagamento.
Após a confirmação seu pedido sera enviado para
a cozinha.""")
    case 5:
        print("Dirija-se ao caixa para finalizar o pedido.")
    case _:
        print("Forma de pagamento invalida, por favor tente novamente")
        
print(f"{name}, obrigado pela preferencia, volte sempre :)")

def now():
    return datetime.now().strftime("%d/%m/%Y")
def agora():
    return datetime.now().strftime("%H:%M:%S")

print(f"Atendimento encerrado: {now} as {agora}")