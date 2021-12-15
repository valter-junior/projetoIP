import pygame
import random


class Enemy:

    def __init__(self, image, TELA, NAVE):
        self.image = image
        self.tamanho = self.image.get_rect().size
        self.TELA = TELA
        self.tela = TELA.get_react().size
        self.rect = self.image.get_rect(
            center=(
                random.randint(self.tela[0] + 20, self.tela[0] + 100),
                random.randint(0, self.tela[1])
            )
        )
        self.speed = random.randint(3, 10)
