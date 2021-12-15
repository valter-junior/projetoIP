import pygame

# (self, imagem, TELA, NAVE)
#

# declara a classe nave que é contralada pelo jogador através das setas e atira pelo "espaço"
# armazena sua posição e seu tamanho além do número de moedas, de corações, inimigos mortos e o tamanho da tela
class Nave:
    # ao inicializar a variável é necessário passar a largura e altura da tela e a posição inicial do jogador
    def __init__(self, imagem, TELA, ataque): # tela é TELA_APP e imagem é pra ser o com o arquivo tbm
        self.imagem = imagem
        self.tamanho = imagem.get_rect().size # determina a posição da imagem na tela aí
        self.TELA = TELA #Apenas para ajudar no blit
        self.tela = TELA.get_rect().size
        
        self.velocidade = 6 # velocidade e posiçoes iniciais
        self.x = 0
        self.y = (self.tela[1] - self.tamanho[1])//2

        # conta a quantidade de vida, moedas coletadas e inimigos derrotados
        self.vida = 4
        self.moedas = 0
        self.inimigos = 0
        
        #armazena a imagem do tiro
        self.tiroIMG = ataque
        #determina o tamanho do tiro
        self.tiroTamanho = self.tiroIMG.get_rect().size
        #velocidade e x e y do tiro
        self.tiroVelocidade = self.tiroTamanho[0]
        self.tiroX = self.x + self.tamanho[0]//2
        self.tiroY = self.y + self.tamanho[1]//2
        self.tiro = False # determina se há um tiro na tela

    def atirar(self):
        if self.tiroX < self.tela[0]:
            self.tiroX += self.tiroVelocidade
        else:
            self.tiro = False

    #controla a movimentação e o tiro da nave
    def controle(self, teclas):
        # teclas = pygame.key.get_pressed()

        #move a nave para cima ao pressionar a seta pra cima
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        #previne que a nave saia da tela ao mudar o y para o valor minimo se ela tentar sair da tela
        elif teclas[pygame.K_UP]:
            self.y = 0

        #o mesmo princípio do movimeto pra cima mais aplicado para o lados restantes
        if teclas[pygame.K_DOWN] and self.y < self.tela[1] - self.tamanho[1]:
            self.y += self.velocidade
        elif teclas[pygame.K_DOWN]:
            self.y = self.tela[1] - self.tamanho[1]

        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade
        elif teclas[pygame.K_LEFT]:
            self.x = 0

        if teclas[pygame.K_RIGHT] and self.x < self.tela[0] - self.tamanho[0]:
            self.x += self.velocidade
        elif teclas[pygame.K_RIGHT]:
            self.x = self.tela[0] - self.tamanho[0]
        
        #define onde o tiro irá aparecer e muda a variavel self.tiro para True que é necessário pra a função atirar
        if teclas[pygame.K_SPACE] and not self.tiro:
            self.tiroX = self.x 
            self.tiroY = self.y + (self.tamanho[1] - self.tiroTamanho[1]) // 2
            self.tiro = True

        #chama a função atirar se self.tiro for verdade
        if self.tiro:
            self.atirar()
        
    #desenha tanto a nave quanto o tiro (se ele estiver na tela)
    def desenhar(self):
        if self.tiro:
            self.TELA.blit(self.tiroIMG, (self.tiroX, self.tiroY))

        self.TELA.blit(self.imagem, (self.x, self.y))


#import pygame
import random


#Declara a vida que pode ser capturada pela nave , controlada pelo jogador. Atualmente a vida surge aleatoriamente na tela e fica parada. Caso tenha colisão com o jogador, deve ser contabilizado. Caso passe um tempo e o jogador n pegue a vida, **deve sumir e aparecer em outro lugar. 

class Vida:
    def __init__(self, imagem, tela):
        #ao inicializar a variável é necessário passar a largura e altura da tela e a posição inicial do jogador

        #salva a tela
        self.tela = tela
        self.tela_tamanho = tela.get_rect().size
        
        #determina o tamnho da imagem
        self.imagem = imagem
        self.tamanho = imagem.get_rect().size
        
        #posições iniciais
        self.x = None
        self.y = None
        #self.posicao = Vida.criar_posicao(player)

        self.aparecer = False

    def criar_posicao(self, nave):
        player_x = nave.x
        player_y = nave.y
        player_size = nave.tamanho
        #define uma posição aleatória para surgir o coração
        x = random.randint(0,self.tela_tamanho[0] - self.tamanho[0])
        y = random.randint(0,self.tela_tamanho[1] - self.tamanho[1])
        #chamar novamente se tiver junto do jogador
        if (player_x <= x and x <= player_x + player_size[0]) and (player_y<= y and y <= player_y + player_size[1]) :
            return self.criar_posicao(nave)
        else:
            self.x = x
            self.y = y 

    def sumir(self, tempo_decorrido, FPS):
        #se passou o tempo desejado (5s), mudar de posição
        if (tempo_decorrido % (15*FPS)) == 0:
        #fazer a muda sumir ou mudar de posição
        ##mudar de posição:
            self.aparecer = False          

    def surgir(self, tempo_decorrido, FPS, nave):
        if (tempo_decorrido % (10*FPS)) == 0 and (random.randint(1,100) <= 30):
            self.aparecer = True
            self.criar_posicao(nave)
 
    def desenhar(self):
        if self.aparecer:
            self.tela.blit(self.imagem, (self.x, self.y))