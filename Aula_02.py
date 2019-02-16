
class Pessoa:
    def __init__(self, nome):
        self.nome = nome;

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf):
        super.__init__(nome)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super.__init__(nome)
        self.cnpj = cnpj

class Autor(Pessoa):
    def __init__(self, nome):
        super.__init__(nome)

class Evento:
    def __init__(self, pessoa):
        self.pessoa = pessoa

class Artigo:
    pass


class AutorArtigos:
    def __init__(self, autor, artigos):
        self.autor = autor
        self.artigos = artigos