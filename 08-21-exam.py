def splitter(num):
    print('=' * 20)
    print()
    print(num, '번')
    
# 예제 10
splitter(10)
a, b, c = map(int, input('[3수중 가장 큰수] a, b, c 입력: ').split(', '))
if a > b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)
print('가장 큰 수:', max(a, b, c))

splitter(11)
m = int(input('[3수중 가장 큰수(2)] max 입력: '))
a = int(input('a 입력: '))
if a > m: m = a
a = int(input('a 입력: '))
if a > m: m = a
print(m)