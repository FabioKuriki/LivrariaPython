from ModelCompra import ModelCompra

class ControlCompra:
    def __init__(self):
        self.model = ModelCompra()
        self.opcao = -1
        self.codigoLivro = -1
        self.loginAtual = ""

    def menuCerteza(self):
        self.opcao = int(input("\n0. Não" +
                               "\n1. Sim" +
                               "\nTem certeza que gostaria de realizar o pagamento? "))

    def menuCertezaCompleto(self):
        self.opcao = -1

        while(self.opcao < 0 or self.opcao > 1):
            self.menuCerteza()
            if(self.opcao == 0):
                break
            elif(self.opcao == 1):
                self.model.realizarCompra(self.codigoLivro, self.loginAtual)
                print("Compra realizada")
            else:
                print("Selecione uma opção válida!")