import json 
import os

def clear():
    os.system('clear')

def carregar():
    with open("produtos.json", "r") as carregar:
        json.load(carregar)

def salvar_dados(dados):
    with.opne("produtos.json", "w") as salvar:
        return json.dump(dados, salvar, indent=4)

class Admin:
    def __init__(self, nome, valor, tipo):
        self.nome = nome 
        self.valor = valor
        self.tipo = tipo 

    def MenuAdmin(self):
        while True:
            carregar()
            try:
                print("[1] adicionar produto")
                print("[2] remover produto")
                print("[3] sair ")
                escolha = int(input("escolha: "))

                if escolha == 1:
                    nome = input("nome do produto: ")
                    tipo = input("tipo do produto: ")
                    try:
                        valor = float(input("valor do produto"))
                    except ValueError:
                        print("somente numeros")
                    dados = 
                    salvar_dados()
