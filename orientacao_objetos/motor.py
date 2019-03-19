"""
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3)_Método frear que deverá decrementar a velocidade em duas unidades.
"""


class Motor:
    def __init__(self):
        """Atributos de dados da classe Motor."""
        self.velocidade = 0

    def acelerar(self):
        """Deverá incrementar a velocidade em uma unidade.
        >>> motor = Motor()
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        """
        self.velocidade += 1

    def frear(self):
        """Deverá decrementar a velocidade em duas unidades.
        >>> motor = Motor()
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> motor.acelerar()
        >>> motor.velocidade
        2
        >>> motor.frear()
        >>> motor.velocidade
        0
        """
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
