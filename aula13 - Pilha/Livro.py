from Autor import Autor

class Livro:
    def __init__(self, titulo: str, autor: Autor, paginas: int):
        self.titulo = titulo
        self.autor = autor  # Agora é um objeto Autor
        self.paginas = paginas
        self.prox = None

    def __str__(self):
        # Acessamos o nome do autor através do objeto
        return f"Título: {self.titulo}, Autor: {self.autor.nome}, Páginas: {self.paginas}"
