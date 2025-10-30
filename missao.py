import random
from academia import escolher_mutante
class Missao():
    def __init__(self, descricao, dificuldade):
        self.descricao = descricao
        self.dificuldade = dificuldade
    def iniciar_missao(self):
        info = escolher_mutante()
        if info == False:
            input("Pressione enter para continuar...")
            return False

        input (info)
        x = random.randint(1, 5)
        x = x * self.dificuldade
        info['missoes_completadas']+=1
        info['vida'] = info['vida'] - x
        if info['vida'] < 0:
            pass
        pass
if __name__ == "__main__":
    m = Missao("Desc", 1)
    m.iniciar_missao()