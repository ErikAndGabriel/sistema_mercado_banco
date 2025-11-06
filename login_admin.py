import os 
from admin_cadastrar import EntrarAdmin

def clear():
    os.system('clear')

def menu():
    while True:
        try:
            clear()
            print("===========================")
            print("[1] entrar")
            print("[2] sair")
            print("===========================")
            escolha = int(input("\nescolha: "))

            if escolha == 1:
                usuario = input("nome de usuario: ")
                senha = input("a senha: ")
                testativa = EntrarAdmin(usuario, senha)
                testativa.Entrar(usuario, senha)
                clear()
                continue

            elif escolha == 2:
                exit()

            else:
                input("escolha imvalida!, precione [ENTER]")
                clear()
                continue

        except ValueError:
            input("somente numeros, precione [ENTER]")
            clear()
            continue

menu()


            
