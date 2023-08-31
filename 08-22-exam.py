
def splitter(title):
    print('\n')
    l = len(title) + 4
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)
    

splitter('1~10 출력(2)')
i = 1
while True:
    if i > 10:
        break
    print(i)
    i += 1


splitter('1~10 출력(2)')
print("\n".join([str(n) for n in range(1, 11)]))


splitter('10~1 출력')
print("\n".join([str(n) for n in range(10, 0, -1)]))


splitter('1~100까지 합')
print('1부터 100까지의 합은 ', sum(range(1, 101)), '입니다')

splitter('1~100 중 짝수의 합')
print('1~100까지 수중 짝수의 합은', sum(range(2, 101, 2)), '입니다')

splitter('1, -2, 3, -4... 99, -100 합 구하기')
print('합:', sum([n * -1 if n % 2 == 0 else 1 for n in range(1, 101)]))

splitter('계승 구하기')
f = 1
for n in range(1, 6):
    f *= n
print('계승:', f)


splitter('약수 구하기')
n = int(input("n 입력: "))
print(', '.join([str(i) for i in range(2, int((n + 1) / 2 + 1)) if n % i == 0]))


splitter('구구단')
for y in range(1, 10):
    for x in range(2, 10):
        print('{} * {} = {:>2d}'.format(x, y, x * y), end = '\t')
    print()