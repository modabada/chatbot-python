"{}".format(10)
"{} {}".format(10, 20)
"{} {} {} {} {}".format(101, 202, 303, 404, 505)



format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(300, 400, 500)
format_d = "{} {} {}".format(1, '문자열', True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)

print("기본")
print("{:d}".format(52))
print('특정 칸에 출력하기')
print('{:5d}'.format(64))
print('{:10d}'.format(52))
print('빈칸을 0으로 채우기')
print('{:05d}'.format(52))
print('{:05d}'.format(-52))


print("{:f}".format(52.273))
print("{:15f}".format(52.273))
print("{:+15f}".format(52.273))
print("{:+015f}".format(52.273))
print("{:+015f}".format(0.1))
print("{:+015f}".format(0.2))


a = "Hello Python Programing...!"
print(a.upper())
print(a.lower())


input_a = """
        안녕하세요
문자열의 함수를 알아봅니다
        """
print(input_a.strip())


print("안녕안녕하세요".find("안녕"))
print("안녕안녕하세요".rfind("안녕"))


print("안녕" in '안녕하세요')

print("10, 20, 30, 40, 50, 60".split(', '))


print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

print('가방' == '가방')
print('가방' != '하마')
print('가방' < '하마')
print('가방' > '하마')

