import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,DUCKING,JUMPING
class Dinosaur(Sprite):

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
    
      self.duck_img = DUCKING 
      self.run_img = RUNNING
      self.jump_img = JUMPING

      self.dino_duck = False
      self.dino_run = True
      self.dino_jump = False
      self.step_index = 0

      self.image = self.run_img[0]
      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_POS
      self.jump_vel = self.JUMP_VEL

    def update(self, userInput):
         
         if self.dino_duck:
             self.duck()
         if self.dino_run: 
             self.run()
         if self.dino_jump: 
             self.jump()
         if self.step_index>= 10: 
            self.step_index = 0

         if userInput [pygame.K_SPACE] or userInput [pygame.K_UP] and not self.dino_jump:
             self.dino_duck = False
             self.dino_run = False
             self.dino_jump = True
             

         elif userInput [pygame.K_DOWN] and not self.dino_jump:
             self.dino_duck = True
             self.dino_run = False
             self.dino_jump = False

         elif not (self.dino_jump or userInput [pygame.K_DOWN]):
             self.dino_duck = False
             self.dino_run = True
             self.dino_jump = False

    def run(self):
         
         self.image= RUNNING[0] if self.step_index < 5 else RUNNING[1]
         self.dino_rect = self.image.get_rect()
         self.dino_rect.x = self.X_POS
         self.dino_rect.y =self.Y_POS 
         self.step_index += 1
        
    def jump(self):
         
         self.image = self.jump_img

         if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
         if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False 
            self.jump_vel = self.JUMP_VEL
       
    
    def duck(self):
         
         self.image= DUCKING[0] if self.step_index < 5 else DUCKING[1]
         self.dino_rect = self.image.get_rect()
         self.dino_rect.x = self.X_POS
         self.dino_rect.y =self.Y_POS_DUCK 
         self.step_index += 1 
    
       
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def reset_dinosaur(self):
          self.dino_duck = False
          self.dino_run = True
          self.dino_jump = False
          self.step_index = 0

          self.image = self.run_img[0]
          self.dino_rect = self.image.get_rect()
          self.dino_rect.x = self.X_POS
          self.dino_rect.y = self.Y_POS
          self.jump_vel = self.JUMP_VEL