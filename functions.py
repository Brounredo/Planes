#coding=utf-8
import vars
import plane
import pyglet


# Инициализация самолётов
def init_planes():
    # Американский истребитель
    vars.all_planes.append(plane.Plane("USA", 100, 2, 50, pyglet.image.load("Images/Planes/USA.png")))