import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))



def carregar_dados(arquivo):
    """Carrega e retorna os dados de um arquivo JSON específico."""
    caminho_json = os.path.join(base_dir, f"{arquivo}.json") 
    with open(caminho_json, "r") as f:
        dados = json.load(f)
    return dados

def atualizar_dados(dicio, arquivo):
    """Atualiza os dados de um item específico no arquivo JSON.
    """
    #lembrar que todo id tem que ser string
    dados = carregar_dados(arquivo)
    if not dados:
        return False

    #isso pega a primeira e unica chave que vem do dicionario
    chave = str(list(dicio.keys())[0])


    for ids, valor in dicio.items():
        if chave == str(ids):
            # modifica e salva 
            dados[chave] = dicio[chave]
            salvar_dados(dados, arquivo)
            return True
    else:
        return False


def adicionar_dados(dicio, arquivo):
    """Adiciona um novo item ao arquivo JSON, verificando se a chave já existe."""
    dados = carregar_dados(arquivo)
    if not dados:
        chave = "1"
    
    #isso pega a primeira e unica chave que vem do dicionario
    chave = str(list(dicio.keys())[0])
    for keys,item in dados.items():
        if chave == keys:
            # se ja existir essa chave
            input("Chave ja existente, chame um desenvolvedor")
            return False
    else:
        # se nao existir adiciona e salva
        dados[chave] = dicio[chave]
        salvar_dados(dados, arquivo)
        return True

a = {"1": {"nome": 'dan', 'vida': 5, 'poder': 5, 'habilidade': 'mimimi'}}

def excluir_dados(dicio, arquivo):
    """Remove um item do arquivo JSON com base em sua chave."""
    dados = carregar_dados(arquivo)
    if not dados:
        return False
    
    #isso pega a primeira e unica chave que vem do dicionario
    chave = str(list(dicio.keys())[0])
    for ids, valor in dados.items():
        if chave == ids:
            # modifica e salva 
            del dados[chave]
            salvar_dados(dados, arquivo)
            return True
    else:
        return False
def salvar_dados(dados, arquivo):
    """Salva um dicionário de dados em um arquivo JSON."""
    caminho_json = os.path.join(base_dir, f"{arquivo}.json") 
    with open(caminho_json, "w") as f:
        json.dump(dados, f)
b = {"2": {"nome": 'gabs', 'vida': 5, 'poder': 5, 'habilidade': 'mimimi'}}
if __name__ == "__main__":
    print(adicionar_dados(b, 'mutantes'))