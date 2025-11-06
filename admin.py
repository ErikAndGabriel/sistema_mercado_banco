import json 
import os
import random 
import time 

def clear():
    os.system('clear')

arquivo = "produto.json"

def carregar():
    with open("produtos.json", "r") as carregar:
        return json.load(carregar)

def salvar_dados(dados):
    with open("produtos.json", "w") as salvar:
        json.dump(dados, salvar, indent=4)

class Admin:
    def __init__(self, nome, valor, tipo, codigo):

        self.nome = nome 
        self.valor = valor
        self.tipo = tipo 
        self.codigo = codigo 

    def MenuAdmin(self):
        while True:
            clear()
            produtos = carregar()
            try:
                print("======================")
                print("[1] adicionar produto")
                print("[2] remover produto")
                print("[3] olhar lista")
                print("[4] sair ")
                print("=======================")
                escolha = int(input("escolha: "))

                if escolha == 1:
                    clear()
                    nome = input("nome do produto: ")
                    tipo = input("tipo do produto: ")
                    codigo = random.randint(1001, 10001)
                    codigos_existentes = [p['codigo'] for p in produtos.values()]
                    while codigo in codigos_existentes:
                        codigo = random.randint(1001, 10001)                                        
                    try:
                        valor = float(input("valor do produto: "))
                    except ValueError:
                        input("somente , precione [ENTER]")
                        clear()
                        continue     
                    novo = Admin(nome, valor, tipo, codigo)
                    produtos[novo.nome] = {
                        "nome": novo.nome,
                        "tipo": novo.tipo,
                        "codigo": novo.codigo,
                        "valor": f"{novo.valor:.2f}",
                        "moeda": "BRL"
                    }
                    salvar_dados(produtos)
                    input("criado com sucesso!, precione [ENTER]")
                    clear()
                    continue 
                
                elif escolha == 2:
                    clear()
                    nome = input("nome do produto: ") 
                    
                    if nome in produtos:
                        del produtos[nome]
                        salvar_dados(produtos)
                        input("produto removido!,precione [ENTER]")
                        clear()
                        continue 
                        
                    else:
                        input("nao existe, precione [ENTER]")
                        clear()
                        continue
                elif escolha == 3:
                    clear()
                    print("======================================================")
                    for chave, valor in produtos.items():
                        print(f"produto: {chave}  codigo: {valor['codigo']}  preço: {valor['valor']}")
                    print("======================================================")
                        
                    input("precione [Enter]")

                elif escolha == 4:
                    break

            except ValueError:
                print("somente numere")

