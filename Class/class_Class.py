# class

# class BlackBox:
#     pass


# b1 = BlackBox()
# b2 = 'ss'

# b1.name = '까망이'
# print(b1.name)
# print(isinstance(b1, BlackBox)) # b1이 BlackBox의 객체가 맞는지 확인


class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # 기능 추가
    # def set_travel_mode(self, min):
    #     print(str(min)+'분 걸림')
    # Self
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 걸림')

b1 = BlackBox('Jin', 20000)
# print(b1.name, b1.price)

b2 = BlackBox('Cin', 10000)
# print(b2.name, b2.price)

b1.set_travel_mode(50)
b2.set_travel_mode(10)
