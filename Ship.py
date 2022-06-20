import pygame
class Ship:
    #класс корабля - класс рабочий!
    def __init__(self, screen, settings):
        # Вытащим экран
        self.screen = screen
        # Инициализация корабля и задать начальную позицию
        self.scrinRect = screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load("Images/SHIP-9999.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.scrinRect.midbottom

        # Преобразование в десятичные числа
        self.x = float(self.rect.x)
        self.isRight = False
        self.isLeft = False

    def Update(self):
        if self.isLeft and self.rect.left > 0:
            self.x -= self.settings.speed
        if self.isRight and self.rect.right < self.scrinRect.right:
            self.x += self.settings.speed
        self.rect.x = self.x

    def blitme(self):
        # blit - отрисовка на экране картинки в нужной позиции
        self.screen.blit(self.image, self.rect)