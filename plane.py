#coding=utf-8


# Класс самолёта
class Plane:
    name = ""       # Название
    hp = 50         # "Здоровье"
    armor = 2       # Защита
    fuel = 50       # Топливо
    image = None    # Изображение

    # Инициализация
    def __init__(self, name, hp, armor, fuel):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.fuel = fuel

    # Уменьшение топлива (частота 1 Гц)
    def fuel_decrease(self):
        self.fuel -= 1