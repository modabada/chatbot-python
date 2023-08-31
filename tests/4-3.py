def splitter(title):
    print()
    l = len(title) + 4
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)
    
    
splitter('2')
k = ['name', 'hp', 'mp', 'level']
v = ['기사', 200, 30, 5]
c = dict()
for k_e, v_e in zip(k, v):
    c[k_e] = v_e
print(c) 


splitter('3')
lim = 10000
i = 1
t = 0
while t < lim:
    t += i
    i += 1
print('{}를 더할 때 {}을 넘으며 그때 {} 입니다'.format(i - 1, lim, t))


splitter('4')
m = 0
a = 0
b = 0
for x in range(51):
    y = 100 - x
    r = x * y
    if m < r:
        m = r
        a = x
        b = y
print('최대가 되는 경우: {} * {} = {}'.format(a, b, m))