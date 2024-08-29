# for
# for x in range(10):
#     print(f'팔 벌려 뛰기 {x}회')

# for x in range(1, 30, 10):
#     print(f'{x}번은 {x}번부터 {x+9}까지 모아줘')

# for 2
# list = [1,2,3]
# for x in list : 
#     print(x)

# app = 'apple'
# for x in app : 
#     print(x)

# while
# max = 25
# weight = 0
# item = 3

# while weight + item <= max :
#     weight += item
#     print('짐짝 추가')
# print(f'총 무게는 {weight} 입니다')

# break

drama = ['season1', 'season2', 'season3', 'season4', 'season5']

# for x in drama : 
#     if x == 'season3' : 
#         print('Finished')
#         break
#     print(f'{x} See')

# continue
# for x in drama :
#     if x == 'season3' : 
#         print('No Jam')
#         continue
#     print(f'{x} See')

#  Call

products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = []

# for x in products : 
#     if x.startswith('SIRO'):
#         recall.append(x)
# print(recall)

# 한 줄로 축약 가능 List Comprehension (aaa = [변수활용 for 변수 in 반복대상 if 조건]) ==> 새 리스트에 담는 행위
rerecall = [x for x in products if x.startswith('SIRO')]
print(rerecall)

print('===========================')

print([p + 'SE' for p in products])
print([p.lower() for p in products])
print([p + '(신상)' for p in products if p.endswith('2022')])



