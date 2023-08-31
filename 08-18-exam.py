def splitter(num):
    print('=' * 20)
    print()
    print(num, '번')
    
    
splitter(1)
a, b = map(int, input('[대소비교] a, b 입력: ').split(','))
print(a if a > b else b)

splitter(2)
a = int(input('[음수, 양수] a 입력: '))
if a > 0:
    print('양수')
elif a < 0:
    print('음수')
else:
    print('0')
    
    
splitter(3)
a = int(input('[3의배수] a 입력: '))
print('3의 배수', '아님' if a % 3 != 0 else '')


splitter(4)
price = 5000
age = int(input('[입장료] age 입력: '))
if age < 8:
    print(price * 0, '원')
elif age < 60:
    print(price, '원')
else:
    print(price * 0.5, '원')
    

splitter(5)
a = int(input('[3과5의배수] a 입력: '))
print('3과 5의 배수', '아님' if a % 3 != 0 or a % 5 != 0 else '')


splitter(6)
age = int(input('[입장료2] age 입력: '))
print('무료' if age < 8 or age >= 60 else price)