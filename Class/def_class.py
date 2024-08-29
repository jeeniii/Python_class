# def show_price():
#     print('감성 커트는 15000원이다 씹덕아')

# customer1 = '나'
# print(f'{customer1} 고객아')
# show_price()

# customer2 = '너'
# print(f'{customer2} 고객아')
# show_price()

# def show_price(customer):
#     print(f'{customer} 고객아')
#     print('감성 커트는 15000원이다 씹덕아')

# customer1 = '나'
# show_price(customer1)

# customer2 = '너'
# show_price(customer2)

# Return
# def get_price(is_vip):
#     if is_vip == True:
#         return 10000
#     else:
#         return 15000
    
# price1 = get_price(True)
# price2 = get_price()
# price3 = get_price()
# price4 = get_price()

# def order(shipping = '선불'):
#     print(f'주문이 완료됨.{shipping}이다')

# order()

# 아래처럼 하면 review만 true로 바뀐다
# def get_price(is_vip=False,
#             is_birthday=False,
#             is_membership=False,
#             card=False,
#             review=False,
#             first_time=False):

# price = get_price(review = True)

# 가변 인수
# def visit( today, *customers):
#     print(today)
#     for customer in customers:
#         print(customer)

# visit('2022년 6월 10일', '나장발') # 1명 방문
# visit('2022년 6월 10일', '나장발', '나수염') # 2명 방문
# visit('2022년 6월 10일', '나장발', '나수염', '나김리') # 3명 방문

# input
# name = input('What your Name?')
# print(name)

# num = int(input('How Many...?'))
# if num > 4:
#     print('Im sorry.')
# else:
#     print('come in')

# open 함수

# < 열기 모드 >
# r : read (읽기)
# w : write (쓰기)
# a : append (이어서 쓰기)#

# f = open('list.txt', 'w', encoding='UTF8')
# f.write('open1\n')
# f.write('open2\n')
# f.write('open3\n')
# f.close()

# f = open('list.txt', 'r', encoding='UTF8')
# contents = f.read()
# print(contents)
# f.close

# f = open('list.txt', 'r', encoding='UTF8')
# for line in f: #파일에서 한 줄씩 가져와서 console에 찍기
#     print(line, end='')
# f.close()

# close 함수 없이 파일 읽기(쓰기도 가능)
with open('list.txt', 'r', encoding='UTF8') as f: # f는 변수이므로 얼마든지 변경 가능
    contents = f.read()
    print(contents)
