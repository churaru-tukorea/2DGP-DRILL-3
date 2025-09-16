from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 800, 5):
        draw_boy(x, 550)


def move_right():
    print('Moving right')
    for y in range(550, 50, -5):
        draw_boy(800, y)


def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -5):
        draw_boy(x, 50)


def move_left():
    print('Moving left')
    for y in range(50, 550, 5):
        draw_boy(0, y)


def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_circle():
    print("Moving circle")
    r = 200
    center_x = 400
    center_y = 300

    for deg in range(0, 360, 5):
        x = r * math.cos(math.radians(deg)) + center_x
        y = r * math.sin(math.radians(deg)) + center_y
        draw_boy(x, y)


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_rectangle()
    move_circle()
    break


close_canvas()
