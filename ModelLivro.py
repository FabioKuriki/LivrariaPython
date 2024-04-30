class ModelLivro:
    def __init__(self):
        self.codigo = [0, 1]
        self.nome = ["Vingadores", "Liga da Justiça"]
        self.quantidade = [1, 2]
        self.descricao = ["Fim dos Vingadores", "Origem da Liga"]
        self.autor = ["Marvel", "DC"]

    def realizarCompra(self, opcao):
        if(self.quantidade[opcao - 1] > 0):
            self.quantidade[opcao - 1] = self.quantidade[opcao - 1] - 1
            return "Compra realizada com sucesso!!"
        else:
            return "Livro indisponível"




