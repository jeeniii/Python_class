num1 = 3
num2 = 1.2

# 예외 처리

# try:
#     result = num1 / num2 
#     print(f'Result is {result}.')
# except:
#     print('Error On')
# else:
#     print('Normal On')
# finally:
#     print('Finished')


# 예외 처리 2
try:
    result = num1 / num2 
    print(f'Result is {result}.')

except ZeroDivisionError:
    print('0으로 못 나눔')
except TypeError:
    print('값의 형태가 이상함')
except Exception as err:
    err = '랴...리건 좀...'
    print('Error On: ', err)