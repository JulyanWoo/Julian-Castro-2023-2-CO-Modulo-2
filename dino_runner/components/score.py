import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Score(Sprite):

    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self):
        self.total_scores = []
        self.font = pygame.font.Font(FONT_STYLE, 30) 


    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text1, self.text_rect1)
        screen.blit(self.text2, self.text_rect2)
        screen.blit(self.text3, self.text_rect3)


    def score(self, message):
        self.text = self.font.render(message, True, (0, 0, 0)) 
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, 360 )

    def total_score(self, message):
        self.text1 = self.font.render(message, True, (0, 0, 0)) 
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = (self.HALF_SCREEN_WIDTH, 390)

    def total_deaths(self, message):
        self.text2 = self.font.render(message, True, (0, 0, 0)) 
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH, 425)

    def update_message2(self, message):
         self.text3 = self.font.render(message, True, (0, 0, 0)) 
         self.text_rect3 = self.text3.get_rect()
         self.text_rect3.center = (self.HALF_SCREEN_WIDTH +20 , self.HALF_SCREEN_HEIGHT + 200)


