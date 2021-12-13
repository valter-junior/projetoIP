import pygame
import random
import assets 

#Declara a vida que pode ser capturada pela nave , controlada pelo jogador. Atualmente a vida surge aleatoriamente na tela e fica parada. Caso tenha colisão com o jogador, deve ser contabilizado. Caso passe um tempo e o jogador n pegue a vida, **deve sumir e aparecer em outro lugar. 

class Vida:
#class Vida(self, tela, player, tam_player, tam_vida ):
  #cor vermelha em RGB ou imagem do coração
  #cor = (255,0,0) 
  #self.tamanho = tam_vida
  #tamanho = ()

  def __init__(self, tela, x,y):
    #ao inicializar a variável é necessário passar a largura e altura da tela e a posição inicial do jogador

    #salva a tela
    self.tela = tela
    #importar a imagem
    self.imagem = pygame.image.load("assets/heart.jpg")
    #determina o tamnho da imagem
    self.tamanho = self.imagem.get_rect().size
    
    #posições iniciais
    self.x = x
    self.y = y  
    #self.posicao = Vida.criar_posicao(player)

  @staticmethod
  def criar_posicao(self, player_x, player_y, player_size):
    #define uma posição aleatória para surgir o coração
    x = random.randint(0,self.tamanho.right)
    y = random.randint(0,self.tamanho.bottom)
    #chamar novamente se tiver junto do jogador
    if (player_x <= x and x <= player_x + player_size[0]) and (player_y<= y and y <= player_y + player_size[1]) :
      return criar_posicao(player_x, player_y, player_size)
    else:
      return x , y

  def sumir(self, tempo_decorrido):
    #se passou o tempo desejado (10s), mudar de posição
    if (tempo_decorrido % (10*60)) == 0:
      #fazer a muda sumir ou mudar de posição
      ##mudar de posição:
      self.posicao = Vida.criar_posicao

  def esbarrar(self, player_x, player_y, x, y,esbarra_coração, player_size):
  #receber a posição da vida e testar se é a mesma da posição do jogador e contabiliza
    #contar
    if(player_x <= x and x <= player_x + player_size[0]) and (player_y<= y and y <= player_y + player_size[1]):
      # esbarra_coração é uma var global
      esbarra_coração += 1
      return esbarra_coração
  
  def blit(self, tela):
    tela.blit(self.imgem,(self.x, self.y))