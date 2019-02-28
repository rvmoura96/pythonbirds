class Pessoa:
    olhos = 2  # este é um atributo de classe.

    def __init__(self, *filhos, nome=None, idade=None):
        """Inicializa os atributos da instância da classe."""
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
    rose = Pessoa(nome='Rose')
    shaw = Pessoa(nome='Shaw')
    andrews = Pessoa(nome='Andrews')
    evans = Pessoa(rose, shaw, andrews, nome='Evans', idade=50)
    print(evans.__dict__)
    print(evans.filhos)
    
