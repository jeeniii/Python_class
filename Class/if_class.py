# If
today = '토요일'
# if today == '일요일' :
#     print('게임 하쉴?')
# print('공부 시작')

# if today == '일요일' :
#     print('게임 하쉴?')
# else : 
#     print('폰 겜 허쉴?')
# print('공부 시작')

if today == '일요일' :
    print('게임 하쉴?')
elif today == '토요일' : 
    print('물 한잔 허쉴?')
else : 
    print('폰 겜 허쉴?')
print('공부 시작')

# If 중첩
yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('퇴장')
    else:
        print('조심')
else:
    print('주의')
