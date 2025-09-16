from pico2d import *
import math

open_canvas()

boy = load_image('character.png')

# 현재 위치를 추적하여 동작 간 점프를 방지
CUR_X, CUR_Y = 100.0, 100.0

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def draw_step(x: float, y: float):
    global CUR_X, CUR_Y
    draw_boy(x, y)
    CUR_X, CUR_Y = x, y

def move_to(x: float, y: float, steps: int = None):
    global CUR_X, CUR_Y
    sx, sy = CUR_X, CUR_Y
    dx, dy = x - sx, y - sy
    dist = math.hypot(dx, dy)
    n = steps if steps is not None else max(int(dist / 5), 1)
    for i in range(1, n + 1):
        t = i / n
        draw_step(sx + dx * t, sy + dy * t)

# 선분 (x1,y1) -> (x2,y2) 를 일정 픽셀 간격으로 이동
def move_line(x1: float, y1: float, x2: float, y2: float, pixel_step: float = 5.0):
    # 시작점까지 매끄럽게 이동 후, 선을 따라 진행
    move_to(x1, y1)
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    steps = max(int(dist / pixel_step), 1)
    for i in range(1, steps + 1):
        t = i / steps
        draw_step(x1 + dx * t, y1 + dy * t)

# 사각형 경로: (100,100) -> (700,100) -> (700,500) -> (100,500) -> (100,100)
def move_top():
    move_line(100, 100, 700, 100)

def move_right():
    move_line(700, 100, 700, 500)

def move_bottom():
    move_line(700, 500, 100, 500)

def move_left():
    move_line(100, 500, 100, 100)

def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()  # 끝나면 (100,100)에 복귀

# 삼각형 경로: A(100,100) -> B(400,400) -> C(700,100) -> A(100,100)
def move_triangle():
    print("Moving triangle")
    A = (100, 100)
    B = (400, 400)
    C = (700, 100)
    move_line(*A, *B)
    move_line(*B, *C)
    move_line(*C, *A)  # 끝나면 (100,100)

# 원 경로: 중심(400,300), 반지름 150
def move_circle():
    print("Moving circle")
    r = 150
    center_x = 400
    center_y = 300

    # 삼각형의 마지막 위치에서 시작하여 원의 시작점으로 이동
    # 원 위의 가장 가까운 점을 시작점으로 계산
    dx = CUR_X - center_x
    dy = CUR_Y - center_y
    start_angle = math.atan2(dy, dx)

    # 시작점 좌표
    start_x = r * math.cos(start_angle) + center_x
    start_y = r * math.sin(start_angle) + center_y

    # 현재 위치에서 원의 시작점까지 연결 이동
    move_to(start_x, start_y)

    # 원을 한 바퀴 돌기
    angle_step = math.radians(5)  # 5도씩
    for i in range(72):  # 360도를 5도씩 나누면 72개
        angle = start_angle + (i * angle_step)
        x = r * math.cos(angle) + center_x
        y = r * math.sin(angle) + center_y
        draw_step(x, y)

    # 마지막에 (100,100)으로 정확히 이동하여 다음 사각형 시작 준비
    move_to(100, 100)

while True:
    # 도형 간 연결 이동을 포함해 부드럽게 무한 반복
    move_rectangle()
    move_triangle()
    move_circle()

# close_canvas()
