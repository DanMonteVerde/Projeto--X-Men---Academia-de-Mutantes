import random
class Missao():
    def __init__(self, descricao, dificuldade, xp):
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.xp = xp
        self.status = status
    def iniciar_missao(self, mutante):
        x = random.randint(1, 10)
        # mutante.vida = mutante.vida - x
        # mutante.energia = mutante.energia - x
        mutante.forca += self.xp
        pass