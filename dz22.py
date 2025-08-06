class Tank:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def shoot(self, target):
        actual_damage = max(0, self.damage - target.armor)
        target.health -= actual_damage
        print(f"{self.name} стреляет в {target.name} и наносит {actual_damage} урона. У {target.name} осталось {target.health} здоровья.")

    def is_alive(self):
        if self.health > 0:
            print('танк жив')
if __name__ == '__main__':
    tank1 = Tank("Т-34", 100, 20, 10)
    tank2 = Tank("Тигр", 120, 25, 15)
    print(tank1.shoot(tank2))