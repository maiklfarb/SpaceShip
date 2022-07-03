import pygame
from pygame.sprite import Sprite    # pygame - фреймворк (библиотека), sprite - файл, Sprite - класс

class Meteorit(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.image = pygame.image.load('Images/m.png')
        self.rect = self.image.get_rect()
        self.settings = game.settings

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def update(self):
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def checkEdges(self):
        # Проверка находится ли корабль у края
        screenReact = self.screen.get_rect()
        if self.rect.right >= screenReact.right or self.rect.left <= 0:
            return True