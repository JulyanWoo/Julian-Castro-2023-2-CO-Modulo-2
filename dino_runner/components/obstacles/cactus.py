import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):

    Y_POS = 340

    def __init__(self, image):
       self.type = random.randint(0, 2)  
       super().__init__(image, self.type) 
       self.position()

    def position(self):
        self.rect.y = self.Y_POS - (self.rect.h - 71)
