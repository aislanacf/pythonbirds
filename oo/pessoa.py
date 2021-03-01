class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    p = Pessoa('Fulano',43)
    #print(Pessoa.cumprimentar(p))
    #print(id(p))
    print(p.cumprimentar())