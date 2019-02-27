class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        """Inicializa os atributos da instância."""
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def __repr__(self):
        """Representa a instancia utilizando seu nome."""
        return self.nome

    def cumprimentar(self):
        """Retorna o cumprimento da instância de pessoa com seu ID."""
        return f'Olá me chamo {self.nome} e tenho {self.idade} anos.'


if __name__ == '__main__':
    filho = Pessoa(nome='Rose')
    segundo_filho = Pessoa(nome='Shaw')
    # Os filhos podem ser enviados do jeito abaixo ou então através
    # de uma tupla.
    pai = Pessoa(filho, segundo_filho, nome='Evans', idade=50)
    print(pai.__dict__)
    print(pai.filhos)
