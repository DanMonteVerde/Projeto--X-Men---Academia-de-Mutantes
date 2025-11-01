from utils import carregar_dados, adicionar_dados, atualizar_dados

class Mutante:
    def __init__(self, nome, vida, poder, habilidades):
        self.nome = nome
        self.vida = vida
        self.poder = poder
        self.habilidades = habilidades
        self.missoes_completadas = 0


    def usar_pooder(self):
        """ Exibe uma mensagem indicando o uso do poder principal do mutante."""
        return f"{self.nome} usa seu poder: {self.poder}!"
    
    def treinar(self):
        """ Aumenta a vida do mutante em 10 pontos, simulando um treino."""
        self.vida += 10
        return f"{self.nome} treinou! Vida atual: {self.vida}"
    
    @staticmethod
    def validar_nome(nome):
        """Verifica se o nome fornecido é válido (não vazio após remover espaços"""
        return bool(nome.strip())
    
    def __str__(self):
        """Retorna uma representação formatada do mutante exibindo seus atributos."""
        habilidades = ", ".join(self.habilidades)
        return (f"Mutante: {self.nome} | Vida: {self.vida} | Poder: {self.poder} | " f"Habilidades: {habilidades} | Missões: {self.missoes_completadas}")

class MutanteFisico(Mutante):
    def usar_poder(self):
        """ Exibe a mensagem de uso do poder físico do mutante."""
        return f"{self.nome} usa seu ataque físico: {self.poder}! Impacto devastador!" 

class MutantePsiquico(Mutante):
    def usar_poder(self):
        """ Exibe a mensagem de uso do poder psíquico do mutante."""
        return f"{self.nome} usa seu ataque psíquico: {self.poder}! Controle mental ativado!"


ARQUIVO = "mutantes"

def criar_mutante():
    """
    Cria um novo mutante recebendo dados do usuário,
    valida o nome, define o tipo e salva no arquivo JSON.
    """
    print("\n=== Criar Mutante ===")
    tipo = input("Digite o tipo [F - Físico | P - Psíquico]: ").upper()
    while tipo != 'F' and tipo != "P":
        tipo = input("Informe um TIPO  [F - Físico | P - Psíquico]: ").upper()
    nome = input("Nome do mutante: ")
    while True:
        try:
            vida = int(input("Vida inicial: "))
            break
        except ValueError:
            print("Digite um valor numérico para a vida!")

    poder = input("Poder principal: ")
    habilidades = input("Habilidades (separadas por vírgula): \n ").split(",")


    if not Mutante.validar_nome(nome):
        print("Nome inválido!")
        return
    
    if tipo == "F":
        mutante = MutanteFisico(nome, vida, poder, habilidades)
    elif tipo == "P":
        mutante = MutantePsiquico(nome, vida, poder, habilidades)
    else:
        print("Tipo inválido!")
        return
    
    dados_para_json = {
        str(len(carregar_dados(ARQUIVO))+1): {
            "nome": mutante.nome,
            "vida": mutante.vida,
            "poder": mutante.poder,
            "habilidades": mutante.habilidades,
            "missoes_completadas":mutante.missoes_completadas
        }
    }

    if adicionar_dados(dados_para_json, ARQUIVO):
        print(f"O Mutante {mutante.nome} cadastrado com sucesso!")
        input("Pressione enter para continuar...")
    else:
        print("Erro ao cadastrar mutante!")
        input("Pressione enter para continuar...")

def treinar_mutante():
    """
    Seleciona um mutante cadastrado, executa seu treino
    e atualiza seus dados no arquivo.
    """
    print("\n=== Treinar Mutante ===")
    
    chave, info = escolher_mutante()
    if info == False:
            input("Pressione enter para continuar...")
            return False
    if "Garras" in info["poder"] or "Força" in info["poder"]:
        mutante = MutanteFisico(info["nome"], info["vida"], info["poder"], info["habilidades"])
    else:
        mutante = MutantePsiquico(info["nome"], info["vida"], info["poder"], info["habilidades"])
    
    resultado = mutante.treinar()
    dados[escolha]["vida"] = mutante.vida
    atualizar_dados({escolha: dados[escolha]}, ARQUIVO)
    input(f"{resultado}\nPressione enter para continuar...")


def escolher_mutante():
    """ Exibe a lista de mutantes e permite ao usuário escolher um pelo número."""
    dados = carregar_dados(ARQUIVO)

    if not dados:
        print("Nenhum mutante cadastrado!")
        return False, False
    
    for chave, info in dados.items():
        print(f"{chave} - {info['nome']} | Vida: {info['vida']} | Poder: {info['poder']}")

    escolha = input("Escolha o mutante pelo número: ")
    if escolha not in dados:
        print("Mutante inválido!")
        return False, False
    return str(escolha), dados[escolha]

def listar_mutante():
    """ Exibe na tela todas as informações de um mutante escolhido."""
    escolha, info = escolher_mutante()
    if info == False:
        input("Pressione enter para continuar...")
        return False
    print(f"Nome: {info['nome']}\nVida: {info['vida']}\nPoder: {info['poder']}\nHabilidades: {info['habilidades']}")
    input("Pressione enter para continuar...")

def editar_cadastro():
    escolha, info = escolher_mutante()
    if info == False:
        input("Pressione enter para continuar...")
        return False
    
    print(f"Nome: {info['nome']}\nVida: {info['vida']}\nPoder: {info['poder']}\nHabilidades: {info['habilidades']}")
    while True:
        mudar = input("O que deseja mudar? (N - Nome, V - Vida, P - Poder, H - Habilidades): ").upper()
        match mudar:
            case "N":
                info["nome"] = input("Novo nome: ")
                break
            case "V":
                info["vida"] = input("Nova vida: ")
                break
            case "P":
                info["poder"] = input("Novo poder: ")
                break
            case "H":
                info["habilidades"] = input("Novas habilidades (separadas com ,): ").split(",")
                break
            case _:
                print("Opção inválida!")
                input("Pressione enter para continuar...")
                continue
        
    atualizar_dados({escolha: info}, "mutantes")
    return True         
if __name__ == "__main__": 
    editar_cadastro()