"""
Você deve criar uma classe Carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3)_Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda


  N
O   L
  S

  Exemplo:
      >>> # Testando o motor
      >>> motor = Motor()
      >>> motor.velocidade
      0
      >>> motor.acelerar()
      >>> motor.velocidade
      1
      >>> motor.acelerar()
      >>> motor.velocidade
      2
      >>> motor.frear()
      0
     >>> # Testando a direção
     >>> direcao = Direcao()
     >>> direcao.valor
     'Norte'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Leste'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Sul'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Oeste'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    'Norte'

     >>> # Testando o carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
"""
from direcao import Direcao
from motor import Motor


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor
