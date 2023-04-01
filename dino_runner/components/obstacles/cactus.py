import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus (Obstacle):

    def __init__(self, image):

        self.type = random.randint(0, 3)    
        super().__init_(image, self.type) 
        self.rect.y = 325
