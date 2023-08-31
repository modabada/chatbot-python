

def splitter(title):
    print('\n')
    l = len(title) + 4
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)
    

splitter('remove list element')
ls = [0, 1, 2, 3, 4, 5]
print('# 리스트의 요소 하나 제거하기')
del ls[1]
print('del ls[1]: ', ls)
ls.pop(2)
print('pop(2): ', ls)


splitter('for문')
ls = [273, 32, 103, 57, 52]

for e in ls:
    print(e)
    

splitter('연습문제')
ls = range(1, 10)
o = [[] for i in range(3)]

for n in ls:
    o[n % 3 - 1].append(n)
print(o)

splitter('range')
a = range(1, 10)
s = 0
for i in a:
    s += i
print(a, '의 합은', s, '입니다')


splitter('for 구구단')
for y in range(1, 10):
    for x in range(2, 10):
        print('{} * {} = {:>2d}'.format(x, y, x * y), end = '\t')
    print()


splitter('for append & list comprehension')
a = [1, 2, 3, 4]
result = []

for n in a:
    result.append(n * 3)
print(result)

result = [n * 3 for n in a]
print(result)


splitter('dictionary')
d = {
    'name': '어벤저스 엔드게임',
    'type': '히어로 무비'
}

print(d)
print('name: ', d['name'])
print('type: ' ,d['type'])

d = {
    'director': ['안소니 루소', '조 루소'],
    'cast': ['아이언맨', '타노스', '토르', '닥터스트레인지', '헐크']
}
print('director: ', d['director'])
print('cast: ', d['cast'])
