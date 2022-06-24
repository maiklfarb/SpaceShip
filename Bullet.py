import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, settings, ship):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship
        self.colour = self.settings.bullet_colour
        self.rect = pygame.Rect(0, 0, self.settings.bullet_wight, self.settings.bullet_height)  # x, y, ширина, высота
        self.rect.midbottom = self.ship.rect.midtop

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def blitme(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)  # где рисуем, цвет, что рисуем