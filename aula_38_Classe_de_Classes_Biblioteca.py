class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.instituicoes = []

    def adicionar_instituicao(self, nome):
        instituicao = Instituicao(nome)
        self.instituicoes.append(instituicao)
        return instituicao

    def mostrar(self):
        print(f"Cidade: {self.nome}")
        for inst in self.instituicoes:
            inst.mostrar(indent=2)

class Instituicao:
    def __init__(self, nome):
        self.nome = nome
        self.bibliotecas = []

    def adicionar_biblioteca(self, nome):
        biblioteca = Biblioteca(nome)
        self.bibliotecas.append(biblioteca)
        return biblioteca

    def mostrar(self, indent=0):
        pad = " " * indent
        print(f"{pad}Instituição: {self.nome}")
        for b in self.bibliotecas:
            b.mostrar(indent + 2)

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        return livro

    def mostrar(self, indent=0):
        pad = " " * indent
        print(f"{pad}Biblioteca: {self.nome}")
        for l in self.livros:
            print(f"{pad}  - {l.titulo} de {l.autor}")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# USO
cidade = Cidade("Londrina")
inst = cidade.adicionar_instituicao("Universidade Estadual")
biblio = inst.adicionar_biblioteca("Biblioteca Central")
biblio.adicionar_livro("Dom Casmurro", "Machado de Assis")
biblio.adicionar_livro("1984", "George Orwell")

cidade.mostrar()