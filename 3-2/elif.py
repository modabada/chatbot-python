import datetime


num = int(input('정수 입력: '))
print('짝' if num % 2 == 0 else '홀', '수입니다', sep='')

money = int(input('돈을 입력: '))
if money >= 5000:
    print('택시를 타고 간다')
elif money >= 2000:
    print('버스를 타고 간다')
else:
    print('걸어간다')


grade = int(input('성적입력: '))
if grade >= 90:
    print('아이패드')
elif grade >= 80:
    print('워치')
elif grade >= 70:
    print('아무일도 없었다')
elif grade > 60:
    print('용돈 차감')
else:
    print('외출금지') 