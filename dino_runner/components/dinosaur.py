import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,DUCKING,JUMPING, DEFAULT_TYPE, RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD, SHIELD_TYPE, HAMMER_TYPE, DUCKING_HAMMER,JUMPING_HAMMER,RUNNING_HAMMER



RUN_IMG= { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD,  HAMMER_TYPE: RUNNING_HAMMER} 
JUMP_IMG= { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER} 
DUCK_IMG= { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}


class Dinosaur(Sprite):

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
      self.playing = True
      self.type = DEFAULT_TYPE
      self.image= RUN_IMG[self.type][0]

      self.dino_duck = False
      self.dino_run = True
      self.dino_jump = False
      self.died = False
      self.step_index = 0

      
      self.dino_rect = self.image.get_rect()
      self.dino_rect.width *= 1
      self.dino_rect.height *= 1
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_POS
      self.jump_vel = self.JUMP_VEL

      self.has_power_up = False
      self.power_time_up = 0

    def update(self, userInput):
         
         if self.dino_duck:
             self.duck()
         if self.dino_run: 
             self.run()
         if self.dino_jump: 
             self.jump()
         if self.died:
             self.die()

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
         
         self.image = RUN_IMG[self.type] [self.step_index // 5]
         self.dino_rect = self.image.get_rect()
         self.dino_rect.x = self.X_POS
         self.dino_rect.y =self.Y_POS 
         self.step_index += 1
        
    def jump(self):
         
         self.image = JUMP_IMG[self.type] 
         if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
         if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False 
            self.jump_vel = self.JUMP_VEL
       
    
    def duck(self):
         
         self.image = DUCK_IMG[self.type] [self.step_index // 5]
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

         
          self.dino_rect = self.image.get_rect()
          self.dino_rect.x = self.X_POS
          self.dino_rect.y = self.Y_POS
          self.jump_vel = self.JUMP_VEL