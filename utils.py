import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))

caminho_json = os.path.join(base_dir, "dados.json") 

def carregar_dados():
    with open(caminho_json, "r") as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_dados(dados):
    # Ver como vai ser isso aqui
    pass
if __name__ == "__main__":
    print(carregar_dados())