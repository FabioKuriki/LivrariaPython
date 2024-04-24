from ModelUsuario import ModelUsuario

class ControlUsuario:
    # Método Construtor
    def __init__(self):
        self.model = ModelUsuario()
        self.opcao = -1
        self.nome = ""
        self.endereco = ""
        self.telefone = 0
        self.dia = 0
        self.mes = 0
        self.ano = 0
        self.login = ""
        self.senha = ""

    def menu(self):
        self.opcao = int(input("\n\n-------- Livraria --------" +
                               "\n0. Sair" +
                               "\n1. Login" +
                               "\n2. Cadastro" +
                               "\nEscolha uma das opções acima: "))

    def menuUsuario(self):
        while(self.opcao != 0):
            self.menu()
            if(self.opcao == 0):
                print("Tenha um ótimo dia!!")
            elif(self.opcao == 1):
                self.menuLogin()
            elif(self.opcao == 2):
                self.menuCadastro()
            elif(self.opcao == 3):
                print(self.model.consultarCadastros())
            else:
                print("A opção selecionada não é válida!")

    def menuLogin(self):
        self.login = input("Informe os seguintes dados: " +
                           "\nLogin: ")

        self.senha = input("Senha: ")
        if(self.model.usuarioExistente(self.login, self.senha) == True):
            print("Login realizado com sucesso")
        else:
            print("Login e senha não válidos")


    def menuCadastro(self):
        self.nome = input("Bem-vindo a nossa Livraria, " +
                          "por gentileza informe os seguintes dados para cadastro: " +
                          "\nNome: ")

        self.endereco = input("Endereço: ")
        self.telefone = int(input("Telefone: "))
        if(self.dia < 1 or self.dia > 31):
            self.dia = int(input("Data de Nascimento" +
                         "\nDia: "))
        if(self.mes < 1 or self.mes > 12):
            self.mes = int(input("Mês: "))
        if(self.ano < 1):
            self.ano = int(input("Ano: "))
        self.login = input("Login: ")
        while(self.model.verificarLogin(self.login) != False):
            self.login = input("Login já existente em sistema, por favor informe outro: ")
        self.senha = input("Senha: ")

        print(self.model.realizarCadastro(self.nome, self.endereco, self.telefone, self.dia, self.mes, self.ano, self.login, self.senha))