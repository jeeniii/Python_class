# TTS ( Text to Speech )

from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# Eng
# text = 'What are phrases used at the hotel? Have you ever stayed at a hotel and felt like the staff was speaking another language?'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# Kor
# text = '파이썬은 아직 감이 잘 안잡힌다. 이게 맞는건가?' #하드 코딩
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

# playsound(file_name)

# 긴 문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

playsound(file_name)