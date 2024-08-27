lang = 'PYTHON'

# print(lang[1:4])
print(lang[:])


snack = '꿀꽈배기'
print(len(snack))

twistSnack = '''꿀꽈배기는
너무
맛있다잉'''

print(len(twistSnack))


regret = '아니 1분만에 파이썬을 어떻게 배우냐고'

print(len(regret))

letter = 'how are YOU'

print(letter.count('how'))

sss = 'StartandEnd'
sss_point = '...StartandEnd...'
print(sss.startswith('Se'))
print(sss.endswith('End'))
print(sss.strip('.'))
print(sss.replace('Start', 'First'))
print(sss.find('and'))
print(sss.center(21,'-'))

python = 'PYTHON'
java = 'JAVA'

print(python, java)
print('개발 언어중 나는 {},{}을 할 수 있다'.format(python,java))
print('개발 언어중 나는 {1},{0}을 할 수 있다'.format(python,java))
print(f'개발 언어중 나는 {python},{java}을 할 수 있다')

print('하지만\'나만 당할 순 없지\'라는 생각에\"엄청 쉽지\"라고 했다.')


print('==============================')
# 리스트
# 노트북에서 했으므로 생략

# 튜플

# 1은 생략

# 2
numbers = (1,2,3,4,5,6,7,8,9,10)
# (one, two, *others) = numbers
# print(one)
# print(two)

# (*others, nine, ten) = numbers
# print(nine)
# print(ten)

(one, *others, ten) = numbers
print(one)
print(ten)

# 나머지는 배열로 저장된다
print(others)


# 세트

A_set = {'a', 'b', 'c'}
B_set = {'c', 'd', 'e'}

# 교집합
print(A_set.intersection(B_set)) 
# 합집합(순서 보장 X)
print(A_set.union(B_set)) 
# 차집합
print(A_set.difference(B_set)) 

A_set.add('제육')
print(A_set) 
A_set.remove('c')
print(A_set) 
'''빈 세트로 지정'''
# A_set.clear()
# print(A_set) 
'''세트의 삭제'''
# del A_set
# print(A_set)
 
# discard는 값이 없어도 오류가 나지 않음
# remove는 오류가 난다
A_set.discard('d')
print(A_set) 

# Dictionary 1
person = {
    '이름': 'Yein',
    '나이': 23,
    '키': 163,
    '무게': 44
}

print(person['나이'])

# Dictionary 2
person['최종학력'] = '덕성여대'
print(person['최종학력'])
person['키'] = 162
print(person['키'])
person.update({'이름': '예인', '무게': 42})
print(person['이름'], person['무게'])