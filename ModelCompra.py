class ModelCompra:
    def __init__(self):
        self.i = 0
        self.codigoCompra = []
        self.codigoLivro = []
        self.login = []
        self.compraTotal = ""

    def realizarCompra(self, codigoDoLivroSelecionado, loginAtual):
        self.codigoCompra.append(self.i)
        self.codigoLivro.append(codigoDoLivroSelecionado)
        self.login.append(loginAtual)
        self.i += 1

    def verCompra(self, loginAtual):
        for i in range(len(self.codigoCompra)):
            if(loginAtual == self.login[i]):
                self.compraTotal += f"\nCódigo da compra: {self.codigoCompra[i]}\nCódigo do Livro: {self.codigoLivro[i]}\nLogin: {self.login[i]}\n\n"

        return self.compraTotal