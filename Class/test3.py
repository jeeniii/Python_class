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