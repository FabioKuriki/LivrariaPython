class ModelUsuario:
    # Método Construtor
    def __init__(self):
        self.loginExistente = False
        self.nome = []
        self.endereco = []
        self.telefone = []
        self.dtNascimento = []
        self.login = []
        self.senha = []

    def realizarCadastro(self, nome, endereco, telefone, dia, mes, ano, login, senha):
        self.nome.append(nome)
        self.endereco.append(endereco)
        self.telefone.append(telefone)
        self.dtNascimento.append(f"{dia}/{mes}/{ano}")
        self.login.append(login)
        self.senha.append(senha)

        return "Cadastro realizado com sucesso!!"

    # Verificar se os dados foram cadastrados e guardados nas listas
    def consultarCadastros(self):
        return f"{self.nome}\n{self.endereco}\n{self.telefone}\n{self.dtNascimento}\n{self.login}\n{self.senha}"


    def verificarLogin(self, login):
        for i in range(0, len(self.login), 1):
            if(login == self.login[i]):
                return True

        return False

    def usuarioExistente(self, login, senha):
        for i in range(0, len(self.login), 1):
            if(login == self.login[i] and senha == self.senha[i]):
                return True

        return False



