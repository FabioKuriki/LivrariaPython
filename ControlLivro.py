from ModelLivro import ModelLivro
from ControlReserva import ControlReserva
from ControlCompra import ControlCompra

class ControlLivro:
    # Método Construtor
    def __init__(self):
        self.model = ModelLivro()
        self.cCompra = ControlCompra()
        self.cReserva = ControlReserva()
        self.loginAtual = ""
        self.opcao = -1

    def menuLivro(self):
        self.opcao = int(input("\n0. Voltar" +
                              "\n1. Vingadores" +
                              "\n2. Liga da Justiça" +
                              "\nEscolha os livros de seu interesse ou selecione 0 para sair: "))

    def menuLivroCompleto(self):
        while (self.opcao != 0):
            self.menuLivro()
            if (self.opcao == 0):
                print("Voltando...")
                self.opcao = -1
                break
            elif (self.opcao == 1):
                self.compraOuReserva(self.opcao)
            elif (self.opcao == 2):
                self.compraOuReserva(self.opcao)
            else:
                print("A opção escolhida não é válida")

    def compraOuReserva(self, opcao):
        self.cCompra.loginAtual = self.cReserva.loginAtual = self.loginAtual
        self.cCompra.codigoLivro = self.cReserva.codigoLivro = self.opcao - 1

        if(self.model.realizarCompra(opcao) == True):
            self.cCompra.menuCertezaCompleto()
        else:
            self.cReserva.menuCertezaCompleto()