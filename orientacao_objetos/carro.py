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
