from direcao import Direcao
from motor import Motor


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor):
        """Atributos de dados da classe Carro."""
        self.motor = motor
        self.direcao = direcao

    def acelerar(self) -> None:
        """Chama o método acelerar da classe motor.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        1
        """
        self.motor.acelerar()

    def frear(self) -> None:
        """Chama o método frear da classe motor.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.acelerar()
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        2
        >>> carro.frear()
        >>> carro.calcular_velocidade()
        0
        """
        self.motor.frear()

    def girar_a_direita(self) -> None:
        """Chama o método girar_a_direita da classe direcao.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.girar_a_direita()
        >>> carro.calcular_direcao()
        'Leste'
        """
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self) -> None:
        """Chama o método girar_a_esquerda da classe direcao.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Oeste'
        """
        self.direcao.girar_a_esquerda()

    def calcular_velocidade(self) -> int:
        """Calcula a velocidade armazenada na classe motor.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade()
        0
        """
        return self.motor.velocidade

    def calcular_direcao(self) -> str:
        """Calcula o valor da direção armazenada na classe direcao.

        >>> motor = Motor()
        >>> direcao = Direcao()
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_direcao()
        'Norte'
        """
        return self.direcao.valor
