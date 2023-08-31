PI = 3.1415926525

def nm_input():
    o = input('숫자 입력: ')
    return float(o)

def get_circumference(r):
    return 2 * PI * r

def get_circle_area(r):
    return PI * r ** 2
