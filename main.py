import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))

from academia import criar_mutante, treinar_mutante


def criar_json():
    caminho_json = os.path.join(base_dir, "mutantes.json") 
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as arquivo:
            json.dump({}, arquivo)
    caminho_json = os.path.join(base_dir, "missao.json") 
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as arquivo:
            json.dump({}, arquivo)
        
criar_json()
def menu():
    os.system("cls")
    print("Menu Principal")
    print("1 - Cadastrar Mutante")
    print("2 - Treinar Mutante")
    print("3 - Enviar para Missão")
    print("4 - Iniciar Batalha")
    print("5 - Visualizar Estatísticas")
    print("0 - Salvar e Sair")

    opcao = input("Digite a opção desejada: ")
    return opcao

while True:
    opcao = menu()
    match opcao:
        case "1":
            criar_mutante()
        case "2":
            treinar_mutante()
        case "3":
            print("Enviar para Missão")
            
        case "4":
            print("Iniciar Batalha")
        case "5":
            print("Visualizar Estatísticas")
        case "0":
            print("Salvar e Sair")
            break
        case _:
            print("Opção inválida")
            input("Pressione enter para continuar...")

