import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD, CLOUD, SHIELD_TYPE, HAMMER_TYPE

class Obstacle_Manager:
    
    def __init__(self):
        self.obstacles = []  # Lista para almacenar los obstáculos
        self.counter = 100  # Contador para generar nuevos obstáculos
        

    def generate_obstacle(self):
        # Método para generar un obstáculo aleatorio (cactus o pájaro)
        obstacle = random.choice([Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS])), Bird (BIRD)])
        return obstacle
    
    def update(self, game):
        # Método para actualizar los obstáculos en pantalla
        if len(self.obstacles) == 0:  # Si no hay obstáculos en pantalla
            obstacle = self.generate_obstacle()  # Generar un obstáculo aleatorio
            self.obstacles.append(obstacle)  # Agregarlo a la lista de obstáculos
        
        for obstacle in self.obstacles:  # Para cada obstáculo en la lista
            obstacle.update(game.game_speed, self.obstacles)  # Actualizar su posición y estado
            if game.player.dino_rect.colliderect(obstacle.rect):  # Si el dinosaurio choca con el obstáculo
                if game.player.type != HAMMER_TYPE:  # Si el dinosaurio no tiene martillo
                    if game.player.type != SHIELD_TYPE:  # Si el dinosaurio no tiene escudo
                        pygame.time.delay(1000)  # Pausar el juego por 1 segundo
                        game.death_count +=1  # Aumentar el contador de muertes
                        game.playing= False  # Terminar el juego
                        break  # Salir del bucle
                else:  # Si el dinosaurio tiene martillo
                    self.obstacles.remove(obstacle)  # Eliminar el obstáculo de la lista
        
    def draw(self, screen):
        # Método para dibujar los obstáculos en pantalla
        for obstacle in self.obstacles:  # Para cada obstáculo en la lista
            obstacle.draw(screen)  # Dibujarlo en pantalla
     
    def reset_obstacles(self):
        # Método para reiniciar la lista de obstáculos
        self.obstacles=[]  # Vaciar la lista de obstáculos