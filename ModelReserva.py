class ModelReserva:
    def __init__(self):
        self.i = 0
        self.codigoReserva = []
        self.codigoLivro = []
        self.login = []
        self.reservaTotal = ""

    def realizarReserva(self, codigoDoLivroSelecionado, loginAtual):
        self.codigoReserva.append(self.i)
        self.codigoLivro.append(codigoDoLivroSelecionado)
        self.login.append(loginAtual)
        self.i += 1

    def verReserva(self, loginAtual):
        for i in range(len(self.codigoReserva)):
            if(loginAtual == self.login[i]):
                self.reservaTotal += f"\nCódigo da reserva: {self.codigoReserva[i]}\nCódigo do Livro: {self.codigoLivro[i]}\nLogin: {self.login[i]}\n\n"

        return self.reservaTotal



