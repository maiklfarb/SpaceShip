class Settings:
    def __init__(self):
        # Параметры экрана
        self.scrinWidth = 1200
        self.scrinHeight = 700
        self.colour = (48,169,225)

        # Параметры корабля
        self.speed = 2.7

        # Параметры снаряда
        self.bullet_speed = 3.0
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_colour = (128,102,18)

        # Кол-во разрешенных пуль на экране для megafire
        self.MegaFireCount = 1

        # параметры врагов
        self.enemy_speed = 2.0
        self.enemy_drop_speed = 10
        self.fleet_direction = 1 # 1 - флот вправо, -1 - флот влево