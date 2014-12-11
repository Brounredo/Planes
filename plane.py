#coding=utf-8
import pyglet


# Класс самолёта
class Plane:
    name = ""       # Название
    hp = 50         # "Здоровье"
    armor = 2       # Защита
    fuel = 50       # Топливо
    image = None    # Изображение
    sprite = None   # Спрайт
    x = 0           # Координата X (относительно экрана)
    y = 0           # Координата Y (относительно экрана)
    height = 0      # Высота (относительно земли)
    distance = 0    # Пройденный путь (относительно земли)
    angle = 0       # Угол к горизонту

    # Инициализация
    def __init__(self, name, hp, armor, fuel, image):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.fuel = fuel
        self.image = image
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.x, y=self.y)

    # Уменьшение топлива (частота 1 Гц)
    def fuel_decrease(self):
        self.fuel -= 1

    # Поворот самолёта и его спрайта
    def rotate(self, a):
        self.angle += a
        self.sprite.rotation = self.angle