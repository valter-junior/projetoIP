import pygame  # a biblioteca do pygame
import random  # para pegar valores aleatórios

# Os imports de pastas agora:
from projetoIP.Classes import *

def dados_game(moeda_capturada, pontuacao, TELA_APP):
    # Essa função serve para colocar os dados de coleta de moeda
    # Ou colisão com o inimigo, na tela

    message_coin = f'Moedas: {moeda_capturada}'
    formatted_text_coin = fonte.render(message_coin, True, (255, 255, 255))

    message_enemy = f'Abates: {pontuacao}'
    formatted_text_enemy = fonte.render(message_enemy, True, (255, 255, 255))

    TELA_APP.blit(formatted_text_coin, (840, 5))
    TELA_APP.blit(formatted_text_enemy, (420, 5))

#função de colisão com qualquer class
def colisao(x_a, y_a, tam_a, x_b, y_b, tam_b): # Checa se a e b colidem
    if (x_a <=  x_b + tam_b[0] and x_b <= x_a + tam_a[0]) and (y_a <=  y_b + tam_b[1] and y_b <= y_a + tam_a[1]):
        return True
    else:
        return False

FPS = 60

# vel_usuario = 6  
# vel_inimigo1 = 4  
# vel_inimigo2 = 2  
# vel_inimigo3 = 8  

# MAX_VIDAS = 10  
# INICIAL_VIDAS = 4  
# tem_vida = False 

tempo_jogo = 0  
ajuste = 0  # Por enquanto é uma variável auxiliar usada para fazer o efeito da tela piscar
qual_imagem = 1 # Essa variaável só vai assumir valores de 1 e -1

tela_aplicativo = 'jogo' # Ela é dividida em: ['tela_inicial', 'jogo', 'pausa', 'tela_final']

LARGURA, ALTURA = 1000, 600  # Largura e altura da tela do aplicativo

TELA_APP = pygame.display.set_mode((LARGURA, ALTURA)) 
# Imagens
USUARIO = pygame.image.load("Imagens/ship_2.png")
INIMIGO1 = pygame.image.load("Imagens/pixel_ship_yellow2.png")
# INIMIGO2 = pygame.image.load("Imagens/pixel_ship_yellow2.png") # Carrega a imagem do inimigo 1
# INIMIGO3 = pygame.image.load("Imagens/pixel_ship_yellow2.png") # Carrega a imagem do inimigo 1
MOEDA = pygame.image.load("Imagens/coin_2.png")
ATAQUE = pygame.image.load("Imagens/lazer2.png")
VIDA = pygame.image.load("Imagens/Health2.png")
BACKGROUND = pygame.image.load("Imagens/galaxy_background.png") # Imagem do backgrond
TELA_INICIAL_IM1 = pygame.image.load("Imagens/1.png")
TELA_INICIAL_IM2 = pygame.image.load("Imagens/2.png")  
TELA_FINAL_IM1 = pygame.image.load("Imagens/3.png")  
TELA_FINAL_IM2 = pygame.image.load("Imagens/4.png")  

imagem_na_tela = TELA_INICIAL_IM1  # A imagem inicial da tela de início, vai precisar mudar depois

TAM_USUARIO = USUARIO.get_rect().size
TAM_INIMIGO1 = INIMIGO1.get_rect().size
TAM_MOEDA = MOEDA.get_rect().size
TAM_ATAQUE = ATAQUE.get_rect().size
TAM_VIDA = VIDA.get_rect().size 

pygame.init()
pygame.display.set_caption('Joguin')

# pygame.mixer.init()
# musica_fundo = pygame.mixer.music.load('Sons\BoxCat Games - Mission.mp3')  # Buscando a música de fundo
# sound_effect_collect = pygame.mixer.Sound('Sons\smw_message_block.wav') # Coleta moeda
# sound_effect_lazer = pygame.mixer.Sound('Sons\Shofixti-Shot.wav') # atira com laser
# sound_effect_health = pygame.mixer.Sound('Sons\smw_kick.wav') #  pega vida
# pygame.mixer.music.play(-1) # Se passar menos -1 para a função, ela fica em Loop

pygame.font.init()  # Iniciando
fonte = pygame.font.SysFont('8-BIT WONDER.TTF', 35, True, True) # A fonte que aparece na tela ainda não é essa

app_fps = pygame.time.Clock()  

rodar_app = True  # Indica se o app tá rodando
while rodar_app:
    app_fps.tick(FPS)
    TELA_APP.fill((0, 0, 0))
    TELA_APP.blit(BACKGROUND, (0,0))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar_app = False


    if tela_aplicativo == 'jogo':
        if tempo_jogo == 0:
            player = Nave(USUARIO, TELA_APP, ATAQUE)
            vida = Vida(VIDA, TELA_APP)
        # Enquanto estiver no jogo, o tempo de jogo será contado (o tempo atual é (tempo_jogo - 1)/60 segundos)
        tempo_jogo += 1

        #surgir a vida
        vida.surgir(tempo_jogo, FPS, player)
        vida.sumir(tempo_jogo, FPS)
        
        if vida.aparecer == True and colisao(player.x, player.y, player.tamanho, vida.x, vida.y, vida.tamanho):
            player.vida += 1
            vida.aparecer = False        

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:  
        #         if event.key == ord('p'):
        #             tela_aplicativo = 'pausa'

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]: 
            rodar_app = False

        player.controle(keys)

        # if (keys[ord("q")] or keys[ord(" ")]) and aparecer_ataque == False:
        #     sound_effect_lazer.play()  # Toda vez que clicar para atacar, vai ter um efeito"
        #     x_ataque, y_ataque = x_usuario, y_usuario + (TAM_USUARIO[1] - TAM_ATAQUE[1])//2
        #     # em cima é só definindo a posição que o ataque aparece, que é no meio do usuario
        #     aparecer_ataque = True
        #     # Como aparecer ataque é true ele não pode atacar de novo

        

        # Mostra os dados de Coleta Moeda e Abates na tela
        dados_game(player.moedas, player.inimigos, TELA_APP)

        vida.desenhar()
        player.desenhar()
        
        # Aqui atualiza a tela inserindo todos os desenhos realizados pelo blit a cada rodar_app do while
        pygame.display.flip()

pygame.quit()