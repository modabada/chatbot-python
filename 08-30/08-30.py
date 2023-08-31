import math
import re

def splitter(title):
    print()
    l = len(title) + 4
    l += len(re.findall('[ㄱ-힣]', title))
    print('-' * l)
    print(' ', title, ' ')
    print('-' * l)


splitter('GC')
class Test:
    def __init__(self, name):
        self.name = name
        print('생성', self.name)
    def __del__(self):
        print('파괴', self.name)

Test('a')
Test('b')
Test('c')


splitter('private')
class Circle:
    def __init__(self, r):
        self.__r = r
    def get_curcumference(self):
        return 2 * math.pi * self.__r
    def get_area(self):
        return math.pi * self.__r ** 2

c = Circle(10)
print(c.get_curcumference())
print(c.get_area())


splitter('예외클래스')
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)

raise CustomException()