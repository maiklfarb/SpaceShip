import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, settings, ship, _type="default"):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship
        self.colour = self.settings.bullet_colour
        self.rect = pygame.Rect(0, 0, self.settings.bullet_wight, self.settings.bullet_height)  # x, y, ширина, высота
        self.rect.midbottom = self.ship.rect.midtop
        self._type = _type
        self.bulletSpeed = self.settings.bullet_speed

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.bulletSpeed
        self.rect.y = self.y

        if self._type != "default":
            if self._type == "right":
                self.x += self.bulletSpeed
            elif self._type == "left":
                self.x -= self.bulletSpeed
            self.rect.x = self.x


    def blitme(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)  # где рисуем, цвет, что рисуем