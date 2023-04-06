import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cloud(Obstacle):

    Y_POS = 100

    def __init__(self, image):
       self.height_position = random.randint(0,2)
       super().__init__(image, 3) 
       self.position()

    def position(self): 
        self.rect.y = self.Y_POS - (self.height_position * 50)
