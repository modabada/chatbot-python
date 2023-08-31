import turtle
import os
import random
import re

def splitter(title):
    turtle.bgcolor('black')
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)

def turtles():
    splitter('거북이')
    turtle.shape('turtle')
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)

    splitter('반복')
    turtle.shape('turtle')
    angle = 89
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.speed(0)
    for x in range(200):
        turtle.forward(x)
        turtle.left(89)
        

    splitter('오각형')
    n = 5
    turtle.color('purple')
    turtle.begin_fill()

    for x in range(n):
        turtle.forward(50)
        turtle.left(360 / n)
    turtle.end_fill()
    turtle.hideturtle


    splitter('원')
    turtle.circle(50)
    turtle.color('red')
    turtle.pensize(3)


    for i in range(12):
        turtle.color(random.random(), random.random(), random.random())
        turtle.circle(50)
        turtle.left(30)

def facto(n):
    return 1 if n == 0 else n * facto(n - 1)


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

d = {
    1: 1,
    2: 1
}
def  fibo2(n):
    if n not in d:
        d[n] = fibo2(n - 1) + fibo2(n - 2)
    return d[n]

splitter('재귀함수')
print(facto(1))
print(facto(2))
print(facto(3))
print(facto(4))
print(facto(5))


splitter('재귀함수를 이용한 피보나치')
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))


splitter('계산한 값을 저장하여 연산량 최적화')
print(fibo(10))
print(fibo(20))
print(fibo(30))
print(fibo(35))