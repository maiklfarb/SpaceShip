import sys  # библиотека для взаимодействия с операционной системой
import pygame
from Settings import Settings
from Ship import Ship

class SpaceShip:
    def __init__(self):
        # Инициализация игры и всех библиотек PyGame (движка)
        pygame.init()
        # Создание объекта настроек
        self.settings = Settings()
        # Сохранение дисплея, а также установка высоты и ширины с помощью кортежа, используя объект settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.scrinWidth = self.screen.get_rect().width
        self.settings.scrinHeight = self.screen.get_rect().height
        # Установка названия сверху у экрана игры
        pygame.display.set_caption("Space Ship Game")
        self.ship = Ship(self.screen, self.settings)
    def CheckDown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.isRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.isLeft = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
    def CheckUp(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.isRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.isLeft = False
    def CheckEvent(self):
        # Проходим все события (нажатия клавиш, движения мышью и т.д.)
        for event in pygame.event.get():
            # Если тип события нажатие на крестик
            if event.type == pygame.QUIT:
                # Заврешаем работу программы
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.CheckDown(event)
            elif event.type == pygame.KEYUP:
                self.CheckUp(event)
    def UpdateScreen(self):
        # Заполняем экран цветом используя объект settings
        self.screen.fill(self.settings.colour)

        # Отрисовка корабля
        self.ship.blitme()

        # Обновляем экран
        pygame.display.flip()

    def start(self):
        # Бесконечно делаем
        while True:
            self.CheckEvent()
            self.ship.Update()
            self.UpdateScreen()

if __name__ == '__main__':
    game = SpaceShip()
    game.start()