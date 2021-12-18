import pygame

class Menu():
    def __init__(self, game): # "GAME" fazendo referência, algumas funções podem ser reutilizadas
        self.game = game # Acesso a todas as variaveis e funções de GAME

        self.mid_w, self.mid_h = self.game.DISPLAY_W // 2, self.game.DISPLAY_H // 2
         
        self.run_display = True  # Diz ao nosso menu para continuar em execução

        self.cursor_rect = pygame.Rect(0, 0, 30, 30) # O cursor vai ficar delimitado nesse espaço

        self.offset = -100  # Deslocamento do cursor

    def draw_cursor(self):
        # Desenhar o cursor
        self.game.draw_text('*', 20, self.cursor_rect.x, self.cursor_rect.y) # Pegando o Draw_text do outro arquivo e só mudando os valores

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game) # Referencia ao ("game") para pegar todas as coisas que fizemos antes 
        self.state = 'Start' # Cursor começa no START
        self.startx, self.starty = self.mid_w, self.mid_h + 30     # Colocando START na posição  
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60 # Colocando OPTIONS na posição 
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90 # Colocando CREDITS na posição  
        self.exitx, self.exity = self.mid_w, self.mid_h + 120      # Colocando EXIT na posição 
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) # Vai alinhar o (*) q é o cursor ao texto inicial do jogo

    def display_menu(self): # Exibir o menu
        self.run_display = True

        self.game.check_eventos()
        self.check_input()
        self.game.draw_text('The Galaxy War', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
        self.game.draw_text('Start Game', 20, self.startx, self.starty)
        self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
        self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
        self.game.draw_text('Exit', 20, self.exitx, self.exity)
        self.draw_cursor()
        self.game.restart_keys() 

    def move_cursor(self): # Basicamente serve para mover o cursor (cima pra baixo e baixo pra cima, sem parar)
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'

            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'

            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

    def check_input(self): # Checando o que o player quer
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options   # Menu atual passa para options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Exit':
                self.game.running = False
            self.run_display = False # Para o loop Display_Menu


class MenuOptions(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Controls'
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)


    def display_menu(self):
        self.run_display = True
        self.game.check_eventos()
        self.check_input()
        self.game.draw_text('Options', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
        self.game.draw_text('Controls', 20, self.controlsx, self.controlsy)
        self.draw_cursor()
        self.game.restart_keys() 

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False # Terminando o loop. Permitindo mudar o menu na prox iteração do loop principal

        if self.state == 'Controls':
            self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)

class CreditsMenu(Menu): # Criando os créditos
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        self.game.check_eventos()
        if self.game.START_KEY or self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        # Eu particularmente achei estranho, mas foi a única forma rápida q achei para colocar os nomes
        self.namex, self.namey = self.mid_w, self.mid_h + 20
        self.name1x, self.name1y = self.mid_w, self.mid_h + 50
        self.name2x, self.name2y = self.mid_w, self.mid_h + 80
        self.name3x, self.name3y = self.mid_w, self.mid_h + 110
        self.name4x, self.name4y = self.mid_w, self.mid_h + 140
        self.name5x, self.name5y = self.mid_w, self.mid_h + 170

        self.game.draw_text('Desenvolvido por', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
        self.game.draw_text('Everlon Figueiroa', 20, self.namex, self.namey)
        self.game.draw_text('Gabriel Pacheco', 20, self.name1x, self.name1y)
        self.game.draw_text('Gabriela Pinheiro', 20, self.name2x, self.name2y)
        self.game.draw_text('Guilherme Caio', 20, self.name3x, self.name3y)
        self.game.draw_text('Joao Pedro', 20, self.name4x, self.name4y)
        self.game.draw_text('Valter Junior', 20, self.name5x, self.name5y)
        self.game.restart_keys() 
