import random

monstros = ([
    {
        "nome": "Basilisco",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 120,
            "ataque": 15,
            "defesa": 20
        }
    },
    {
        "nome": "Cultista",
        "tipo": "Humano",
        "atributos": {
            "vida": 100,
            "ataque": 15,
            "defesa": 18
        }
    },
    {
        "nome": "Cerberus",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 180,
            "ataque": 22,
            "defesa": 22
        }
    },
    {
        "nome": "Grifo",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 140,
            "ataque": 18,
            "defesa": 16
        }
    },
    {
        "nome": "Quimera",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 160,
            "ataque": 20,
            "defesa": 25
        }
    },
    {
        "nome": "Manticora",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 130,
            "ataque": 23,
            "defesa": 14
        }
    },
    {
        "nome": "Kraken",
        "tipo": "Criatura Marinha",
        "atributos": {
            "vida": 220,
            "ataque": 30,
            "defesa": 28
        }
    },
    {
        "nome": "Ciclope",
        "tipo": "Gigante",
        "atributos": {
            "vida": 180,
            "ataque": 28,
            "defesa": 20
        }
    },
    {
        "nome": "Banshee",
        "tipo": "Fantasma",
        "atributos": {
            "vida": 100,
            "ataque": 25,
            "defesa": 12
        }
    },
    {
        "nome": "Medusa",
        "tipo": "Criatura Mítica",
        "atributos": {
            "vida": 150,
            "ataque": 21,
            "defesa": 18
        }
    },
    {
        "nome": "Dragão de Fogo",
        "tipo": "Dragão",
        "atributos": {
            "vida": 100,
            "ataque": 20,
            "defesa": 15
        }
    },
    {
        "nome": "Golem de Pedra",
        "tipo": "Elemental",
        "atributos": {
            "vida": 150,
            "ataque": 10,
            "defesa": 25
        }
    },
    {
        "nome": "Espectro Sombrio",
        "tipo": "Fantasma",
        "atributos": {
            "vida": 80,
            "ataque": 18,
            "defesa": 10
        }
    }
])
def monstro():
    global nome
    global tipo
    global atributos
    # Acessando o terceiro monstro na lista
    monstro = monstros[random.randint(0,12)]

    # Acessando informações separadamente
    nome = monstro["nome"]
    tipo = monstro["tipo"]
    atributos = monstro["atributos"]

    # Imprimindo as informações
    print("Nome:", nome)
    print("Tipo:", tipo)
    print("Atributos:", atributos)


monstro()

print("Nome:", nome)
print("Tipo:", tipo)