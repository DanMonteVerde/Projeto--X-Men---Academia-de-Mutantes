from utils import carregar_dados, salvar_dados

def criar_conta():
    contas = carregar_dados('contas')
    if not contas:
        contas = {}
    email = input("Email: ")
    senha = input("Senha: ")
    for i in contas:
        if contas[i]['email'] == email:
            print("Email ja cadastrado!")
            input("Pressione enter para continuar...")
            break
        if contas[i]['senha'] == senha:
            print("Senha ja cadastrada!")
            input("Pressione enter para continuar...")
            break
    else:
        contas[email] = {'email': email, 'senha': senha}
        salvar_dados(contas, 'contas')
def autenticar():
    contas = carregar_dados('contas')
    if not contas:
        print("Nenhuma conta cadastrada!")
        input("Pressione enter para continuar...")
        return False
    email = input("Email: ")
    senha = input("Senha: ")
    for i in contas:
        if contas[i]['email'] == email and contas[i]['senha'] == senha:
            return contas[i]
    else:
        print("Email ou senha incorretos!")
        input("Pressione enter para continuar...")
        return False