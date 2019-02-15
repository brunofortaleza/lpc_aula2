class Projeto:
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __str__(self):
        return "Pessoa: " + self.nome


class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return "Pessoa: " + self.nome + " Data/Nasc: " + self.data_nascimento


class Atividade:

    def __init__(self, nome, prioridade, pessoa, projeto, data_inicio, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = pessoa
        self.projeto = projeto
        self.data_inicio = data_inicio
        self.data_fim = data_fim


p=Pessoa('Bruno', '25/01/1993')
pj = Projeto ('Larisse', "08/02/2019", "15/02/2019")
a = Atividade('teste', 1, p, pj, "10/02/2019", "20/02/2019")

print()
