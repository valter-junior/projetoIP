import pygame  # a biblioteca do pygame
# import random  # para pegar valores aleatórios

# Os imports de pastas agora:
from classes.enemyClass import *
from classes.moeda import *
from classes.vida import *
from classes.nave import *
from classes.inimigo2 import *
# from game import *

def dados_game(moeda_capturada, pontuacao, quantidade_vidas, tempo, VIDA, TELA_APP):
    # Essa função serve para colocar os dados de coleta de moeda
    # Ou colisão com o inimigo, na tela

    message_coin = f'Moedas: {moeda_capturada}/999'
    formatted_text_coin = fonte.render(message_coin, True, (255, 255, 255))

    message_enemy = f'Abates: {pontuacao}'
    formatted_text_enemy = fonte.render(message_enemy, True, (255, 255, 255))

    message_time = f'Tempo: {tempo}s'
    formatted_text_time = fonte.render(message_time, True, (255, 255, 255))

    TAM_VIDA = VIDA.get_rect().size
    for i in range(quantidade_vidas):
        TELA_APP.blit(VIDA, (i*TAM_VIDA[0], 0))

    TELA_APP.blit(formatted_text_coin, (760, 5))
    TELA_APP.blit(formatted_text_enemy, (370, 5))
    TELA_APP.blit(formatted_text_time, (560, 5))

#função de colisão com qualquer class
def colisao(x_a, y_a, tam_a, x_b, y_b, tam_b): # Checa se a e b colidem
    if (x_a <=  x_b + tam_b[0] and x_b <= x_a + tam_a[0]) and (y_a <=  y_b + tam_b[1] and y_b <= y_a + tam_a[1]):
        return True
    else:
        return False

LARGURA, ALTURA = 1000, 600  # Largura e altura da tela do aplicativo

TELA_APP = pygame.display.set_mode((LARGURA, ALTURA)) 
# Imagens
USUARIO = pygame.image.load("Imagens/ship_2.png")
INIMIGO1 = pygame.image.load("Imagens/pixel_ship_yellow2.png")
INIMIGO2 = pygame.image.load("Imagens/pixel_ship_yellow2.png") # Carrega a imagem do inimigo 1
MOEDA = pygame.image.load("Imagens/coin_2.png")
ATAQUE = pygame.image.load("Imagens/lazer2.png")
VIDA = pygame.image.load("Imagens/Health2.png")
BACKGROUND = pygame.image.load("Imagens/galaxy_background.png") # Imagem do backgrond
TELA_INICIAL_IM1 = pygame.image.load("Imagens/1.png")
TELA_INICIAL_IM2 = pygame.image.load("Imagens/2.png")  
TELA_FINAL_IM1 = pygame.image.load("Imagens/3.png")  
TELA_FINAL_IM2 = pygame.image.load("Imagens/4.png")  

pygame.init()
pygame.display.set_caption('The Galaxy War')

# pygame.mixer.init()
# musica_fundo = pygame.mixer.music.load('Sons\BoxCat Games - Mission.mp3')  # Buscando a música de fundo
# sound_effect_collect = pygame.mixer.Sound('Sons\smw_message_block.wav') # Coleta moeda
# sound_effect_lazer = pygame.mixer.Sound('Sons\Shofixti-Shot.wav') # atira com laser
# sound_effect_health = pygame.mixer.Sound('Sons\smw_kick.wav') #  pega vida
# pygame.mixer.music.play(-1) # Se passar menos -1 para a função, ela fica em Loop

pygame.font.init()  # Iniciando
fonte = pygame.font.SysFont('8-BIT WONDER.TTF', 35, True, True) # A fonte que aparece na tela ainda não é essa


FPS = 60
tempo_jogo = 0 
tempo_tela = 0  # O tempo que o app tá aberto
tela_aplicativo = 'tela_inicial' # Ela é dividida em: ['tela_inicial', 'jogo', 'pausa', 'tela_final']
app_fps = pygame.time.Clock()  

rodar_app = True  # Indica se o app tá rodando
while rodar_app:
    app_fps.tick(FPS)
    tempo_tela += 1
    TELA_APP.fill((0, 0, 0))
    TELA_APP.blit(BACKGROUND, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar_app = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                rodar_app = False
            
            if tela_aplicativo == 'jogo':
                if event.key == ord('p'):
                    tela_aplicativo = 'pausa'

            elif tela_aplicativo == 'pausa':
                if event.key == ord('p'):
                    tela_aplicativo = 'jogo'

                elif event.key == ord('r'):
                    tempo_jogo = 0
                    tela_aplicativo = 'jogo'
                    
        if event.type == pygame.KEYUP:
            if tela_aplicativo == 'tela_inicial':
                if event.key == pygame.K_SPACE:
                    tela_aplicativo = 'jogo'

            elif tela_aplicativo == 'tela_final':
                if event.key == pygame.K_SPACE:
                    tempo_jogo = 0
                    tela_aplicativo = 'jogo'

    if tela_aplicativo == 'tela_inicial':

        if (tempo_tela//(FPS//2)) % 2 == 0:
            imagem_tela = TELA_INICIAL_IM2
        else:
            imagem_tela = TELA_INICIAL_IM1

        imagem_tela_tamanho = imagem_tela.get_rect().size

        TELA_APP.blit(imagem_tela, 
                        (LARGURA//2 - imagem_tela_tamanho[0]//2,
                        ALTURA//2 - imagem_tela_tamanho[1]//2))

            
    elif tela_aplicativo == 'jogo':

        if tempo_jogo == 0:
            player = Nave(USUARIO, TELA_APP, ATAQUE)
            vida = Vida(VIDA, TELA_APP)
            moeda = Moeda(MOEDA, TELA_APP)
            lista_inimigos = []
            tempo_respawn = 3
            lista_inimigos.append(Enemy(INIMIGO1, TELA_APP))

        
        # Enquanto estiver no jogo, o tempo de jogo será contado (o tempo atual é (tempo_jogo - 1)/60 segundos)
        tempo_jogo += 1

        if (tempo_jogo % int(tempo_respawn*FPS) == 0):
            lista_inimigos.append(Enemy(INIMIGO1, TELA_APP))

        if tempo_jogo//FPS >= 0 and (tempo_jogo % (10*FPS) == 0):
            lista_inimigos.append(Inimigo2(INIMIGO2, TELA_APP))

        if tempo_jogo % (15*FPS) == 0 and tempo_respawn > 0.4:
            tempo_respawn -= 0.2

        #surgir a vida
        vida.surgir(tempo_jogo, FPS, player)
        vida.sumir(tempo_jogo, FPS)


        #surgir moeda
        if player.moedas < 999:
            moeda.aparecer(tempo_jogo, FPS, player)

        if moeda.tem_moeda == True and colisao(player.x, player.y, player.tamanho, moeda.x, moeda.y, moeda.tamanho):
            player.moedas += 1
            moeda.tem_moeda = False  
        
        if vida.aparecer == True and player.vida < 10 and colisao(player.x, player.y, player.tamanho, vida.x, vida.y, vida.tamanho):
            player.vida += 1
            vida.aparecer = False

        for i in range(len(lista_inimigos)):
            if colisao(player.x, player.y, player.tamanho, lista_inimigos[i].rect[0], lista_inimigos[i].rect[1], lista_inimigos[i].tamanho):
                player.vida -= 1
                lista_inimigos[i].aparecer = False 

            if player.tiro == True and colisao(player.tiroX, player.tiroY, player.tiroTamanho, lista_inimigos[i].rect[0], lista_inimigos[i].rect[1], lista_inimigos[i].tamanho):
                player.inimigos += 1
                player.tiro = False
                lista_inimigos[i].aparecer = False 

        keys = pygame.key.get_pressed()
        player.controle(keys)

        # enemy.update()
        for i in range(len(lista_inimigos)):
            lista_inimigos[i].update()

        for inimigo in lista_inimigos:
            if inimigo.aparecer == False:
                lista_inimigos.remove(inimigo)

        if player.vida <= 0:
            tela_aplicativo = 'tela_final' 

        # Mostra os dados de Coleta Moeda e Abates na tela
        dados_game(player.moedas, player.inimigos, player.vida, tempo_jogo//FPS,  VIDA, TELA_APP)

        vida.desenhar()
        moeda.desenhar()
        for inimigo in lista_inimigos:
            inimigo.desenhar()

        player.desenhar()

        
    elif tela_aplicativo == 'pausa':
        dados_game(player.moedas, player.inimigos, player.vida, tempo_jogo//FPS,  VIDA, TELA_APP)

        vida.desenhar()
        moeda.desenhar()
        for inimigo in lista_inimigos:
            inimigo.desenhar()

        player.desenhar()


    elif tela_aplicativo == 'tela_final':

        tempo_tela += 1

        if (tempo_tela//(FPS//2)) % 2 == 0:
            imagem_tela = TELA_FINAL_IM2
        else:
            imagem_tela = TELA_FINAL_IM1

        imagem_tela_tamanho = imagem_tela.get_rect().size

        TELA_APP.blit(imagem_tela, 
                        (LARGURA//2 - imagem_tela_tamanho[0]//2,
                        ALTURA//2 - imagem_tela_tamanho[1]//2))

        dados_game(player.moedas, player.inimigos, player.vida, tempo_jogo//FPS,  VIDA, TELA_APP)

        vida.desenhar()
        moeda.desenhar()
        for inimigo in lista_inimigos:
            inimigo.desenhar()

        player.desenhar()
    
    # Aqui atualiza a tela inserindo todos os desenhos realizados pelo blit a cada rodar_app do while
    pygame.display.flip()


pygame.quit()