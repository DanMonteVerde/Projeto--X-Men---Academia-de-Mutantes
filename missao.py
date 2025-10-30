import random
from academia import escolher_mutante
from utils import excluir_dados, carregar_dados, atualizar_dados
class Missao():
    def __init__(self, descricao, dificuldade):
        self.descricao = descricao
        self.dificuldade = dificuldade
    def todict(self):
        return {str(len(carregar_dados('missao'))+1):
            {
            "descricao": self.descricao,
            "dificuldade": self.dificuldade
        }}
    
    def morreu(self, info):
        if excluir_dados(info['nome'], 'mutantes') == True:
            print(f"{info['nome']} Morreu")
            input("Pressione enter para continuar...")
        else :
            print("Erro ao excluir dados!")

def escolher_missao():
    dados = carregar_dados('missao')

    if not dados:
        print("Nenhuma missão cadastrada!")
        input("Pressione enter para continuar...")
        return False
    
    for chave, info in dados.items():
        print(f"{chave} - {info['descricao']} | Dificuldade: {info['dificuldade']}")

    escolha = input("Escolha a misssão pelo número: ")
    while escolha not in dados:
        print("Missao inválida!")
        escolha = input("Escolha a missão pelo número: ")
    return dados[escolha]
def iniciar_missao():
    chave, info = escolher_mutante()
    if info == False:
        input("Pressione enter para continuar...")
        return False
    if escolher_missao() == False:
        return False
    
    x = random.randint(1, 5)
    x = x * missao['dificuldade']
    info['missoes_completadas']+=1
    info['vida'] = info['vida'] - x
    if info['vida'] < 0:
        morreu(info)
    else:
        atualizar_dados({str(chave):info}, 'mutantes')
        print(f"{info['nome']} completou a missão {missao['descricao']} com sucesso! Perdendo {x} de vida!")
        input("Pressione enter para continuar...")
    
if __name__ == "__main__":
    m = Missao("Desc", 1)
    print(escolher_missao())