import pygame  # a biblioteca do pygame
import random  # para pegar valores aleatórios
from pygame import mixer

# As funções que eu tinha feito e esqueci de por aplicar aqui (Everlon)
# def pos_inimigo_aleatoria(p_x, p_y, w, h, en_size, p_size):
#     x_en, y_en = w - en_size[0], random.randint(0, h - en_size[1])
#     while (p_x <= x_en and x_en <= p_x + p_size[0]) and (p_y <= y_en and y_en <= p_y + p_size[1]):
#         x_en, y_en = w - en_size[0], random.randint(0, h - en_size[1])

#     return x_en, y_en

# def pos_vidas_moedas_aleatoria(p_x, p_y, w, h, obj_size, p_size):
#     x_obj, y_obj =  random.randint(0, w - obj_size[0]), random.randint(0, h - obj_size[1])
#     while (p_x <= x_obj and x_obj <= p_x + p_size[0]) and (p_y <= y_obj and y_obj <= p_y + p_size[1]):
#         x_obj, y_obj = random.randint(0, w - obj_size[0]), random.randint(0, h - obj_size[1])

#     return x_obj, y_obj

# def colide(x_a, y_a, tam_a, x_b, y_b, tam_b): # Checa se a e b colidem
#     if (x_a <=  x_b + tam_b[0] and x_b <= x_a + tam_a[0]) and (y_a <=  y_b + tam_b[1] and y_b <= y_a + tam_a[1]):
#         return True
#     else:
#         return False


def pos_inimigo_aleatoria(p_x, p_y, w, h, en_size, p_size):
    # Essa função pode ter as variaveis reescrita no futuro,
    # mas como é função vou deixar pra depois.
    # uma função que recebe os paramêtros da tela e da posição do player
    # O tamanho do player e do objeto
    # e retorna uma tuple da posição aleatória que o objeto irá aparecer
    # Obs.: todos objetos aparecem do lado direito (de quem observa ->) da tela

    x_en, y_en = w - en_size[0], random.randint(0, h - en_size[1])
    while (p_x <= x_en and x_en <= p_x + p_size[0]) and (p_y <= y_en and y_en <= p_y + p_size[1]):
        # Esse while é para o objeto não nascer no lugar que o usuário está
        x_en, y_en = w - en_size[0], random.randint(0, h - en_size[1])

    return x_en, y_en


def pos_vidas_moedas_aleatoria(p_x, p_y, w, h, obj_size, p_size):
    # Essa função pode ter as variaveis reescrita no futuro,
    # mas como é função vou deixar pra depois.
    # uma função que recebe os paramêtros da tela e da posição do player
    # O tamanho do player e do objeto
    # e retorna uma tuple da posição aleatória que o objeto irá aparecer
    # Obs.: todos objetos aparecem do lado direito (de quem observa ->) da tela

    x_obj, y_obj = random.randint(
        0, w - obj_size[0]), random.randint(0, h - obj_size[1])
    while (p_x <= x_obj and x_obj <= p_x + p_size[0]) and (p_y <= y_obj and y_obj <= p_y + p_size[1]):
        # Esse while é para o objeto não nascer no lugar que o usuário está
        x_obj, y_obj = random.randint(
            0, w - obj_size[0]), random.randint(0, h - obj_size[1])

    return x_obj, y_obj


def dados_game(moeda_capturada, TELA_APP, pontuacao):
    # Essa função serve para colocar os dados de coleta de moeda
    # Ou colisão com o inimigo, na tela

    message_coin = f'Moedas: {moeda_capturada}'
    formatted_text_coin = fonte.render(message_coin, True, (255, 255, 255))

    message_enemy = f'Abates: {pontuacao}'
    formatted_text_enemy = fonte.render(message_enemy, True, (255, 255, 255))

    TELA_APP.blit(formatted_text_coin, (840, 5))
    TELA_APP.blit(formatted_text_enemy, (420, 5))


vel_usuario = 6  # vel de velocidade, o usuário anda por 6 pixels por movimento

vel_inimigo1 = 4  # velocidade do inimigo 1, o 1 é o inimigo pequeno e lento
vel_inimigo2 = 2  # velocidade do inimigo 2, ele é grande e precisa de 2 tiros para destruir
# e quando ele leva 1 tiro ele vira o inimigo 1
vel_inimigo3 = 12  # velocidade do inimigo 3, ele é mais rápido, mas anda pelas diagonais

# A pontuação do usuario, ele recebe pontos quando acerta um inimigo por enquanto...
pontuacao = 0

pygame.font.init()  # Iniciando
# A fonte que aparece na tela ainda não é essa
fonte = pygame.font.SysFont('8-BIT WONDER.TTF', 35, True, True)
# Mas logo logo vai ta bonitinho

MAX_VIDAS = 10  # O Máximo de vidas que o usuario pode ter
INICIAL_VIDAS = 4  # A quantidade inicial de vidas do usuario por partida
tem_vida = False  # Indica se há alguma vida na tela


tempo_jogo = 0  # O tempo que passa durante o jogo, é checado para momentos como a pausa,
# Se o tempo for 0 significa que é o início de um novo jogo, se não é a continuação
# de um anterior

ajuste = 0  # Por enquanto é uma variável auxiliar usada para fazer o efeito de ficar piscando da
# tela inicial e da tenha de game over.
# Essa variável trabalha junto do ajuste pra saber qual a imagem que tá na tela
qual_imagem = 1
# Essa variaável só vai assumir valores de 1 e -1

LARGURA, ALTURA = 1000, 600  # Largura e altura da tela do aplicativo

# Para a àrea de movimento nos jogos agora, uma largura e altura mínima serão definidas
# A gente define essa área de movimento para que tenha um espaço vazio para depois colocar coisas
# que ficaram ocupando espaço na tela feito a pontuação e tals
# A gente considera a tupla (LARGURA, ALTURA) como sendo a máxima

# Inicia o pygame para que eu possa começar a carregar as imagens e outras coisas.
pygame.init()

# Iniciando mixer
mixer.init()

# Não sei pq ta sublinhado como vermelho, mas executa normalmente
musica_fundo = pygame.mixer.music.load('Sons\BoxCat Games - Mission.mp3')  # Buscando a música
##musica_fundo = pygame.mixer.music.load('Alexey_Anisimov_-_Space_Cyberpunk.mp3')
# Startando a música
# Se passar menos -1 para a função, ela fica em Loop
pygame.mixer.music.play(-1)

app_fps = pygame.time.Clock()  # É usado depois para definir o fps do aplicativo

# Sound Effect
sound_effect_collect = pygame.mixer.Sound('Sons\smw_message_block.wav')
sound_effect_lazer = pygame.mixer.Sound('Sons\Shofixti-Shot.wav')
sound_effect_health = pygame.mixer.Sound('Sons\smw_kick.wav')

# Carregando o background
###########

# Define a tela do momento atual em que o aplicativo do jogo está
tela_aplicativo = 'tela_inicial'
# Ela é divididae em: ['tela_inicial', 'jogo', 'pausa', 'tela_final']

TELA_APP = pygame.display.set_mode((LARGURA, ALTURA))  # A tela do aplicativo
# Nome do app, aparece no canto de <- da tela...
pygame.display.set_caption('Joguin')

# Carrega a imagem do usuario
USUARIO = pygame.image.load('Imagens\ship_2.png')
# pega o tamanho do usuario, é tuple de (largura, altura)
TAM_USUARIO = USUARIO.get_rect().size


# Carrega a imagem do inimigo 1
INIMIGO1 = pygame.image.load('Imagens\pixel_ship_yellow2.png')
# pega o tamanho do inimigo 1, tuple (largura, altura)
TAM_INIMIGO1 = INIMIGO1.get_rect().size
# Por enquanto o programa só tem o inimigo 1

# INIMIGO2 = pygame.image.load("sqgreen.png") # Carrega a imagem do inimigo 1
# TAM_INIMIGO2 = INIMIGO2.get_rect().size # pega o tamanho do inimigo 1, tuple (largura, altura)
##
# INIMIGO3 = pygame.image.load("sqpurple.png") # Carrega a imagem do inimigo 1
# TAM_INIMIGO3 = INIMIGO3.get_rect().size # pega o tamanho do inimigo 1, tuple (largura, altura)

# Carrega a imagem da moeda
MOEDA = pygame.image.load('Imagens\coin_2.png')
# pega o tamanho da moeda, tuple (largura, altura)
TAM_MOEDA = MOEDA.get_rect().size
tem_moeda = False  # Indica se tem moeda na tela

# Carrega a imagem do laser usado pelo usuario para atacar
ATAQUE = pygame.image.load("Imagens\lazer2.png")
# tamanho da imagem do lazer, (largura, altura)
TAM_ATAQUE = ATAQUE.get_rect().size
# boolean que indica se o ataque aparece na tela no momento atual.
aparecer_ataque = False

# carrega a imagem da vida (coração)
VIDA = pygame.image.load('Imagens\Health2.png')
TAM_VIDA = VIDA.get_rect().size  # o tamanho da imagem da vida, (larg, alt)

# Imagem do backgrond
BACKGROUND = pygame.image.load("Imagens\galaxy_background.png")

# É só a imagem da tela inicial em branco
TELA_INICIAL_IM1 = pygame.image.load("Imagens/1.png")
TELA_INICIAL_IM2 = pygame.image.load("Imagens/2.png")  # e aqui a mesma imagem em azul

TELA_FINAL_IM1 = pygame.image.load("Imagens/3.png")  # imagem da tela final em branco
TELA_FINAL_IM2 = pygame.image.load("Imagens/4.png")  # a mesma só q azul

imagem_na_tela = TELA_INICIAL_IM1  # Define a imagem que está na tela do programa
# começa com esse pois é a imagem da tela inicial

##############################################
# OS BLOCOS DO APLICATIVO:
##
# if tela_aplicativo == 'tela_inicial':
# pass
##
# if tela_aplicativo == 'jogo':
# pass
##
# if tela_aplicativo == 'pausa':
# pass
##
# if tela_aplicativo == 'tela_final':
# pass
##############################################


rodar_app = True  # Indica se o app tá rodando
while rodar_app:
    # Define o FPS da app, se colocado dentro dos if principais
    app_fps.tick(60)
    # (os que define a tela_aplicatido) então define o FPS daquela tela.

    # Coloco o fundo da tela como o RGB = (0,0,0) que indica a cor preta
    #TELA_APP.fill((0, 0, 0))
    TELA_APP.blit(BACKGROUND, (0,0))
    # Começo criando o fundo da tela para colocar os outros objetos em cima dele usando o .blit()

    if tela_aplicativo == 'tela_inicial':

        ajuste += 1  # Aqui começa a contar o tempo em que está na tela inicial
        if ajuste % 30 == 0:  # Esse if é só para controlar a imagem que está na tela inicial
            qual_imagem *= -1  # qual_imagem vai mudar entre 1 e -1 apenas

            if qual_imagem == 1:
                imagem_na_tela = TELA_INICIAL_IM1

            else:
                imagem_na_tela = TELA_INICIAL_IM2

        # Esse for a seguir vai checar todos os eventos que ocorrem na tela do aplicativo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pygame.QUIT indica que clicou no X de fechar a tela
                rodar_app = False  # quanto o rodar_app recebe False o while para

            if event.type == pygame.KEYUP:  # pygame.KEYUP indica quando uma tecla é solta
                if event.key == ord(" "):  # Se a techa solta dor o espaço:...
                    ajuste = 0  # O ajuste é zeradao quando sai da tela inicial para ser reusado na tela final
                    tela_aplicativo = 'jogo'  # A tela do aplicativo muda para jogo

            if event.type == pygame.KEYDOWN:  # pygame.KEYUP indica quando uma tecla é apertada
                if event.key == pygame.K_ESCAPE:  # se apertar esc o jogo fecha
                    rodar_app = False

        tam_imagem_na_tela = imagem_na_tela.get_rect().size
        # Pego o tamanho da imagem que está na tela,
        # que podem ser TELA_INICIAL_IM1 ou TELA_INICIAL_IM2 nesse caso

        x_imagem, y_imagem = (
            LARGURA - tam_imagem_na_tela[0])//2, (ALTURA - tam_imagem_na_tela[1])//2
        # x_imagem, y_imagem indicam a posição em pixels do canto superior esquerdo de imagem_na_tela
        # Essa posição coloca a imagem no meio da tela

        # Indica a posição da imagem USUARIO
        x, y = 0, (ALTURA - TAM_USUARIO[1])//2
        # Essa posição coloca a imagem no canto da esquerda em x e o meio em y.

        # Aqui começamos a desenhar na tela do app
        # Esse desenho a seguir é o desenho que fica na tela inicial apenas.

        # TELA_APP.blit(imagem, tuple com a pos da imagem) coloca as imagens na tela
        # Para colocar as vidas no topo da tela, a quantidade inicial de vidas
        for i in range(INICIAL_VIDAS):
            TELA_APP.blit(VIDA, (i*TAM_VIDA[0], 0))

        TELA_APP.blit(imagem_na_tela, (x_imagem, y_imagem))
        TELA_APP.blit(USUARIO, (x, y))
        pygame.display.flip()  # Atualiza a tela com as novas informações a serem adicionadas

    if tela_aplicativo == 'jogo':

        if tempo_jogo == 0:
            # O tempo de jogo é 0 apenas quando a partida começa, então isso tá definindo as posições iniciais
            # do usuario e do primeiro inimigo que aparece na tela
            # A quantidade de vidas que o usuário tem atualmente na partida, no caso no inicio.
            qt_vidas = INICIAL_VIDAS
            pontuacao = 0  # Sempre que o jogo começa a pontuação zera.
            moeda_capturada = 0  # quantidade de moedas capturadas

            # Quando o jogo começa o ataque não foi feito ainda, então n aparece.
            aparecer_ataque == False
            # O usuario começa no meio do lado da esquerda <-
            x_usuario, y_usuario = 0, (ALTURA - TAM_USUARIO[1])//2
            x_inimigo1, y_inimigo1 = pos_inimigo_aleatoria(
                x_usuario, y_usuario, LARGURA, ALTURA, TAM_INIMIGO1, TAM_USUARIO)
            # O inimigo1 (quadrado vermelho) começa numa posição aleatória.

        # Enquanto estiver no jogo, o tempo de jogo será contado (o tempo atual é (tempo_jogo - 1)/60 segundos)
        tempo_jogo += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar_app = False
            if event.type == pygame.KEYDOWN:  # Indica se uma tecla foi pressionada
                # Se presionar a tecla p ele vai pra pausa, pode mudar a tecla depois...
                if event.key == ord('p'):
                    tela_aplicativo = 'pausa'

        keys = pygame.key.get_pressed()
        # Agora vem, qual a diferença entre usar o pygame.key.get_pressed() e fazer o if checando com o pygame.keydown?
        # A resposta é, o pygame.KEYDOWN vai só checar se a tecla foi aperta e não se ela está sendo pressionada,
        # Ou seja, ele só da a resposta de um clique por vez, já o get_pressed vai dizer se ela ainda está sendo pressionada
        # então para algo de pressionar e segurar a tecla o keydown só vai dar resultado uma vez e o .get_pressed vai continuar
        # dando o resultado.

        # pygame.key.get_pressed()[Número da tecla em ascii]  == keys[Número da tecla em ascii]
        # retorna true se a tecla estiver sendo pressionada e false se não
        if keys[pygame.K_ESCAPE]:  # pygame.K_ESCAPE é o ord do esc, tem todos na documentação do pygame.key
            rodar_app = False

        # K_UP, K_DOWN,... São referente às setinhas do teclado...
        # Esse x > 0 define o limite do quanto ele pode ir pra esquerda
        if (keys[pygame.K_LEFT] or keys[ord("a")]) and x_usuario > 0:
            x_usuario -= vel_usuario

        # o x < ... é o limite que ele por ir pra a direita...
        if (keys[pygame.K_RIGHT] or keys[ord("d")]) and x_usuario < LARGURA - TAM_USUARIO[0]:
            x_usuario += vel_usuario

        if (keys[pygame.K_UP] or keys[ord("w")]) and y_usuario > 0:  # mesmo estilo aqui
            y_usuario -= vel_usuario

        if (keys[pygame.K_DOWN] or keys[ord("s")]) and y_usuario < ALTURA - TAM_USUARIO[1]:  # e aqui
            y_usuario += vel_usuario

        if (keys[ord("q")] or keys[ord(" ")]) and aparecer_ataque == False:
            # Aqui diz que se o ataque não tiver na tela ele pode atacar, tipo isso
            sound_effect_lazer.play()  # Toda vez que clicar para atacar, vai ter um efeito"

            x_ataque, y_ataque = x_usuario, y_usuario + \
                (TAM_USUARIO[1] - TAM_ATAQUE[1])//2
            # em cima é só definindo a posição que o ataque aparece, que é no meio do usuario

            aparecer_ataque = True
            # Como aparecer ataque é true ele não pode atacar de novo

        if (x_usuario <= x_inimigo1 + TAM_INIMIGO1[0] and x_inimigo1 <= x_usuario + TAM_USUARIO[0]) and (y_usuario <= y_inimigo1 + TAM_INIMIGO1[1] and y_inimigo1 <= y_usuario + TAM_USUARIO[1]):
            # Aqui ele checa a colisão, se a area da imagem do usuário colidiu com a area da imagem do inimigo,
            # pra isso ele usa o x e y do usuario e do inimigo além do tamanho deles...
            # é bom ler esse if até entender pra implementar depois viu...

            # Se chocou com o inimigo ele diminui a quantidade de vidas do usuario nessa partida.
            qt_vidas -= 1
            if qt_vidas == 0:  # Se a quantidade de vidas chegou a zero ele vai pra tela final que é a de game over
                tela_aplicativo = 'tela_final'
            else:  # se a quantidade de vidas não chegou a zero ele chama o novo inimigo que vai nascer na posição aleatoria
                x_inimigo1, y_inimigo1 = pos_inimigo_aleatoria(
                    x_usuario, y_usuario, LARGURA, ALTURA, TAM_INIMIGO1, TAM_USUARIO)

        # Agora aqui é implementando o movimento do inimigo1, ele checa onde o inimigo1 tá e faz ele andar pra a esquerda
        # subtraindo apenas no valor do do inimigo, e quando o x_inimigo1 passa pela borda da esquerda da tela ele reseta ele
        # e gera a posição aleatoria que o prox inimivo vai aparecer.
        if x_inimigo1 > 0 and x_inimigo1 <= LARGURA - TAM_INIMIGO1[0]:
            x_inimigo1 -= vel_inimigo1
        elif x_inimigo1 <= 0:
            x_inimigo1, y_inimigo1 = pos_inimigo_aleatoria(
                x_usuario, y_usuario, LARGURA, ALTURA, TAM_INIMIGO1, TAM_USUARIO)


############
        if tempo_jogo % 180 == 0:  # isso indica a cada 3 segundos
            tem_moeda = True
            x_moeda, y_moeda = pos_vidas_moedas_aleatoria(
                x_usuario, y_usuario, LARGURA, ALTURA, TAM_MOEDA, TAM_USUARIO)

            if tem_vida == False and qt_vidas < MAX_VIDAS:
                # isso implica que há uma chance aleatória de 20% de aparecer uma vida a cada 3 segundos de jogo
                if random.randint(0, 100) < 20:
                    tem_vida = True
                    x_vida, y_vida = pos_vidas_moedas_aleatoria(
                        x_usuario, y_usuario, LARGURA, ALTURA, TAM_VIDA, TAM_USUARIO)

            elif tem_vida == True:
                tem_vida = False
                

        # Para colocar as vidas no topo da tela, a quantidade inicial de vidas
        for i in range(qt_vidas):
            # É o primeiro blit a ser feito para que ele fique "em baixo" das outras imagens.
            TELA_APP.blit(VIDA, (i*TAM_VIDA[0], 0))

        if tem_moeda == True:
            TELA_APP.blit(MOEDA, (x_moeda, y_moeda))
            if (x_usuario <= x_moeda + TAM_MOEDA[0] and x_moeda <= x_usuario + TAM_USUARIO[0]) and (y_usuario <= y_moeda + TAM_MOEDA[1] and y_moeda <= y_usuario + TAM_USUARIO[1]):
                # Toda vez que o usuário coletar a moeda, vai ter um efeito
                sound_effect_collect.play()
                moeda_capturada += 1
                print(f"moedas: {moeda_capturada}")
                tem_moeda = False

        if tem_vida == True:
            TELA_APP.blit(VIDA, (x_vida, y_vida))
            if (x_usuario <= x_vida + TAM_VIDA[0] and x_vida <= x_usuario + TAM_USUARIO[0]) and (y_usuario <= y_vida + TAM_VIDA[1] and y_vida <= y_usuario + TAM_USUARIO[1]):
                qt_vidas += 1
                # Toda vez que o usuário coletar o coração, vai ter um efeito
                sound_effect_health.play()
                tem_vida = False

        # Aqui é o movimento do laser usado para o ataque, se o ataque foi realizado então aparecer ataque vira true e
        # temos os valores de x e y do ataque, então só precisamos fazer ele se mover agora
        # o movimento segue apenas para a direita então imcrementamos apenas o valor de x do ataque
        if aparecer_ataque == True:
            x_ataque += TAM_ATAQUE[0]

            if x_ataque <= LARGURA:
                # aqui diz que o ataque será desenhado na tela, que ocorre apenas
                TELA_APP.blit(ATAQUE, (x_ataque, y_ataque))
                # enquanto o x_ataque está aparecendo na tela
            else:
                # se o desenho do ataque sai da tela então aqui vira false oq permite
                aparecer_ataque = False
                # um novo ataque ser realizado.

            if (x_ataque <= x_inimigo1 + TAM_INIMIGO1[0] and x_inimigo1 <= x_ataque + TAM_USUARIO[0]) and (y_ataque <= y_inimigo1 + TAM_INIMIGO1[1] and y_inimigo1 <= y_ataque + TAM_USUARIO[1]):
                # Aqui é checando a colisão do ataque com um inimigo se a colisão acontecer a pontuação aumenta
                # e uma nova posição para o inimigo é gerada.
                pontuacao += 1
                aparecer_ataque = False
                print(pontuacao)
                x_inimigo1, y_inimigo1 = pos_inimigo_aleatoria(
                    x, y, LARGURA, ALTURA, TAM_INIMIGO1, TAM_USUARIO)

        # Aqui diz que o usuario e o inimigo será desenhado na tela e a posição deles
        # a ordem que ele desenha é em ordem dado os blit então
        # o desenho do usuario fica abaixo do desenho do inimigo e o desenho do ataque fica abaixo de todos ou outros quando ele é feito
        TELA_APP.blit(USUARIO, (x_usuario, y_usuario))
        TELA_APP.blit(INIMIGO1, (x_inimigo1, y_inimigo1))
        # Mostra os dados de Coleta Moeda e Abates na tela
        dados_game(moeda_capturada, TELA_APP, pontuacao)

        # Aqui atualiza a tela inserindo todos os desenhos realizados pelo blit a cada rodar_app do while
        pygame.display.flip()

    if tela_aplicativo == 'pausa':
        dados_game(moeda_capturada, TELA_APP, pontuacao)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar_app = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('p'):
                    tela_aplicativo = 'jogo'

                # r da restart no jogo, aí o tempo_jogo zera então o jogo vai pra as configs iniciais
                if event.key == ord('r'):
                    tempo_jogo = 0
                    tela_aplicativo = 'jogo'

                if event.key == pygame.K_ESCAPE:  # se apertar esc o jogo fecha
                    rodar_app = False

        for i in range(qt_vidas):  # Para colocar as vidas no topo da tela
            TELA_APP.blit(VIDA, (i*TAM_VIDA[0], 0))

        if aparecer_ataque == True:  # Se o laser estava na tela quando deu o pause ele continua na tela
            TELA_APP.blit(ATAQUE, (x_ataque, y_ataque))

        if tem_moeda == True:
            TELA_APP.blit(MOEDA, (x_moeda, y_moeda))

        if tem_vida == True:
            TELA_APP.blit(VIDA, (x_vida, y_vida))

        TELA_APP.blit(USUARIO, (x_usuario, y_usuario))
        TELA_APP.blit(INIMIGO1, (x_inimigo1, y_inimigo1))

        pygame.display.flip()

    if tela_aplicativo == 'tela_final':  # a tela do game over
        dados_game(moeda_capturada, TELA_APP, pontuacao)

        if ajuste % 30 == 0:  # Esse if é só para controlar a imagem que está na tela inicial
            qual_imagem *= -1  # qual_imagem vai mudar entre 1 e -1 apenas

            if qual_imagem == 1:
                imagem_na_tela = TELA_FINAL_IM1

            else:
                imagem_na_tela = TELA_FINAL_IM2

        ajuste += 1  # Aqui começa a contar o tempo em que está na tela inicial
        # Obs.: só lembrando que ele foi zerado ao sair da tela inicial.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar_app = False

            if event.type == pygame.KEYUP:
                # Se o usuario aperta a barra de espaço o jogo reinicia
                if event.key == ord(" "):
                    # lembrando: sempre que o tempo de jogo é zerado ele reinicia tudo.
                    tempo_jogo = 0
                    # E novamente o ajuste é zerado, pois se o usuario perder de novo ele volta pra essa tela aqui.
                    ajuste = 0
                    tela_aplicativo = 'jogo'

                if event.key == pygame.K_ESCAPE:
                    rodar_app = False

        tam_imagem_na_tela = imagem_na_tela.get_rect().size
        
        x_imagem, y_imagem = (
            LARGURA - tam_imagem_na_tela[0])//2, (ALTURA - tam_imagem_na_tela[1])//2

        # A imagem fica abaixo de todos
        TELA_APP.blit(imagem_na_tela, (x_imagem, y_imagem))

        # Para colocar as vidas, mas nem precisa pq ele tem 0 vidas...
        for i in range(qt_vidas):
            TELA_APP.blit(VIDA, (i*TAM_VIDA[0], 0))

        if aparecer_ataque == True:  # Se o laser estava na tela quando acabou ele continua na tela, feito o pause
            TELA_APP.blit(ATAQUE, (x_ataque, y_ataque))

        TELA_APP.blit(USUARIO, (x_usuario, y_usuario))
        TELA_APP.blit(INIMIGO1, (x_inimigo1, y_inimigo1))

        pygame.display.flip()


pygame.quit()
