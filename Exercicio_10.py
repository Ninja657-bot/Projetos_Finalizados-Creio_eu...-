import os 
import time
os.system("cls")

lista = []
voltar = False

print("- BANCO DE DADOS DOS CIDADÃOS -")
print()

while True:
    opcao = (input("""1 | Mostrar Pessoas cadastradas 
2 | Exibir resultados
3 | Sair
"""))
    match opcao:
        case "1":
            while True:
                os.system("cls")    
                if not lista:
                    os.system("cls")
                    print("Nenhuma pessoa cadastrada.")
                    print()
                    opcao = (input("""1 | Para Adicionar Pessoa
2 | Para Voltar
"""))
                    match opcao:
                        case "1":
                            os.system("cls")
                            print("Digite os dados da pessoa")
                            nome = input("Nome: ")
                            idade = int(input("Idade: "))
                            while True:
                                sexo = input("Sexo (F ou M): ").lower()
                                if sexo == "f":
                                    sexo = "Feminino"
                                    break
                                if sexo == "m":
                                    sexo = "Masculino"
                                    break
                                else: 
                                    print("Opção inválida utilize apaenas F ou M")
                                    time.sleep(1)
                                    print("Tente Novamente")
                                    time.sleep(1.5)
                                    
                                    continue

                            salario = float(input("salario: "))
                            
                            pessoa = {
                            "nome": nome,
                            "idade": idade,
                            "sexo": sexo,
                            "salario": salario 
                            }
                            lista.append(pessoa)
                            os.system("cls")
                            continue
                        
                        case "2":
                            os.system("cls")
                            continue
                        
                        case _:
                            os.system("cls")
                            print("Oção Invalida")
                            print("Tente novamente")
                            time.sleep(2)
                            os.system("cls")
                            continue
                
                for i, pessoa in enumerate(lista, start=1):
                    print(f"\nPessoa {i}")
                    print(f"Nome: {pessoa['nome']}")
                    print(f"Idade: {pessoa['idade']}")
                    print(f"Sexo: {pessoa['sexo']}")
                    print(f"Salário: R${pessoa['salario']:.2f}")
                    print("-" * 20)
                    print()
                opcao = input("""1 | Adicionar Pessoa
2 | Remover Pessoa
3 | Voltar
""")
                if opcao == "1":
                    os.system("cls")
                    print("Digite os dados da pessoa")
                    nome = input("Nome: ")
                    idade = input("Idade: ")
                    while True:
                        sexo = input("Sexo (F ou M): ").lower()
                        if sexo == "f":
                            sexo = "Feminino"
                            break
                        if sexo == "m":
                            sexo = "Masculino"
                            break
                        else: 
                            print("Opção inválida utilize apenas F ou M")
                            print("Tente Novamente")
                            time.sleep(2)
                            os.system("cls")
                            continue

                    salario = float(input("salario: "))
                    
                    pessoa = {
                    "nome": nome,
                    "idade": idade,
                    "sexo": sexo,
                    "salario": salario 
                    }
                    lista.append(pessoa)
                    os.system("cls")
                    continue
                
                if opcao == "2":
                    remover = int(input("Digite o número da pessoa que deseja remover: "))

                    lista.pop(remover - 1)
                    time.sleep(2)
                    print("Pessoa Removida")
                    input("Presione ENTER para voltar")
                    os.system("cls")
                    continue
                
                if opcao == "3":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Opção Inválida")
                    print("Tente novamente")
                    os.system("cls")
                    continue   
        case "2":
            os.system("cls")
            soma_salarios = 0
            contador = 0

            if lista:
                for pessoa in lista:
                    soma_salarios += float(pessoa["salario"])
                    if pessoa["sexo"] == "Feminino" and float(pessoa ["salario"]) >= 5000:
                        contador += 1 
                
                    if lista:
                        media_salario = soma_salarios / len(lista)
                    else:
                        media_salario = 0
                        
                    pessoa_mais_velha = max(lista, key=lambda p: int(p["idade"]))
                    pessoa_mais_nova = min(lista, key=lambda p: int(p["idade"]))
            
                print(f"Média dos salários: {media_salario:.2f}")
                print(f"Mais velho(a): {pessoa_mais_velha['nome']} | {pessoa_mais_velha['idade']} anos")
                print(f"Mais Novo(a): {pessoa_mais_nova['nome']} | {pessoa_mais_nova['idade']} anos")
                print(f"Mulheres com Salário acima de R$5000,00: {contador}") 
                input("Presione ENTER para voltar")
                os.system("cls")
                continue
            else:
                os.system("cls")
                print("ERRO")
                print("Nenhuma pessoa cadastrada")
                time.sleep(2)
                os.system("cls")
                print("Voltando para o inicio")
                time.sleep(2)
                os.system("cls")
                continue
            
        case "3":
            print("Finalizando o programa")
            time.sleep(2)
            exit()
        case _:
            os.system("cls")
            print("Opção Inválida")
            print("Tente Novamente")
            time.sleep(2)
            os.system("cls")
            continue