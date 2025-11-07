import json
import os 

def clear():
    os.system('clear')

def carregar():
    with open("produtos.json", "r") as arq:
        return json.load(arq)

class Caixa:
    def __init__(self, produto, quantidade):
        self.produto = produto 
        self.quantidade = quantidade 

    def Verificador(self):
        produtos = carregar()
        if self.produto in produtos:
            print("existe sim ")
            valor_unitario = float(produtos[self.produto]['valor'])
            valor_final = valor_unitario * self.quantidade
            print(f"{self.produto} X {self.quantidade} = {valor_final}")


        else:
            print("produto n existe na lista")
            return False

    def Menu(self):
        while True:
            try:
                clear()
                comprar = carregar()
                print("========= CAIXA =========")
                print("[1] comprar produtos")
                print("[2] cancelar produtos")
                print("[3] meu carrinho")
                print("[4] produtos atuais!")
                print("========================")
                escolha = int(input("\nescolha: "))
                if escolha == 1:
                    nome = input("nome do produto: ")
                    try:
                        qunatidade = int(input("quantidade: "))
                    except ValueError:
                        print("somente numeros na qunatidade!")
                        clear()
                        continue
                    funcionario = Caixa(nome, qunatidade)
                    funcionario.Verificador(nome, qunatidade)
            except ValueError:
                print("somente numeros")





eu = Caixa("banana", 8)
eu.Menu()
