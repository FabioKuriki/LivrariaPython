from ModelLivro import ModelLivro

class ControlLivro:
    # Método Construtor
    def __init__(self):
        self.model = ModelLivro()
        self.opcao = -1

    def menuLivro(self):
        self.opcao = int(input("\n0. Sair" +
                              "\n1. Vingadores" +
                              "\n2. Liga da Justiça" +
                              "\nEscolha os livros de seu interesse ou selecione 0 para sair: "))

    def menuLivroCompleto(self):
        while (self.opcao != 0):
            self.menuLivro()
            if (self.opcao == 0):
                print("Saindo...")
                self.opcao = -1
                break
            elif (self.opcao == 1):
                print(self.model.realizarCompra(self.opcao))
            elif (self.opcao == 2):
                print(self.model.realizarCompra(self.opcao))
            else:
                print("A opção escolhida não é válida")