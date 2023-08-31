import re

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('문제 1')
s_min = 2
s_max = 10
total = 100

memory = {}

def solution(remain, sitting):
    key = str([remain, sitting])
    
    if key in memory:
        return memory[key]
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    
    t = 0
    for s in range(sitting, s_max + 1):
        t += solution(remain - s, s)
    memory[key] = t
    return t

print(solution(6, 2))
print(solution(total, s_min))