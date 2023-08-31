import random
import re

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('def')
def print_3_times():
    print('hi!')
    print('hi!')
    print('hi!')
print_3_times()


splitter('매개변수가 있는 함수')
def print_n_times(v, n):
    for _ in range(n):
        print(v)
print_n_times('안녕하세요', 5)


splitter('가변 매개변수')
def print_n_times(n, *v):
    for _ in range(n):
        for e in v:
            print(e)
        print()
print_n_times(3, 'hi', 'hello', 'bye')


splitter('기본 매개변수')
def print_n_times(v, n=2):
    for _ in range(n):
        print(v)
print_n_times('hi hello')


splitter('named parameter')
def print_n_times(*v, n=2):
    for _ in range(n):
        for e in v:
            print(e)
        print()
print_n_times('hi hello')


splitter('리턴')
def return_test():
    return 100
print(return_test())


splitter('매개변수와 리턴')
def sum_all(end, start=0):
    return sum([i for i in range(start, end + 1)])
print('0 to 100')
print(sum_all(0, 100))
print(sum_all(100, 1000))


splitter('파일 시스템')
file = open('basic.txt', 'w')
file.write('Hello programming')
file.close()


splitter('파일시스템 with keyword')
with open('basic.txt', 'r') as file:
    print(file.read())


splitter('랜덤하게 1000명 키몸무게')
h = list('가나다라마바사아자차카타파하')
with open('info.txt', 'w', encoding='UTF-16') as file:
    for i in range(1000):
        name = random.choice(h) + random.choice(h)
        weight = random.randint(40, 100)
        height =  random.randint(140, 200)
        
        file.write('{}, {}, {}\n'.format(name, weight, height))
print('파일 생성 완료')

with open('info.txt', 'r', encoding='UTF16') as file:
    for l in file:
        name, weight, height = l.strip().split(', ')
        
        
        if (not name) or (not weight) or (not height):
            print('error data found:', name, weight, height)
            continue
        
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ''
        if 18.5 > bmi:
            result = '저체중'
        elif 25 > bmi:
            result = '정상 체중'
        else:
            result = '과체중'
            
            print('\n'.join([
                '이름: {}',
                '몸무게: {}',
                '키: {}',
                'BMI: {}',
                '결과: {}'
            ]).format(name, weight, height, bmi, result))
            print()