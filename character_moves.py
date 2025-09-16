from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0,750,5):
        draw_boy(x,550)
    pass


def move_right():
    print('Moving right')
    for y in range(550,0,-5):
        draw_boy(750,y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(750,0,-5):
        draw_boy(x,50)
    pass


def more_left():
    print('Moving left')
    for y in range(0,550,5):
        draw_boy(50,y)
    pass


def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    more_left()
    pass


def move_circle():
    print("Moving circle")

    r = 200

    for deg in range(0,360):
        x = r*math.cos(math.radians(deg))+400
        y = r*math.sin(math.radians(deg))+300
        draw_boy(x, y)

    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


def move_triangle_bottom():
    pass


def move_triangle_right():
    pass


def move_triangle_left():
    pass


def move_triangle():
    print("Moving triangle")
    move_triangle_bottom()
    move_triangle_right()
    move_triangle_left()


while True:
    move_rectangle()
    move_circle()
    move_triangle()

    break
    pass


close_canvas()
