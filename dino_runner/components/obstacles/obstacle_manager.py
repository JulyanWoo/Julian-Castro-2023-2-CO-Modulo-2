import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class Obstacle_Manager:
    
    def __init__(self):
        self.obstacles = []
        self.counter = 100

    def generate_obstacle(self):
        
        obstacle = random.choice([Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS])), Bird (BIRD)])
        return obstacle
    
    def update(self, game):
        self.counter += 1
        if self.counter > 60:
            self.counter = random.randint(0, 40)
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
              pygame.time.delay(1000)
              game.playing= False
              break

       
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
     