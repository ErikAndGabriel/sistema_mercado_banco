import os
import random
import time 
import json 

class EntrarAdmin:
    def __init__(self, senha="Erik2008", usuario="Erik Lima"):

        self.usuario = usuario 
        self.senha = senha

    def Entrar(self, senha, usuario):
        tentativas = 3
        if self.usuario == usuario and self.senha == senha:
            print("esse usuario existe")
            verificaçao = random.randint(1001, 10001)
            with open("verificacao.txt", "w") as arq:
                json.dump(verificaçao, arq)

            verificacao_usuario = int(input("codigo de verificaçao: "))

            if int(verificaçao) == verificacao_usuario:
                print("bem vindo")
                tentativas = 3

            else:
                print("envalido")
                tentativas -= 1
                if tentativas <= 0:
                    print("bloqueado")
                    exit()

        else:
            print("senha ou usuario invalido")

eu = EntrarAdmin("Erik2008", "Erik Lima")
eu.Entrar("Erik2008", "Erik Lima")
