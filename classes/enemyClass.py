import pygame


class Enemy:
    image = pygame.image.load("/home/valter/projetoIP/images/enemy.jpeg")

    def __init__(self, name, velo, x, y):
        self.name = name
        self.velo = velo
        self.x = x
        self.y = y
