# rpgv4
import time
# # clear terminal
def clear_terminal():
    import os
    os. system('cls')

# # Set de atributos
class atributos:
    def __init__(self, vida_jogador, dano_jogador, velocidade_jogador, conh_magia_jogador, ferraria):
        self.vida_jogador = vida_jogador
        self.dano_jogador = dano_jogador
        self.velocidade_jogador = velocidade_jogador
        self.conh_magia_jogador = conh_magia_jogador
        self.ferraria = ferraria   

# # escolher classe
class classe:
    def __init__(self, dano_magia, dano_distancia, dano_corpoacorpo):
        self.dano_magia = dano_magia
        self.dano_distancia = dano_distancia
        self.dano_corpoacorpo = dano_corpoacorpo
    
    def escolher_classe(self):
        while True:
            escolha_d_classe = input("Qual classe você deseja ser?\n1-Mago\n2-Guerreiro\n3-Arqueiro\nSua escolha: ")
            if escolha_d_classe == "1":
                dano_classe = classe(10,0,0)
                break
            elif escolha_d_classe == "2":
                dano_classe = classe(0,0,10)
                break
            elif escolha_d_classe == "3":
                dano_classe = classe(0,10,0)
                break
            else:
                time.sleep(1)
                print("Insira uma Classe valida")
                time.sleep(2)
        dano_classe = dano_classe

# # tempo
dia = 1
tempo = "dia"

# # # Localidades
    
# # loja
def loja():
    clear_terminal()
    time.sleep(1)
    print("---loja---")
# # escola de magia
def escola_d_magia():
    clear_terminal()
    time.sleep(1)
    print("---Na escola---")
  
# # ferreiro
def ferreiro():
    time.sleep(2)
    clear_terminal()
    time.sleep(1)
    print("---Na ferraria---")
    decisao = input("O que deseja fazer?\n 1-Falar com o ferreiro\n 2-Forjar\n 3-Sair\nEscolha: ")
    if decisao == "1" and dia <= 5:
        while True:
            time.sleep(1)
            print("Ferreiro: Se deseja forjar alguma arma volte outro dia estou sem suprimentos")
            decisao2 = input("\n1-Sabe quando chega novos suprimentos?      2-Ok,Obrigado\nEscolha: ")
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
                print("Insira uma opção valida")
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
  
# # set de coisas para cultista
import random
senha = random.randint(34566, 94563)
cultista_morto = True
cultistas = ["Carlos", "Fernanda", "Ricardo", "jorje", "João", "Larissa", "Pedro", "Bianca", "Felipe", "Gabriela", "Eduardo", "Isabel", "Miguel", "Thais", "Arthur", "Marina", "Rodrigo", "Beatriz", "Daniel", "Laura"]
nome_cultista = random.choice(cultistas)
culto_liberado = False
# # culto
def entrar_culto():
    clear_terminal()
    time.sleep(1)
    print("---Nos becos---")
    time.sleep(1)
    print("Você procura por algo nos becos da Vila...")
    time.sleep(2)
    print("Você acha uma porta escondida entre os becos")
    decisao = int(input("Oque deseja fazer?\n 1-Bater na porta      2-Sair\nEscolha: "))
    if cultista_morto == False:
        if decisao == 1:
            time.sleep(1)
            print("?: Uh.. Quem bateu na porta?")
            time.sleep(4)
            print("?: Quem é você? O que esta fazendo aqui?\n")
            time.sleep(1)
            input(f"1-Eu estava passando por aqui e achei essa porta      2-Nada não, ja estou saindo\n Escolha: ")
            time.sleep(2)
            print("?: ENTÃO VAZA, NÃO TEM O QUE VOCÊ VER AQUI")
            time.sleep(3)
            cidade()
        elif decisao == 2:
            time.sleep(1)
            cidade()
        else:
            entrar_culto()
    elif cultista_morto == True and decisao == 1:
        print("?: Uh.. Quem bateu na porta?")
        time.sleep(4)
        while True:
            print("?: Quem é você? O que esta fazendo aqui?\n")
            time.sleep(1)
            decisao2 = input(f"1-Eu estava passando por aqui e achei essa porta      2-Nada não, ja estou saindo\n3-Sou {nome_cultista}\n Escolha: ")
            if decisao2 == "1":
                time.sleep(2)
                print("?: ENTÃO VAZA, NÃO TEM O QUE VOCÊ VER AQUI")
                time.sleep(3)
                cidade()
                break
            if decisao2 == "2":
                time.sleep(2)
                print("?: ENTÃO VAZA, NÃO TEM O QUE VOCÊ VER AQUI")
                time.sleep(3)
                cidade()
                break
            elif decisao2 == "3":
                time.sleep(1)
                print("?: Qual é a senha?")
                time.sleep(2)
                print(f"{nome_jogador}: A senha é {senha}")
                time.sleep(2)
                print("Homem de Capuz: Ok, pode entrar")
                culto_liberado = True
                break
            else:
                time.sleep(1)
                print("Insira uma opção valida")
                time.sleep(2)


# # Cidade/menu
def cidade():
    clear_terminal()
    time.sleep(1)
    print("---Na cidade---")
    print(f"\nVejamos, oque posso fazer agora")
    decisao = input("1 - Ir a ferraria\n2 - Ver as lojas\n3 - ir a academia de magia\n4 - Ir aos becos\nEscolha: ")
    if decisao == "1":
        ferreiro()
    elif decisao == "2":
        loja()
    elif decisao == "3":
        escola_d_magia()
    elif decisao == "4":
        entrar_culto()
    else:
        cidade()


# dialogo de introdução
print("Seja bem vindo a aventura de...")
time.sleep(2)
nome_jogador = input(f"???: A é qual é seu nome? \n meu nome é ")
time.sleep(2)
# escolha da raça 
while True:    
    escolha_d_raca = input("\nE qual de qual raça você quer ser? \n1-humano\n   -força maior\n   -status basicos\n2-Anão\n   -Velocidade reduzida\n   -Força reduzida\n   -Vida maior\n   -passa por lugares pequenos\n   -fabrição na ferraria liberado\n3-Elfo\n   -Conhecimento em magia\n   -conhecimento da floresta\n   -status basicos\nSua escolha: ")
    raca = ""
    if escolha_d_raca == "1":
        raca = "Humano"
        status_jogador = atributos(100, 15, 10, 0, False)
        clear_terminal()
        break
    elif escolha_d_raca == "2":
        raca = "Anão"
        status_jogador = atributos(130, 6, 6, 0, True)
        clear_terminal()
        break
    elif escolha_d_raca == "3":
        raca = "Elfo"
        status_jogador = atributos(100, 10, 10, 10, False)
        clear_terminal()
        break
    else:
        time.sleep(1)
        print("Insira uma raça valida")
        time.sleep(2)
    clear_terminal()

# # dialogo inicial
time.sleep(2)
print("\n???: Oh obrigado, então recomeçando")
time.sleep(2)
print(f"Seja bem vindo a aventura de {nome_jogador}")
time.sleep(2)
print(f"{nome_jogador}: Só um minuto, Quem é você?")
time.sleep(2)

print("???: No momento não interessa pra Você, algum dia você acaba descobrindo")
time.sleep(2)
print("???: Mas agora o resto é com você, só não morre ok?")
time.sleep(2)
print(f"{nome_jogador}: Ok...")
time.sleep(2)
clear_terminal()
print(f"{nome_jogador}: Pra aonde vou agora?")
time.sleep(2)
print(f"{nome_jogador}: Ó tem uma cidade logo ali na frente")
time.sleep(2)
cidade()
    
# floresta 
def floresta():
    clear_terminal()
    Locais = ['Ruinas', 'Campos', 'Floresta']
    local_esc = random.choice(Locais)
    time.sleep(2)
    print("---Na floresta---")
    time.sleep(1)
    decisao = input(f'O que deseja fazer agora?\n1 - Explorar{local_esc}\n2 - Explorar por recursos\n 3 - Voltar para a cidade\nEscolha:')
    if decisao == "1":
        combate()
    elif decisao == "2":
        pass
    elif decisao == "3":
        time.sleep(1)
        cidade()
    else:
        floresta()

# iniciação a aventura 

# status, armas e armaduras do personagem

#  sitema de combate
def combate():
    clear_terminal()
    import Rpg.monstros as monstros
    time.sleep(1)
    print('---Em combate---')
    time.sleep(1)
    print('Você encontrou:')
    monstros.monstro()

# vida
# ataques
# ouro
# nives/xp
# pontos de habilidade




# pos batalha 
    # descançar
    # inventario
    # equipamentos 
