import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self): 
        # Inicializa una lista vacía de power-ups.
        self.power_ups = []
        # Cuando el primer power-up aparecerá (un número aleatorio entre 150 y 250).
        self.when_appears = random.randint(150, 250)
        # Duración de cada power-up (un número aleatorio entre 3 y 5).
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        # Genera un power-up aleatorio: escudo o martillo.
        if random.random() < 0.5:
            power_up = Shield()
        else:
            power_up = Hammer()
        # Actualiza cuando aparecerá el próximo power-up.
        self.when_appears += random.randint(150, 250) 
        # Agrega el power-up generado a la lista de power-ups.
        self.power_ups.append(power_up)

    def update(self, game):
        # Si no hay power-ups y se alcanzó el puntaje para que aparezca el primer power-up, genera uno.
        if len(self.power_ups) == 0 and self.when_appears == game.score:
            self.generate_power_up() 

        # Actualiza todos los power-ups en la lista.
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            # Si el rectángulo del jugador colisiona con el rectángulo de un power-up, el jugador obtiene ese power-up.
            if game.player.dino_rect.colliderect(power_up.rect):
                # Registra el momento en que el jugador obtiene el power-up.
                power_up.start_time = pygame.time.get_ticks()
                # El tipo de power-up del jugador se convierte en el tipo del power-up obtenido.
                game.player.type = power_up.type
                # El jugador tiene un power-up.
                game.player.has_power_up = True
                # El tiempo en que el power-up termina se establece sumando la duración del power-up al momento en que se obtuvo el power-up.
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                # Elimina el power-up de la lista de power-ups.
                self.power_ups.remove(power_up)
            
    def draw(self, screen):
        # Dibuja todos los power-ups en la pantalla.
        for power_up in self.power_ups: 
            power_up.draw(screen)

    def reset(self):
        # Restablece la lista de power-ups y el momento en que aparecerá el próximo power-up.
        self.power_ups = []
        self.when_appears = random.randint(150, 250)