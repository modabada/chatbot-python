import time

def splitter(title):
    print('\n')
    print('-' * 10)
    print(title)
    print('-' * 10)


splitter('학점계산기')
# 변수 선언
score = float(input('학점 입력: '))

# 조건문 적용
if score == 4.5:
    print('신')
elif 4.2 <= score:
    print('교수님의 사랑')
elif 3.5 <= score:
    print('현 체제의 수호자')
elif 2.8 <= score:
    print('일반인')
elif 2.3 <= score:
    print('일탈을 꿈꾸는 소시만')
elif 1.75 <= score:
    print('오락문화의 선구자')
elif 1.0 <= score:
    print('불가촉천민')
elif 0.5 <= score:
    print('자벌레')
elif 0 < score:
    print('플랑크톤')
else:
    print('시대를 앞서가는 혁명의 씨앗')
    
    
splitter('자판기')
menu = {
    '코카콜라': 1000,
    '사이다': 800,
    '환타': 900,
    '밀키스': 700,
    '솔의눈': 600,
    '삼다수': 500
}
menu = list(menu.items())
money = int(input('돈을 입력: '))
m = sorted(menu, key=lambda x: x[1])[0][1]
if money < m:
    print('입력한 돈', money, '원이 최소 주문 가능금액', m, '원 보다 낮습니다')
else:
    i = 1
    for k, v in menu:
        print('{:2d} {:10}:{:>10d}'.format(i, k, v))
        i += 1
    sel = int(input('메뉴를 선택하세요: ')) - 1
    price = menu[sel][1]
    if money < price:
        print('주문금액', price, '원 보다 잔돈이 적습니다')
    else:
        print(menu[sel][0], '를 선택하셨습니다. 잔돈:', money - menu[sel][1], '원')
        
splitter('pass 키워드')
number = int(input('정수 입력: '))

if number > 0:
    print('')
else:
    pass


splitter('리스트')
ls = [273, 32,103, '문자열', True, False]
print(ls[0])
print(ls[3][0])
ls = [[1,2,3], [4,5,6], [7,8,9]]
print(ls[1])
print(ls[1][1])
print(ls[2][1])


splitter('리스트 연산')
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]

print("# 리스트")
print('ls1 =', ls1)
print('ls2 =', ls2)
print()

print('# 리스트 기본 연산자')
print('ls1 + ls2 =', ls1 + ls2)
print('ls1 * 3 =', ls1 * 3)
print()

print('# 길이 구하기')
print('len(ls1) =', len(ls1))
print()


splitter('리스트 연장')
ls = [1, 2, 3]
print('리스트 뒤에 요소 추가')
ls.append(4)
ls.append(5)
print(ls)
print('리스트 중간에 요소 추가')
ls.insert(0, 10)
print(ls)


splitter('while 문')
hit = 0
while hit < 10:
    hit += 1
    print('나무를 %d번 찍었습니다' % hit)
print('나무 넘어갑니다.')


splitter('prompt')
prompt = """
1. Add    |
2. Del    |
3. List   |
4. Quit   |
Enter number: """

i = 0
while i != 4:
    print(prompt, end='')
    i = int(input())

splitter('커피 자판기')
coffee = 10
money = 300
while True:
    break
    if not coffee:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다')
        break
    money = int(input('돈을 입력: '))
    if money < 300:
        print('돈이 부족합니다')
        continue
    if money > 300:
        print(f'거스름돈 {money - 300}원을 주고 ', end='')
    print('커피를 줍니다')
    coffee -= 1
    

splitter('구구단')
d = int(input('몇 단을 출력할까요: '))
y = 1
while y < 10:
    print(d, '*', y, '=', d * y)
    y += 1
    

splitter('별찍기')
c = 1
while c < 11:
    print('*' * c)
    c += 1
    

splitter('시간을 기반으로 반복')
print(time.time())
n = 0
t = time.time() + 5
while time.time() < t:
    break
    print(n)
    n += 1
    

splitter('반복문 사용자 중지')
l = 0
while True:
    print(l, '번째 반복입니다')
    t = input('종료하시겠습니까?(y/n): ')
    if t in ['y', 'Y']:
        print('종료합니다')
        break
    l += 1


splitter('반대 별')
c = 1
f = 1
while True:
    print('*' * c)
    c += f
    if c == 10:
        f = -1
    if c == 0:
        break

i , j = 0, 0
while i < 10:
    j = 0
    print('i =', i)
    while j < 10:
        print('j =', j, '\t', end='')
        j += 1
    print()
    i += 1
    
    
    
splitter('구구단')
y = 2
while y < 10:
    x = 2
    while x < 10:
        print(x, '*', y, '=', y * x, '\t', end='')
        x += 1
    print()
    y += 1