from ModelUsuario import ModelUsuario
from ControlLivro import ControlLivro

class ControlUsuario:
    # Método Construtor
    def __init__(self):
        self.model = ModelUsuario()
        self.cLivro = ControlLivro()
        self.opcao = -1
        self.opcao2 = -1
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

    def menuAcesso(self):
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
        if(self.model.usuarioExistente(self.login, self.senha) != True):
            print("Login e senha não válidos")
        else:
            self.opcao2 = -1
            self.cLivro.loginAtual = self.login
            self.menuUsuarioCompleto()


    def menuCadastro(self):
        self.nome = input("Bem-vindo a nossa Livraria, " +
                          "por gentileza informe os seguintes dados para cadastro: " +
                          "\nNome: ")

        self.endereco = input("Endereço: ")
        self.validarNum(self.telefone, "Telefone: ")
        print("Data de Nascimento")
        self.validarData(self.telefone, 1, 31, "Dia: ")
        self.validarData(self.telefone, 1, 12, "Mês: ")
        self.validarAno(self.telefone, 0,  "Ano: ")
        self.login = input("Login: ")
        while(self.model.verificarLogin(self.login) != False):
            self.login = input("Login já existente em sistema, por favor informe outro: ")
        self.senha = input("Senha: ")

        print(self.model.realizarCadastro(self.nome, self.endereco, self.telefone, self.dia, self.mes, self.ano, self.login, self.senha))


    def validarData(self, variavel, num1, num2, mensagem):
        try:
            variavel = int(input(f"{mensagem}"))
            while(variavel < num1 or variavel > num2):
                if(variavel < num1 or variavel > num2):
                    print(f"Informe um valor entre {num1} e {num2}")
                    variavel = int(input(f"{mensagem}"))
        except ValueError:
            print("Informe um valor númerico")
            self.validarNum(variavel, mensagem)

    def validarAno(self, variavel, num1, mensagem):
        try:
            variavel = int(input(f"{mensagem}"))
            while(variavel < num1):
                if(variavel < num1 ):
                    print(f"Informe um valor maior ou igual a {num1}")
                    variavel = int(input(f"{mensagem}"))
        except ValueError:
            print("Informe um valor númerico")
            self.validarNum(variavel, mensagem)

    def validarNum(self, variavel, mensagem):
        try:
            variavel = int(input(f"{mensagem}"))
        except ValueError:
            print("Informe um valor númerico")
            self.validarNum(variavel, mensagem)

    def menuUsuario(self):
        self.opcao2 = int(input("\n\n0. Sair" +
                               "\n1. Ver livros" +
                               "\n2. Consultar compras" +
                               "\n3. Consultar reservas" +
                               "\nO que você gostaria de fazer? "))

    def menuUsuarioCompleto(self):
        while(self.opcao2 != 0):
            self.menuUsuario()
            if(self.opcao2 == 0):
                print("Saindo...")
            elif(self.opcao2 == 1):
                self.cLivro.menuLivroCompleto()
            elif(self.opcao2 == 2):
                print(self.cLivro.cCompra.model.verCompra(self.login)) #Não está funcionando no momento(ARRUMAR)
            elif(self.opcao2 == 3):
                print(self.cLivro.cReserva.model.verReserva(self.login))
            else:
                print("Selecione uma opção válida!!!")