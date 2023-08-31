import re

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)



splitter('2번')
ls = [52, 273, 32, 103, 90, 10, 275]
print('요소 내부에 있는 값 찾기')
print('- {}는 {} 위치에 있습니다'.format(52, ls.index(52)))
print()
print('요소 내부에 없는 값 찾기')
n = 10000
try:
    print('- {} 는 {} 위치에 있습니다'.format(n, ls.index(n)))
except:
    print('- 리스트 내부에 없는 값입니다')
print()
print('--- 정상적으로 종료되었습니다 ---')


splitter('throw')
n = input('정수 입력: ')
n = int(n)
if n > 10:
    raise NotImplementedError
else:
    raise NotImplementedError