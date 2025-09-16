from pico2d import *
import math

# 화면 초기화
open_canvas()

# 리소스 로드
character = load_image('character.png')
grass = load_image('grass.png')

# 화면 크기 설정
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def draw_background():
    """배경(잔디) 그리기"""
    grass.draw(CANVAS_WIDTH // 2, 30)


def check_quit() -> bool:
    """창 닫기 또는 ESC 입력 시 True 반환"""
    for e in get_events():
        if e.type == SDL_QUIT:
            return True
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            return True
    return False


def draw_character(x, y) -> bool:
    """캐릭터 그리기. 종료 요청 시 False 반환"""
    clear_canvas()
    draw_background()
    character.draw(x, y)
    update_canvas()
    delay(0.02)
    return not check_quit()


def move_rectangle() -> bool:
    """사각형 운동 - 화면 테두리를 따라 시계방향으로 이동. 중간 종료 시 False"""
    # 1. 위쪽 가장자리 - 왼쪽에서 오른쪽으로
    for x in range(50, CANVAS_WIDTH - 50, 5):
        if not draw_character(x, CANVAS_HEIGHT - 50):
            return False

    # 2. 오른쪽 가장자리 - 위에서 아래로
    for y in range(CANVAS_HEIGHT - 50, 100, -5):
        if not draw_character(CANVAS_WIDTH - 50, y):
            return False

    # 3. 아래쪽 가장자리 - 오른쪽에서 왼쪽으로
    for x in range(CANVAS_WIDTH - 50, 50, -5):
        if not draw_character(x, 100):
            return False

    # 4. 왼쪽 가장자리 - 아래에서 위로
    for y in range(100, CANVAS_HEIGHT - 50, 5):
        if not draw_character(50, y):
            return False

    return True


def move_circle() -> bool:
    """원 운동 - 화면 중앙에서 원형으로 이동. 중간 종료 시 False"""
    center_x = CANVAS_WIDTH // 2
    center_y = CANVAS_HEIGHT // 2
    radius = 200

    for degree in range(0, 360, 3):
        radian = math.radians(degree)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
        if not draw_character(x, y):
            return False

    return True


def main():
    """메인 실행 함수 - 사각형과 원 운동을 번갈아 무한 반복, 종료 입력 시 탈출"""
    try:
        while True:
            if not move_rectangle():
                break
            if not move_circle():
                break
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
