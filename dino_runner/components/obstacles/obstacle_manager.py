import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD, CLOUD, SHIELD_TYPE

class Obstacle_Manager:
    
    def __init__(self):
        self.obstacles = []
        self.counter = 100
        self.cloud =Cloud

    def generate_obstacle(self):
        
        obstacle = random.choice([Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS])), Bird (BIRD)])
        return obstacle
    
    def update(self, game):

        if len(self.obstacles) == 0:
             obstacle = self.generate_obstacle()
             self.obstacles.append(obstacle)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
              if game.player.type != SHIELD_TYPE:
                 pygame.time.delay(1000)
                 game.death_count +=1
                 game.playing= False
                 break
              else:
                self.obstacles.remove(obstacle)

       
    def draw(self, screen):

        for obstacle in self.obstacles:
            obstacle.draw(screen)
     
    def reset_obstacles(self):
        self.obstacles=[]