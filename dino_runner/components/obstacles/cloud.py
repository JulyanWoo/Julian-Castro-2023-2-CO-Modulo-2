import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cloud(Obstacle):
    
    Y_POS = 100

    def __init__(self, image):
        self.counter = 0
        self.image = [image]
        super().__init__(self.image, 3)