# rpgv4
import time
# clear terminal
def clear_terminal():
    import os
    os. system('cls')
dia = 5

def ferreiro():
    time.sleep(2)
    clear_terminal()
    print("---Na ferraria---")
    decisao = input("O que deseja fazer?\n 1-Falar com o ferreiro\n 2-Forjar\n 3-Sair\nEscolha:")
    if decisao == "1" and dia <= 5:
        time.sleep(1)
        while True:
            print("Ferreiro: Se deseja forjar alguma arma volte outro dia estou sem suprimentos")
            decisao2 = input("\n1-Sabe quando chega novos suprimentos?      2-Ok,Obrigado\nEscolha:")
            if decisao2 == "1":
                time.sleep(2)
                print(f"Ferreiro: provavelmente daqui a {5 - dia} dias")
                time.sleep(5)
                ferreiro()
                break
            elif decisao2 == "2":
                time.sleep(2)
                cidade()
                break
            else:
                time.sleep(1)
                print("Insira uma raça valida")
            time.sleep(2)
    elif decisao =="2":
        print("em desenvolvimento")
        time.sleep(3)
        cidade()
    elif decisao == "3":
        time.sleep(3)
        cidade()
    else:
        ferreiro()
# Cidade/menu
def cidade():
    clear_terminal()
    print("---Na cidade---")
    print(f"\nVejamos, oque posso fazer agora")
    decisao = input("1 - Ir a ferraria\n2 - Ver as lojas\n3 - ir a academia de magia\n4 - Ir aos becos")
    if decisao == "1":
        ferreiro()
cidade()

