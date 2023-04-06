import pygame
import random

from dino_runner.utils.constants import BG,FLY, ICON, SCREEN_HEIGHT, SCREEN_WIDTH,RESETT, CLOUD, TITLE, FPS, FONT_STYLE, GAME_OVER, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_Manager
from dino_runner.components.menu  import Menu
from dino_runner.components.score  import Score
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

# Definimos la clase Game
class Game:
    GAME_SPEED = 20  # Velocidad del juego
    SCORE = 0  # Puntaje del jugador
    DEAD = 0  # Contador de muertes del jugador
    COUNT = 0  # Contador
    BACKGROUND_COLOR = ((255, 255, 255))  # Color de fondo del juego
    BACKGROUND_COLOR_ALT = ((109, 109, 109))  # Color de fondo alternativo del juego
    COLOR_CHANGE_SCORE = 500  # Puntaje necesario para cambiar el color de fondo

    def __init__(self):
        pygame.init()  # Inicializa Pygame
        pygame.display.set_caption(TITLE)  # Define el título de la ventana
        pygame.display.set_icon(ICON)  # Define el ícono de la ventana
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana
        self.clock = pygame.time.Clock()  # Crea el objeto Clock de Pygame
        self.playing = False  # Booleano que indica si se está jugando
        self.background_color_count = 0  # Contador para alternar colores de fondo
        self.background_color = ((255, 255, 255))  # Color de fondo blanco
        self.cloud_heights = [50, 100, 150]  # Alturas posibles para las nubes
        self.game_speed = self.GAME_SPEED  # Velocidad del juego
        self.x_pos_bg = 0  # Posición inicial del fondo
        self.y_pos_bg = 380  # Altura del fondo
        self.x_pos_c = SCREEN_WIDTH + random.randint(800, 1000)  # Posición inicial de la nube
        self.y_pos_c = self.cloud_heights[random.randint(0, 2)]  # Altura de la nube
        self.player = Dinosaur()  # Objeto Dinosaurio
        self.scor = Score()  # Objeto Score
        self.obstacle_manager = Obstacle_Manager()  # Objeto Obstacle_Manager
        self.power_up_manager = PowerUpManager()  # Objeto PowerUpManager
        self.menu = Menu("Press any key to start....... ", self.screen)  # Objeto Menu
        self.score = self.SCORE  # Puntaje
        self.running = False  # Booleano que indica si se está ejecutando
        self.death_count = self.DEAD  # Cantidad de veces que murió el jugador
        self.total_score= []  # Lista de puntajes
        self.background_color_count = self.COUNT  # Contador para alternar colores de fondo
        self.background_color = self.BACKGROUND_COLOR  # Color de fondo
        self.background_color_count = self.COUNT  # Contador para alternar colores de fondo
        self.sound= pygame.mixer.music.load("X2Download.ogg")  # Carga el sonido de fondo
        pygame.mixer.music.play(-1)  # Reproduce el sonido de fondo en loop
       
   # Método para ejecutar el juego
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    # Método principal para correr el juego
    def run(self):
        # Loop del juego: eventos, actualización y dibujo
        self.reset_variables()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    # Método para manejar eventos
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    # Método para actualizar el juego
    def update(self):

        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.obstacle_manager.update(self)
        self.update_score()
        ss=self.score -1 #aca guardamos los datos del score en la lista total_score
        self.total_score.append(ss)
        self.power_up_manager.update(self)

    def draw(self):

        self.clock.tick(FPS)
        self.update_background()
        self.screen.fill(self.background_color)
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()  
        self.draw_power_up_time()
        pygame.display.update()
        #pygame.display.flip()    
        

    def draw_background(self):

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    
    def update_background(self):

        if self.score % self.COLOR_CHANGE_SCORE == 0:
            if self.background_color_count == 0:
                self.background_color = self.BACKGROUND_COLOR_ALT
                self.background_color_count = 1
            else:
                self.background_color = self.BACKGROUND_COLOR
                self.background_color_count = 0

    def show_menu(self):

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0: 
            self.menu.draw(self.screen) 
    
        else:
            self.scor.score( "Your score is: "   + str(self.score -1))
            self.scor.total_score("Highest score: " +  str(max(self.total_score)))
            self.scor.total_deaths("Total Deaths: " + str(self.death_count))
            self.scor.update_message2("Press any key to restart... ") 

            self.scor.draw(self.screen)
            self.screen.blit(GAME_OVER, (half_screen_width -180, half_screen_height -200))
            self.screen.blit(RESETT, (half_screen_width -50, half_screen_height -20))  
        
        self.screen.blit(ICON, (half_screen_width -50, half_screen_height - 120))
        self.menu.update(self)
    
    def update_score(self):

        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5



    def draw_score(self):

        font = pygame.font.Font(FONT_STYLE, 30)
        if self.background_color == self.BACKGROUND_COLOR:
            text_color = (0, 0, 0)  # black text on white background
        else:
            text_color = (255, 255, 255)  # white text on black background
        text = font.render(f'Score: {self.score}', True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)




    def draw_power_up_time(self):

        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0: 
                 font = pygame.font.Font(pygame.font.get_default_font(), 20)
                 text = font.render(f'{self.player.type.capitalize()} enabled for {time_to_show} seconds', True, (0, 0, 0))
                 self.screen.blit(text, (380, 100))
            else:
                 self.player.has_power_up = False
                 self.player.type = DEFAULT_TYPE
    
    def draw_cloud(self):
     
     self.screen.blit(CLOUD, (self.x_pos_c, self.y_pos_c))
     self.x_pos_c -= self.game_speed / 2
     if self.x_pos_c < -CLOUD.get_width():
        self.x_pos_c = SCREEN_WIDTH + random.randint(400, 800)
        # Update cloud height
        self.y_pos_c = self.cloud_heights[random.randint(0, 2)]



    def reset_variables(self):
        self.background_color_count = 0
        self.background_color = self.BACKGROUND_COLOR
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.scor = Score()
        self.obstacle_manager = Obstacle_Manager()
        self.power_up_manager = PowerUpManager()
        self.score = self.SCORE
        self.background_color_count = self.COUNT
        self.sound= pygame.mixer.music.load("X2Download.ogg")
        pygame.mixer.music.play(-1)