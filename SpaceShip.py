import sys  # библиотека для взаимодействия с операционной системой
import pygame
from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from meteorit import Meteorit

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
        # Контейнер пуль (спрайтов)
        self.bullets = pygame.sprite.Group()

        # Контейнер врагов
        self.enemies = pygame.sprite.Group()
        #self.EnemiesCreate()
        self.EnemiesFleetCreate()

    def EnemiesCreate(self,i, j):
        enemy = Meteorit(self)
        alienWidth = enemy.rect.width
        allienHeight = enemy.rect.height
        enemy.x = alienWidth + 2 * alienWidth * i
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2*enemy.rect.height*j
        self.enemies.add(enemy)

    def EnemiesFleetCreate(self):
        enemy = Meteorit(self)

        # Получаем высоту и ширину врага для подсчетов
        alienWidth = enemy.rect.width
        alienHeight = enemy.rect.height

        # Допустимое значение спавна в ряд  пришельцев (в пикселях)
        space = self.screen.get_width() - 2 * alienWidth
        # Допстимое значение спавна в высоту пришельцев (в пикселях)
        spaceY = self.screen.get_height() - self.ship.rect.height - 2 * alienHeight

        # Кол-во врагшов в ряду
        n = space // (2 * alienWidth)

        # кол-во рядов
        m = spaceY // (2 * alienHeight)

        for j in range(m):
            for i in range(n + 1):
                self.EnemiesCreate(i, j)


    def Fire(self):
        bullet = Bullet(self.screen, self.settings, self.ship)
        self.bullets.add(bullet)

    def FireMega(self):
        if len(self.bullets) < self.settings.MegaFireCount:
            bullet = Bullet(self.screen, self.settings, self.ship)
            bullet.rect.width = 200
            bullet.rect.height = 5
            bullet.rect.midbottom = self.ship.rect.midbottom
            bullet.bulletSpeed = 1.5
            self.bullets.add(bullet)

    def FireMultiple(self, n):
        left = 5
        right = 0
        for i in range(0, n):
            bullet = Bullet(self.screen, self.settings, self.ship)

            if i % 2 == 0:
                bullet.rect.x += right
                right += 5
            else:
                bullet.rect.x -= left
                left += 5

            self.bullets.add(bullet)

    def FireSpread(self):
        bulletCenter = Bullet(self.screen, self.settings, self.ship)
        bulletRight = Bullet(self.screen, self.settings, self.ship, "right")
        bulletLeft = Bullet(self.screen, self.settings, self.ship, "left")

        self.bullets.add(bulletCenter)
        self.bullets.add(bulletRight)
        self.bullets.add(bulletLeft)



    def CheckDown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.isRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.isLeft = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_KP_ENTER:
            self.Fire()
        elif event.key == pygame.K_KP0:
            self.FireMultiple(11)
        elif event.key == pygame.K_KP1:
            self.FireSpread()
        elif event.key == pygame.K_SPACE:
            self.FireMega()
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

        # отрисовка пуль
        for bullet in self.bullets.sprites():
            bullet.blitme()

        # отрисовка врагов
        self.enemies.draw(self.screen)

        # Обновляем экран
        pygame.display.flip()

    def start(self):
        # Бесконечно делаем
        while True:
            self.enemies.update()
            for en in self.enemies.sprites():
                if en.checkEdges():
                    self.settings.fleet_direction *= -1

            self.CheckEvent()
            self.ship.Update()
            # Вызываем метод update у группы спрайтов
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self.UpdateScreen()

if __name__ == '__main__':
    game = SpaceShip()
    game.start()