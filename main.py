import os
import json



base_dir = os.path.dirname(os.path.abspath(__file__))

from academia import criar_mutante, treinar_mutante, listar_mutante, editar_cadastro
from missao import Missao, iniciar_missao
from utils import adicionar_dados
from auth import autenticar, criar_conta

def criar_json():
    caminho_json = os.path.join(base_dir, "mutantes.json") 
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as arquivo:
            json.dump({}, arquivo)
    caminho_json = os.path.join(base_dir, "missao.json") 
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as arquivo:
            json.dump({}, arquivo)
    caminho_json = os.path.join(base_dir, "contas.json")
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as arquivo:
            json.dump({}, arquivo)
        
criar_json()
def menu_posautenticar():
    os.system("cls")
    print("Menu Principal")
    print("1 - Cadastrar Mutante")
    print("2 - Treinar Mutante")
    print("3 - Enviar para Missão")
    print("4 - Visualizar Estatísticas")
    print("5 - Adicionar Missão")
    print("6 - Editar cadastro de Mutante")
    print("0 - Salvar e Sair")

    opcao = input("Digite a opção desejada: ")
    return opcao

def menu_inicial():
    os.system("cls")
    print("Menu Principal")
    print("1 - entrar")
    print("2 - Criar Conta")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")
    return opcao

def pos_autenticar(informacoes):
    while True:
        opcao = menu_posautenticar()    
        match opcao:
            case "1":
                criar_mutante()
            case "2":
                treinar_mutante()
            case "3":
                iniciar_missao()
            case "4":
                listar_mutante()
            case "5":
                print("Adicionar Missão")
                descricao = input("Digite a descrição da missão: ")
                while True: 
                    try:
                        dificuldade = int(input("Digite a dificuldade da missão (1 mais facil - 5 mais dificil): "))
                        if dificuldade < 1 or dificuldade > 5:
                            print("Digite uma dificuldade entre 1 e 5!")
                            continue
                        else:
                            missao = Missao(descricao, dificuldade)
                            missao.todict()
                            adicionar_dados(missao.todict(), 'missao')
                            print("salvo com sucesso!")
                            input("Pressione enter para continuar...")
                            break
                    except ValueError:
                        print("Digite um valor numérico para a dificuldade!")
                        continue
            case "6":
                print("Editar cadastro de Mutante")
                editar_cadastro()
            case "0":
                print("Salvar e Sair")
                break
            case _:
                print("Opção inválida")
                input("Pressione enter para continuar...")

while True:
    opcao = menu_inicial()
    match opcao:
        case "1":
            informacoes = autenticar()
            if informacoes == False:
                continue
            else:
                pos_autenticar(informacoes)
        case "2":
            criar_conta()
        case "0":
            break
        case _:
            print("Opção inválida!")
            input("Pressione enter para continuar...")
