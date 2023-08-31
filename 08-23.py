import random

def splitter(title):
    print()
    l = len(title) + 4
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)
    
    

splitter('dictionary')
d = {
    'name': '8D 건조 망고',
    'type': '당절임',
    'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
    'origin': '필리핀',
}
print('name:', d['name'])
print('type:', d['type'])
print('ingredient:', d['ingredient'])
print('origin:', d['origin'])
d['name'] = '8D 건조 망고'
print('new name:', d['name'])


splitter('랜덤')
print('실수:', random.random())
print('정수범위:', random.randint(0, 2))


splitter('로또')
print('로또:', ', '.join([str(random.randint(1, 10) )for i in range(6)]))

splitter('입력받아 값 출력')
k = 'name' #input('키: ')
print(d[k] if k in d else '존재하지 않는 키에 접근하고 있습니다')


splitter('존재하지 않는 값 가져오기')
v = d.get('asfd')
print('값:', v)
if v == None:
    print('존재하지 않는 키에 접근했었습니다')
    
splitter('loop dictionary')
for k in d:
    print(k, ':', d[k])


splitter('range 객체')
ar = [273, 32, 103, 57, 52]
for i in range(len(ar)):
    print(f'{i}번째 반복: {ar[i]}')
    
    
splitter('continue')
ar = [5, 15, 6, 20, 7, 25]
for n in ar:
    if n < 10:
        continue
    print(n)


splitter('iterable method')
ls = ['a', 'b', 'c']
print('normal:\t\t\t', ls)
print('enumerate:\t\t', enumerate(ls))
print('list(enumerate(ls)):\t', list(enumerate(ls)))
print('with loop:')
for i, v in enumerate(ls):
    print(f'\t{i} 번째 요소는 {v} 입니다')


splitter('dictionalry.items')
d = {
    'ka': 'va',
    'kb': 'vb',
    'kc': 'vc',
    'kd': 'vd'
}
print(d.items())
print('with for:')
for k, v in d.items():
    print(f'\t{k} : {v}')
    

splitter('include other list')
ls = []
for i in range(0, 20, 2):
    ls.append(i * i)
print(ls)


splitter('include other list with condition')
ls = ['사과', '자두', '초콜릿', '바나나', '체리']
o = [f for f in ls if f != '초콜릿']
print(o)


splitter('reversed')
n = [1, 2, 3, 4, 5]
rn = reversed(n)
print(rn)
print(next(rn))
print(next(rn))
print(next(rn))
print(next(rn))
print(next(rn))

