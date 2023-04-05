import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_Manager
from dino_runner.components.menu  import Menu
from dino_runner.components.score  import Score


class Game:
    
    GAME_SPEED = 20
    SCORE=0
    DEAD = 0
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.scor= Score()
        self.obstacle_manager = Obstacle_Manager()   
        self.menu = Menu("Press any key to start....... ", self.screen)  
        self.running = False 
        self.death_count = self.DEAD
        self.total_score= []
       

    def execute(self): 

        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):

        # Game loop: events - update - draw
        self.score = self.SCORE
        self.game_speed = self.GAME_SPEED   
        self.obstacle_manager.reset_obstacles()
        self.player.reset_dinosaur()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):

        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.obstacle_manager.update(self)
        self.update_score()
        ss=self.score #aca guardamos los datos del score en la lista total_score
        self.total_score.append(ss)

    def draw(self):

        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()  
        pygame.display.update()
        pygame.display.flip()    

    def draw_background(self):

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0: 
            self.menu.draw(self.screen) 
    
        else:
            self.menu.update_message("¡Game Over!")  
            self.scor.score("Your score is: "   + str(self.score))
            self.scor.total_score("Highest score: " +  str(max(self.total_score)))
            self.scor.total_deaths("Total Deaths: " + str(self.death_count))
            self.scor.update_message2("Press any key to restart... ") 

            self.menu.draw(self.screen)       
            self.scor.draw(self.screen)
            
        self.screen.blit(ICON, (half_screen_width -50, half_screen_height - 140))
        self.menu.update(self)
    
    def update_score(self):

        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5



    def draw_score(self):

        font = pygame.font. Font (FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect )