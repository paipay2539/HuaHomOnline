class Player:
    def __init__(self, name, health=100, position=(0, 0)):
        self.name = name
        self.health = health
        self.position = position

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Player(name={self.name}, health={self.health}, position={self.position})"