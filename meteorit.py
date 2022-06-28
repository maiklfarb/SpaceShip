import pygame
from pygame.sprite import Sprite    # pygame - фреймворк (библиотека), sprite - файл, Sprite - класс

class Meteorit(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.image = pygame.image.load('Images/m.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)