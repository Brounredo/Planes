#coding=utf-8
import pyglet
import vars
import functions

window = pyglet.window.Window(800, 600, "Planes")
pyglet.gl.glClearColor(0, 0.75, 1, 1)
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

functions.init_planes()

@window.event
def on_draw():
    window.clear()
    vars.all_planes[vars.Cur_plane].sprite.draw()

@window.event
def on_key_press(symbol, modifiers):
    pass
    #if symbol == pyglet.window.key.Q:
    #    vars.all_planes[vars.Cur_plane].rotate(-1)
    #elif symbol == pyglet.window.key.A:
    #    vars.all_planes[vars.Cur_plane].rotate(1)

@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_UP:
        vars.all_planes[vars.Cur_plane].rotate(-1)
    elif motion == pyglet.window.key.MOTION_DOWN:
        vars.all_planes[vars.Cur_plane].rotate(1)

pyglet.app.run()