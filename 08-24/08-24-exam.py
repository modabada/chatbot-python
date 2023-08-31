import csv
import getpass
import os
import random
import re
import time


double_quote_to_int = lambda x: int(eval(x)) if type(x) != int else x


def get_book_list():
    with open('book.csv', 'r') as f:
        rd = csv.reader(f)
        return list(rd)

def get_user_dict():
    with open('user.csv', 'r') as f:
        r = dict()
        rd = csv.reader(f)
        for data in rd:
            data[2] = [] if data[2] == '[]' else data[2][1:-1].split(',')
            data[3] = [] if data[3] == '[]' else data[3][1:-1].split(',')
            r[data[0]] = {'pw': data[1], 'book': data[2], 'lent': data[3]}
        return r

def save_user_dict():
    with open('user.csv', 'w', newline='\n') as f:
        wr = csv.writer(f)
        for id, data in users.items():
            book = []
            lent = []
            if 'book' in data:
                book = data['book']
            if 'lent' in data:
                lent = data['lent']
            wr.writerow([id, data['pw'], book, lent], )

books:list = get_book_list()
users:dict = get_user_dict()

def page_display(pageName):
    l = len(pageName) + 4
    l += len(re.findall('[ㄱ-힣]', pageName))
    os.system('cls')
    print('=' * l)
    print(' ', pageName, ' ')
    print('=' * l)

def first_page():
    while True:
        page_display('초기 페이지')
        print("어디로 이동하시겠습니까?")
        print('\t1. 로그인')
        print('\t2. 회원가입')
        print('\t3. 도서 반납')
        print('\t4. 종료')
        i = input().strip()
        if i == '1':
            return login()
        elif i == '2':
            return regis()
        elif i == '3':
            refunt_by_book_id()
        elif i == '4':
            exit(0)
        else:
            print('다시 입력해주세요')

def title(id):
    page_display(f'메인화면입니다. 환영합니다 {id}님')
    print('오늘의 추천 도서')
    for i in range(5):
        print(f'\t({i + 1}). {books[i][5]}')
    print()

def main(id):
    while True:
        title(id)
        print('어디로 이동하시겠습니까?')
        print(f'\t1. 도서 조회')
        print(f'\t2. 도서 대여')
        print(f'\t3. 도서 반납')
        print(f'\t4. 종료')
        i = input().strip()
        if i == '1':
            search(id)
            title(id)
        elif i == '2':
            lent(id)
        elif i == '3':
            refund(id)
        elif i == '4':
            exit(0)
        else:
            print('다시 입력해주세요')
            time.sleep(2)

def login():
    page_display('로그인 화면')
    while True:
        id = input('아이디를 입력해주세요: ').strip()
        pw = getpass.getpass('비밀번호를 입력해주세요 (입력 내용이 보이지 않습니다): ').strip()
        if id in users and users[id]['pw'] == pw:
            return login_suc(id)
        else:
            print('로그인 실패')

def login_suc(id):
    page_display(f'로그인 성공! 어서오세요. {id}님')
    print('2초 후 메인 화면으로 진입합니다')
    time.sleep(2)
    main(id)

def regis():
    page_display('회원가입 화면입니다.')
    while True:
        id = input('생성할 아이디를 입력해주세요: ').strip()
        pw = getpass.getpass('생성할 비밀번호를 입력해주세요(입력 내용이 보이지 않습니다): ').strip()
        pw2 = getpass.getpass('비밀번호 확인(입력 내용이 보이지 않습니다): ').strip()
        if pw != pw2:
            print('비밀번호가 다릅니다')
            continue
        if id not in users:
            users[id] = {'pw': pw, 'book': [], 'lent': []}
            save_user_dict()
            page_display(f'회원가입 성공! 어서오세요. {id}님')
            print('2초후 메인화면으로 진입합니다')
            return main(id)
        else:
            print('이미 존재하는 아이디입니다')
    
def search(id):
    page_display('도서 조회 화면입니다')
    while True:
        print('검색어 조건을 설정합니다')
        print(f'\t1. 특정 도서명 검색')
        print(f'\t2. 특정 저자명 검색')
        print(f'\t3. 특정 도서관별 도서 검색')
        i = input().strip()
        if i == '1':
            return search_books(id, 5)
        elif i == '2':
            return search_books(id, 6)
        elif i == '3':
            return search_books(id, 1)
        else:
            print('다시 입력해주세요')

def search_books(id, column):
    os.system('cls')
    lib_name = random.choice(books)[1]
    if column != 1:
        print(f'{lib_name}에 대해 검색합니다: ')
    s = input('입력: ').strip()
    ls = [b for b in books if ( (column == 1) or (b[1] == lib_name)) and (s in b[column])]
    page = 0
    TOTAL_P = len(ls) // 15 + 1
    def display_list(page) :
        os.system('cls')
        display_basket(id)
        print()
        print('조회된 목록')
        print('{:10}{:15}{:15}{:30}{:10}{:10}'.format('책번호', '등록번호', '도서관', '도서명', '저자명', '발행처'))
        for i in range(min(15, len(ls[page*15:page*15 + 15]))):
            i = page * 15 + i
            print('{:10}|{:15}|{:15}|{:10}|{:10}'.format(
                str(i + 1) + '.',
                ls[i][4],
                ls[i][1],
                ls[i][5],
                ls[i][6],
                ls[i][7]
                )
            )
        print()
        print(f'페이지 {page + 1}/{TOTAL_P}')
        print('\t 페이지번호')
        print('\t+책 번호. 장바구니에 책을 넣는다.')
        print('\t-장바구니 번호. 장바구니에 책을 뺀다.')
        print('\tend 검색 종료')
        
    while True:
        display_list(page)
        i:str = input().strip()
        if i.isdecimal():
            page = int(i) - 1
        elif i[0] == '+':
            b = users[id]['book']
            if len(b) < 5:
                i = int(i[1:]) - 1
                b.append(ls[i][0])
                users[id]['book'] = b
                save_user_dict()
        elif i[0] == '-':
            del users[id]['book'][int(i[1:]) - 1]
            save_user_dict()
        elif i == 'end':
            return
        else:
            print('다시 입력해주세요')

def display_basket(id):
    print('장바구니')
    b = list(map(double_quote_to_int, users[id]['book']))
    for i in range(5):
        print(f'[{i + 1}]: {"" if len(b) <= i else books[b[i]][5]}')

def lent(id):
    while True:
        page_display('도서 대여 화면입니다')
        display_basket(id)
        
        print('기능을 선택해주세요')
        print('\t-장바구니 번호, 장바구니에서 책 빼기')
        print('\t1. 장바구니 대여')
        print('\t2. 조회 화면 이동')
        print('\t3. 메인 화면 이동')
        i = input().strip()
        if i[0] == '-':
            del users[id]['book'][int(i[1:]) - 1]
            save_user_dict()
        elif i[0] == '1':
            long = int(input('대여 기간을 설정해주세요(1~5): '))
            if 0 < long < 6:
                lent:list = users[id]['lent']
                book :list = list(map(double_quote_to_int, users[id]['book']))
                if len(lent) + len(book) > 5:
                    print('대여 가능 목록을 초과했습니다')
                    print('2초 후 다시 입력으로 돌아갑니다')
                    time.sleep(2)
                    continue
                lent.extend(book)
                users[id]['lent'] = lent
                users[id]['book'] = []
                save_user_dict()
                print('대여가 완료되었습니다')
                print('2초뒤 메인화면으로 나갑니다')
                time.sleep(2)
                return
        elif i[0] == '2':
            return search(id)
        elif i[0] == '3':
            return

def refund(id):
    while True:
        page_display('도서 반납 환경입니다')
        print('반납 방식을 선택하세요')
        print('\t1. 등록번호로 반납')
        print('\t2. 대여 목록으로 반납')
        print('\t3. 반납 종료')
        i = input().strip()
        if i == '1':
            refunt_by_book_id(id)
        elif i == '2':
            if users[id]['lent'] == list():
                print('대여한 책이 없습니다!')
                print('2초 후 자동으로 이전으로 돌아갑니다')
                time.sleep(2)
                continue
            print_lent_list(id)
            i = input('대여 목록에서 반납할 책을 선택해주세요(1~5):')
            if not i.isdecimal():
                continue
            i = int(i)
            if i < 1 or i > 5:
                print('올바르지 않은 범위입니다')
                print('2초 후 자동으로 이전으로 돌아갑니다')
                time.sleep(2)
                continue
            if input('반납하시겠습니까?(y/n)').strip().upper() == 'Y':
                del users[id]['lent'][i - 1]
                save_user_dict()
                print('반납됐습니다')
                print('2초 후 자동으로 이전으로 돌아갑니다')
                time.sleep(2)
        elif i == '3':
            return

def refunt_by_book_id(id=None):
    book_id = input('대여한 책의 등록번호를 입력하세요: ').strip()
    for i in range(len(books)):
        if books[i][4] == book_id:
            if id == None:
                for user_id, data in users.items():
                    for lent_i in range(len(data['lent'])):
                        if book_id == books[double_quote_to_int(data['lent'][lent_i])][4]:
                            id = user_id
                if id == None:
                    print('대여되지 않은 책입니다')
                    print('2초 후 자동으로 이전으로 돌아갑니다')
                    return time.sleep(2)
            for lent_book_i, lent_book_id in enumerate(users[id]['lent']):
                if book_id == books[double_quote_to_int(lent_book_id)][4]:
                    del users[id]['lent'][lent_book_i]
                    print('반납됐습니다')
                    print('2초 후 자동으로 이전으로 돌아갑니다')
                    save_user_dict()
                    time.sleep(2)
                    break
                elif lent_book_i + 1== len(users[id]['lent']):
                    print('대여되지 않은 책입니다')
                    print('2초 후 자동으로 이전으로 돌아갑니다')
                    return time.sleep(2)
            break
        elif i + 1 == len(books):
            print('대여되지 않은 책입니다')
            print('2초 후 자동으로 이전으로 돌아갑니다')
            return time.sleep(2)

def print_lent_list(id):
    print('대여 목록')
    for i in range(len(users[id]['lent'])):
        book_id = double_quote_to_int(users[id]['lent'][i])
        print(f'{i + 1}. {books[book_id][5]}')


first_page()