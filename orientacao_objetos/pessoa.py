class Pessoa:
    def cumprimentar(self):
        """
        Retorna o cumprimento da instância de pessoa com seu ID.
        """
        return f'Olá {id(self)}'
