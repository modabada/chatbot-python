score = 400  # 변수 선언
print(score + 200) # print 함수를 이용해 출력
print(score - 100)
print(score * 2)
print(score / 4)
print(score ** 3)
print(score % 9)

pi = 3.1415926535
r = 10
print("원주율:\t", pi)
print("반지름:\t", r)
print('둘래:\t', 2 * pi * r)
print('넓이:\t', r * r * pi)


print('\t\t\t성적표\t\t\t')
print('-' * 75)
sc = [
    ['강용우', 100, 100, 100, 98],
    ['김유준', 100, 100, 100, 98],
    ['문인우', 100, 100, 100, 99],
    ['박형진', 100, 100, 100, 97]
]
for p in sc:
    print("\t".join(map(str, p)), '\t', sum(p[1:]) / 4)

name_1 = "강용우"
name_2 = "김유준"
name_3 = "문인우"
name_4 = "박형진"

score_korean1 = 90
score_korean2 = 80
score_korean3 = 70
score_korean4 = 80

score_math1 = 90
score_math2 = 60
score_math3 = 70
score_math4 = 80

score_eng1 = 70
score_eng2 = 90
score_eng3 = 80
score_eng4 = 60

score_pyth1 = 80
score_pyth2 = 60
score_pyth3 = 70
score_pyth4 = 90

print("\t\t\t성적표\t\t\t")
print("-----" *15)
print("이름\t국어\t수학\t영어\t파이썬")
print(name_1,"\t",score_korean1, '\t', score_math1,'\t',  score_eng1,'\t',  score_pyth1, '\t', (score_korean1 + score_math1 + score_eng1 + score_pyth1) / 4)
print(name_2,"\t",score_korean2, '\t', score_math2,'\t',  score_eng2,'\t',  score_pyth2, '\t', (score_korean2 + score_math2 + score_eng2 + score_pyth2) / 4)
print(name_3,"\t",score_korean3, '\t', score_math3,'\t',  score_eng3,'\t',  score_pyth3, '\t', (score_korean3 + score_math3 + score_eng3 + score_pyth3) / 4)
print(name_4,"\t",score_korean4, '\t', score_math4,'\t',  score_eng4,'\t',  score_pyth4, '\t', (score_korean4 + score_math4 + score_eng4 + score_pyth4) / 4)


numbers = 100
numbers += 10
numbers += 20
numbers += 30
numbers += 40
print('numbers:', numbers)



# 입력
print('\n\n\n\n\n')


inp = input("인삿말을 밉력하세요:")
print(type(inp))
print(inp * 3)


x, y = map(int, input("input x, y: ").split(','))
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)



st_1 = input('학생이름, 국어성적, 수학성적, 영어성적, 파이썬성적 순으로 입력: ').split(',')
st_2 = input('학생이름, 국어성적, 수학성적, 영어성적, 파이썬성적 순으로 입력: ').split(',')
st_3 = input('학생이름, 국어성적, 수학성적, 영어성적, 파이썬성적 순으로 입력: ').split(',')
st_4 = input('학생이름, 국어성적, 수학성적, 영어성적, 파이썬성적 순으로 입력: ').split(',')

print("\t\t\t성적표\t\t\t")
print("-----" *15)
print("이름\t국어\t수학\t영어\t파이썬\t평균")
print("\t".join(st_1), '\t', sum(map(int, st_1[1:])) / 4)
print("\t".join(st_2), '\t', sum(map(int, st_2[1:])) / 4)
print("\t".join(st_3), '\t', sum(map(int, st_3[1:])) / 4)
print("\t".join(st_4), '\t', sum(map(int, st_4[1:])) / 4)