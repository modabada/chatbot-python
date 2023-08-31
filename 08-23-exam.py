import random
import time

def splitter(title):
    print()
    l = len(title) + 4
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)

width = 10

splitter('삼각형')
for i in range(width):
    print('{}{}'.format(' ' * (width - i), '*' * (1 + 2 * i)))

splitter('다이아몬드')
for i in range(width):
    print('{}{}'.format(' ' * (width - i), '*' * (1 + 2 * i)))
for i in range(width + 1):
    print('{}{}'.format(' ' * i, '*' * (1 + 2 * (width - i))))
    
    
splitter('바람개비')
width = width * 2
star = width // 2 + 1
space = width // 2 - 1
left = 1
while space > 0:
    print('{}{}{}'.format('*' * left, ' ' * space, '*' * ((width //2)- left)))
    left += 1
    space -= 1
space = 0
left = width // 2 - 1
while space < (width // 2 - 1):
    # print(left,(width // 2 - left), space,  star - (width // 2 - left))
    print('{}{}{}{}'.format(' ' * left, '*' * (width // 2 - left), ' ' * space, '*' * (star - (width // 2 - left + 1))))
    space += 1
    left -= 1


splitter('금붕어')
g = {}
g['m'] = '나무'
g['f'] = '팔'
f = 2
t = 1
print('금붕어 수컷 애칭: {}'.format(g['m']))
print('금붕어 수컷 애칭: {}'.format(g['f']))

print('{:2} {:>6} {:>8} {:>8}'.format('턴', '초기값', '추가', '감소'))
while True:
    ad = 0
    minus = 0
    if f < 0:
        break
    if f > 1000:
        break
    p = f // 2
    ad = sum([random.randint(1, 10) for i in range(p)]) * 2
    if t >= 2:
        minus = sum([random.randint(1, 5) for i in range(p)]) * 2
    t += 1
    print('{:2d} {:>10d} {:>10d} {:>10d}'.format(t, f, ad, minus))
    f += ad - minus
if f < 0:
    print('물고기가 모두 죽었습니다...')
else:
    print('{}턴만에 {}마리가 되었습니다'.format(t, f))