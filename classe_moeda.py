import pygame
import random


class moeda:

    def __init__ (self, x_moeda, y_moeda, moeda_capturada):
        # armazena a tela
        # armazena a largura = telaX
        # armazena a altura = telaY
        self.telaX = telaX
        self.telaY = telaY
        self.tela = (self.telaX, self.telaY)
        self.x = x
        self.y = y
        #posiçao do x e y da moeda
        self.x_moeda = x_moeda
        self.y_moeda = y_moeda
        # importar a imagem da nave e seu tamanho
        self.imagem_nave = pygame.image.load("foto.nave1.png")
        self.tamanho_nave = self.imagem_nave.get_rect().size
        # importar a imagem da moeda e seu tamanho
        self.moeda_capturada = moeda_capturada

        self.imagem_moeda = pygame.image.load('foto.moeda.png')
        self.tamanho_moeda = self.imagem_moeda.get_rect().size


        self.tem_moeda = False
        self.moeda_capturada = 0

    def pos_vidas_moedas_aleatoria(self, x, y, obj_size, p_size):
        x_obj, y_obj = random.randint(0, self.x_moeda - obj_size[0]), random.randint(0, self.y_moeda - obj_size[1])
        while (x <= x_obj and x_obj <= x + p_size[0]) and (y <= y_obj and y_obj <= y + p_size[1]):
            # Fazendo que nao va nascer no lugar do usuario
            x_obj, y_obj = random.randint(0, self.x_moeda - obj_size[0]), random.randint(0, self.y_moeda - obj_size[1])

        return x_obj, y_obj

    def aparecer(self, tempo_jogo):
        if tempo_jogo % 180 == 0:  # isso indica a cada 3 segundos(60 por segundo)
            self.tem_moeda = True
            self.x_moeda, self.y_moeda = self.pos_vidas_moedas_aleatoria(self, self.x, self.y, self.telaX, self.telaY, self.tamanho_moeda, self.tamanho_nave)

    def esbarrar(self, tem_moeda, tela):
        if tem_moeda == True:
            tela.blit(self.imagem_moeda, (self.x_moeda, self.y_moeda))
            if (self.x <= self.x_moeda + self.tamanho_moeda[0] and self.x_moeda <= self.x + self.tamanho_nave[0]) and (
                    self.y <= self.y_moeda + self.tamanho_moeda[1] and self.y_moeda <= self.y + self.tamanho_nave[1]):
                    self.moeda_capturada += 1
                    print(f"moedas: {self.moeda_capturada}")
                    self.tem_moeda = False
