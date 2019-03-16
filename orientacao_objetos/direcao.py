"""
A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda
"""


class Direcao:
    def __init__(self):
        self.valor = "Norte"

    def girar_a_direita(self):
        """Deve alterar o valor virando a direita.
        Deverá alterar o valor da direção para a próxima direção olhando a sua direita,
        por exemplo:
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Sul'
        """
        direcoes = {"Norte": "Leste", "Leste": "Sul", "Sul": "Oeste", "Oeste": "Norte"}
        self.valor = direcoes.get(self.valor)

    def girar_a_esquerda(self):
        """Deve alterar o valor virando a esquerda.
        Deverá alterar o valor da direção para a próxima direção a sua esquerda,
        por exemplo:
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Sul'
        """
        direcoes = {"Norte": "Oeste", "Oeste": "Sul", "Sul": "Leste", "Leste": "Norte"}
        self.valor = direcoes.get(self.valor)
