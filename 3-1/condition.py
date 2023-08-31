import datetime


num = int(input('정수 입력: ')) 
if num > 0:
        print('양수입니다')
elif num < 0:
        print('음수입니다')
else:
        print('0입니다')
        
    
num = int(input('정수 입력: '))
print('5의 배수입니다' if num % 5 == 0 else '5의 배수가 아닙니다')

now = datetime.datetime.now()
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

print('현재 시각은 {}시로 '.format(now.hour), end='')
if now.hour < 12:
    print('오전입니다.')
else:
    print('오후입니다')
    
