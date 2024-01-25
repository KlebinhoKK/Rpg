# rpgv4

# criar personagem
    # escolher raça
        # humano
            # força maior, e status padrão
        # Anão
            # velocidade reduzida, força reduzida, passa por lugares pequenos, buff de ferraria, maior defesa
        # elfo
            # bonus de conhecimentos da floresta e de magia
        # roger
def clear_terminal():
    import os
    print("\n" * os.get_terminal_size().lines)
import time
print("Seja bem vindo a aventura de...")
time.sleep(2)
nome_jogador = input(f"???: A é qual é seu nome? \n meu nome é ")
time.sleep(2)


class atributos:
    def __init__(self, vida_jogador, dano_jogador, velocidade_jogador, conh_magia_jogador, ferraria):
        self.vida_jogador = vida_jogador
        self.dano_jogador = dano_jogador
        self.velocidade_jogador = velocidade_jogador
        self.conh_magia_jogador = conh_magia_jogador
        self.ferraria = ferraria   


while True:    
    escolha_d_raca = input("\nE qual de qual raça você quer ser? \n1-humano\n   -força maior\n   -status basicos\n2-Anão\n   -Velocidade reduzida\n   -Força reduzida\n   -Vida maior\n   -passa por lugares pequenos\n   -fabrição na ferraria liberado\n3-Elfo\n   -Conhecimento em magia\n   -conhecimento da floresta\n   -status basicos\nSua escolha:")
    raca = ""
    if escolha_d_raca == "1":
        raca = "Humano"
        status_jogador = atributos(100, 15, 10, 0, False)
        break
    elif escolha_d_raca == "2":
        raca = "Anão"
        status_jogador = atributos(130, 6, 6, 0, True)
        break
    elif escolha_d_raca == "3":
        raca = "Elfo"
        status_jogador = atributos(100, 10, 10, 10, False)
        break
    else:
        time.sleep(1)
        print("Insira uma raça valida")
        time.sleep(2)

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
print(f"{nome_jogador}: Pra aonde vou agora?")
time.sleep(2)
print(f"{nome_jogador}: Ó tem uma cidade logo ali na frente")
time.sleep(2)
import random
senha = random.randint(34566, 94563)
cultista_morto = False
print("---Na cidade---")

dia = 1
tempo = "dia"
    # cidade
        # ferreiro          
        # lojas
        # cultos
            # senha do tinhoso
                # aleatoria toda nova vez
        # escolas de magia
            # enem -> tira nota boa -> escola de graça
            # enem -> tira nota ruim -> a cada 10 aula
            # enem uma vez a cada 60 dias
def ferreiro():
    time.sleep(2)
    print("---Na ferraria---")
    decisao = input("O que deseja fazer?\n 1-Falar com o ferreiro\n 2-Forjar\n 3-Sair\nEscolha:")
    if decisao == "1" and dia <= 5:
        print("Ferreiro: Se deseja forjar alguma arma volte outro dia estou sem suprimentos")
        decisao2 = input("\n1-Sabe quando chega novos suprimentos?      2-Ok,Obrigado\nEscolha:")
        if decisao2 == "1":
            print(f"Ferreiro: provavelmente daqui a {5 - dia} dias")
        elif decisao2 == "2":
            clear_terminal()
            print("a") # voltar para cidade
    elif decisao =="2":
        print(f"Ferreiro: provavelmente daqui a {5 - dia} dias")
    elif decisao == "3":
        clear_terminal()
        print("a") # voltar para cidade
ferreiro()
def culto():
    time.sleep(1)
    print("---Nos becos---")
    time.sleep(1)
    print("Você procura por algo nos becos da Vila...")
    time.sleep(2)
    print("Você acha uma porta escondida entre os becos")
    decisao = input("Oque deseja fazer?\n 1-Bater na porta      2-Sair\nEscolha:")
    if cultista_morto == False:
        if decisao == "1":
            print("?: Uh.. Quem bateu na porta?")
            time.sleep(4)
            print("?: Quem é você? O que esta fazendo aqui?\n")
            input(f"1-Eu estava passando por aqui e achei essa porta      2-Nada não, ja estou saindo\n Escolha:")
            time.sleep(2)
            print("ENTÃO VAZA, NÃO TEM O QUE VOCÊ VER AQUI")
            print("a") # voltar para cidade
        elif decisao == "2":
            print("a") # voltar para cidade
    elif cultista_morto == True:
        print("?: Uh.. Quem bateu na porta?")
        time.sleep(4)
        print("?: Quem é você? O que esta fazendo aqui?\n")
        input(f"1-Eu estava passando por aqui e achei essa porta      2-Nada não, ja estou saindo\n3-Sou {nome_cultista} Escolha:")









# iniciação a aventura 
    # escolher classe
        # mago 
        # guerreiro
        # arqueiro

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



# status, armas e armaduras do personagem



# escolher local
    # cidade
        # ferreiro
        # lojas
        # cultos
        # escolas de magia
    # floresta 
        # monstros
        # aldeias 
        # zona de perigo em geral

#  sitema de combate
    # vida
    # ataques
    # ouro
    # nives/xp
    # pontos de habilidade

# pos batalha 
    # descançar
    # inventario
    # equipamentos 
