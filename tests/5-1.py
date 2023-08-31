import re
def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('예제 1')
f1 = lambda x: 2 * x + 1
f2 = lambda x: (x ** 2) * 2 * x + 1
print(f1(10))
print(f2(10))


splitter('예제 2')
def mul(*v):
    s = 1
    for e in v:
        s *= e
    return s
print(mul(5, 7, 9, 10))
