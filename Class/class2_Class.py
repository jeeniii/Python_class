class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TravelBlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 걸림')

# class TravelBlackBox(BlackBox):
#     # self.name, price를 상속으로 가져오기
#     def set_travel_mode(self, min):
#         print(f'{self.name} {min}분 걸림')

# b2 = TravelBlackBox('ddd', 2000)
# b2.set_travel_mode(30)


# class TravelBlackBox222(BlackBox):
#     def __init__(self, name, price, sd):
#         super().__init__(name, price)
#         self.sd = sd

#     def set_travel_mode(self, min):
#         print(f'{self.name} {min}분 걸림')


# b3 = TravelBlackBox222('ddd', 2000, 999)
# b3.set_travel_mode(50)

class VideoMaker:
    def make(self):
        print('추억 쌓기')


class TravelBlackBox333(BlackBox, VideoMaker):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

b4 = TravelBlackBox333('ddd',2000, 444)
print(b4.name, b4.price, b4.sd)
b4.make()

class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox444(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

b5 = TravelBlackBox444('ddd',2000, 444)
print(b5.name, b5.price, b5.sd)
b5.make()
b5.send()


# Reset
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min)+'에게겍게')
        self.make()
        self.send()