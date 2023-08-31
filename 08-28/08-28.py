import re
from math import sin, cos, tan, floor, ceil

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('yield 키워드')
def t():
    print('A 지점 통과')
    yield 1
    print('B 지점 통과')
    yield 2
    print('C 지점 통과')
o = t()
print('D 지점 통과')
a = next(o)
print('E 지점 통과')
b = next(o)
print('F 지점 통과')
# c = next(o)
print(a)
print(b)
# print(c)


splitter('예외처리')
i = input('정수 입력: ')
if i.isdigit():
    int_i = int(i)
    print('원의 반지름:', int_i)
    print('원의 둘레', 2 * 3.14 * int_i)
    print('원의 넓이:', 3.14 * int_i ** 2)
else:
    print('정수를 입력하지 않았습니다')


splitter('try-catch')
i = input('정수 입력: ')
try:
    int_i = int(i)
    print('원의 반지름:', int_i)
    print('원의 둘레', 2 * 3.14 * int_i)
    print('원의 넓이:', 3.14 * int_i ** 2)
except:
    print('알 수 없는 오류가 발생했습니다')


splitter('')
ls = ['12', '34', '45', '스파이', '56']
rs = []
for i in ls:
    try:
        float(i)
        rs.append(i)
    except:
        pass
print('전:', ls)
print('후:', rs)


splitter('try-except-else')
n_i = 0
try:
    n_i = int(input('정수 입력: '))
except:
    print('정수를 입력하지 않았습니다')
else:
    print('원의 반지름:', n_i)
    print('원의 둘레:', 2 * 3.14 * n_i)
    print('원의 넓이:', 3.14 * n_i ** 2)


splitter('try-except-else-finally')
try:
    n_i = int(input('정수 입력: '))
    print('원의 반지름:', n_i)
    print('원의 둘레:', 2 * 3.14 * n_i)
    print('원의 넓이:', 3.14 * n_i ** 2)
except:
    print('정수를 입력하지 않았습니다')
else:
    print('예외가 발생하지 않았습니ㅏㄷ')
finally:
    print('프로그램이 종료되었습니다')


print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))