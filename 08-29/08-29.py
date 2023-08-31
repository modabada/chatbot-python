import re
from bs4 import BeautifulSoup
from urllib import request
from flask import Flask

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('기상청 크롤링')
target = request.urlopen('https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
soup = BeautifulSoup(target, "html.parser")
for location in soup.select('location'):
    print('도시:', location.select_one('city').string)
    print('날씨:', location.select_one('wf').string)
    print('최저기온:', location.select_one('tmn').string)
    print('최고기온:', location.select_one('tmx').string)
    print()


splitter('클래스 전')
stud = [
    {'name': '가나다', 'korean': 90, 'math': 79, 'science': 92, 'music': 74},
    {'name': '가나라', 'korean': 94, 'math': 78, 'science': 94, 'music': 76},
    {'name': '가나마', 'korean': 93, 'math': 77, 'science': 96, 'music': 77},
    {'name': '가나바', 'korean': 92, 'math': 76, 'science': 97, 'music': 75},
    {'name': '가나사', 'korean': 91, 'math': 74, 'science': 98, 'music': 73},
    {'name': '가나아', 'korean': 99, 'math': 75, 'science': 99, 'music': 71},
]
print('이름', '총점', '평균', sep='\t')
for s in stud:
    t = sum([s['korean'], s['math'], s['science'], s['music']])
    v = t / 4
    print(s['name'], t, v, sep='\t')


splitter('클래스 후')
class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_avg(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )
s_ls = [
    student('가나다', 90, 79, 92, 74),
    student('가나라', 94, 78, 94, 76),
    student('가나마', 93, 77, 96, 77),
    student('가나바', 92, 76, 97, 75),
    student('가나사', 91, 74, 98, 73),
    student('가나아', 99, 75, 99, 71)
]

print('이름', '총점', '평균', sep='\t')
for s in s_ls: 
    print(s.to_string())