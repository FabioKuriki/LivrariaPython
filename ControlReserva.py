from ModelReserva import ModelReserva

class ControlReserva:
    def __init__(self):
        self.model = ModelReserva()
        self.opcao = -1
        self.loginAtual = ""
        self.codigoLivro = -1
    def menuCerteza(self):
        self.opcao = int(input("\n0. Não" +
                               "\n1. Sim" +
                               "\nO livro que você procura, se encontra indisponivel. Gostaria de realizar uma reserva? "))

    def menuCertezaCompleto(self):
        self.opcao = -1

        while(self.opcao < 0 or self.opcao > 1):
            self.menuCerteza()
            if(self.opcao == 0):
                break
            elif(self.opcao == 1):
                self.model.realizarReserva(self.codigoLivro, self.loginAtual)
                print("Reserva realizada")
            else:
                print("Selecione uma opção válida!")
