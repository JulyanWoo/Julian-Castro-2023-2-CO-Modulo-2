import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS

class Obstacle_Manager:
    
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        obstacle = Cactus(LARGE_CACTUS)
        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("chocaste")

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
