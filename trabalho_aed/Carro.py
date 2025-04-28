from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, cor, ano=2025, qtd=4, cat=None):
        super().__init__(modelo, cor, ano)
        self.portas = qtd
        self.categoria = cat

    def __str__(self):
        cat_nome = self.categoria.nome if self.categoria else "Sem Categoria"
        return super().__str__() + f"\nPortas: {self.portas}\nCategoria: {cat_nome}"

    def exibir_dados(self):
        cat_nome = self.categoria.nome if self.categoria else "Sem Categoria"
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Portas: {self.portas}, Categoria: {cat_nome}"

