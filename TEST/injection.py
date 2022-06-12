class Sprite:
    def __init__(self, texture, health):
        self.texture = texture
        self.health = health
    def Damage(self):
        self.health -= 1

class Player(Sprite):
    def __init__(self, texture, health, nick):
        super().__init__(texture, health) # инициализация всех компонентов родителя
        self.nick = nick
    def Walk(self):
        print("Идет....")

player = Player("text.png", 349, "Lol")
player.Damage()
print(player.health)
player.Walk()