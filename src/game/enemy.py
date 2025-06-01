class Enemy:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    def move(self):
        # Logic for enemy movement
        pass

    def attack(self, player):
        # Logic for attacking the player
        player.health -= self.damage

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Logic for enemy death
        pass

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Damage: {self.damage}, Speed: {self.speed})"