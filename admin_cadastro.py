import random
import json 
from admin import Admin

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
                tentativas = 3
                admin = Admin("", "", "", "")
                admin.MenuAdmin()

            else:
                print("envalido")
                tentativas -= 1
                if tentativas <= 0:
                    print("bloqueado")
                    exit()

        else:
            print("senha ou usuario invalido")

