# # Import1 모듈 모든 기능을 가져온다
# import goodjob
# goodjob.say()

# Import2 모듈 중 필요한것만 가져온다
# from goodjob import say
# say()

# 다른 폴더에서 가져오기
import JinCode.goodjoob
JinCode.goodjoob.say()

from JinCode import goodbye
goodbye.bye()