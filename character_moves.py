from pico2d import *

open_canvas()

boy = load_image('character.png')

def move_to(start_x, start_y, end_x, end_y):
    for i in range(20):
        t = i / 20
        x = start_x + (end_x - start_x) * t
        y = start_y + (end_y - start_y) * t
        draw_boy(x, y)

def move_top():
    print('Moving top')
    for x in range(50,751,5):
        draw_boy(x,550)
    pass


def move_right():
    print('Moving right')
    for y in range(550,49,-5):
        draw_boy(750,y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(750,49,-5):
        draw_boy(x,50)
    pass


def more_left():
    print('Moving left')
    for y in range(50,551,5):
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
    move_to(50, 50, 600, 300)
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
    print("Moving triangle bottom")
    for x in range(50, 401, 5):
        draw_boy(x, 50)

def move_triangle_right():
    print('Moving right')
    x1, y1 = 400, 50
    x2, y2 = 200, 350

    for i in range(60 + 1):
        t = i / 60
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)





def move_triangle_left():
    print('Moving_triangle_left')
    x1, y1 = 200, 350
    x2, y2 = 50, 50

    for i in range(60 + 1):
        t = i / 60
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)
    pass


def move_triangle():
    print("Moving triangle")
    move_to(50, 550, 50, 50)
    move_triangle_bottom()
    move_triangle_right()
    move_triangle_left()


while True:
   move_rectangle()
   move_triangle()
   move_circle()
   move_to(600, 300, 50, 550)



close_canvas()
