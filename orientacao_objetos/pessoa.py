class Pessoa:
    def __init__(self, nome=None, idade=None):
        """Inicializa os atributos da instância."""
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        """Retorna o cumprimento da instância de pessoa com seu ID."""
        return f'Olá me chamo {self.nome} e tenho {self.idade} anos.'
