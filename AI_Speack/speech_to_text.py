# STT ( Speech to Text )

import speech_recognition as sr

# 음성 인식
reg = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있습니다.')
    audio = reg.listen(source) # 마이크로 음성 듣기

# 음성 파일 인식 후 텍스트로 변환 (wav, aiff, flac)
# reg = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio = reg.record(source)

try:
    # Eng
    # text = reg.recognize_google(audio, language='en-US')
    # print(text)

    # Kor
    text = reg.recognize_google(audio, language='ko')
    print(text)
    

except sr.UnknownValueError:
    print('인식 실패')
except sr.RequestError as e:
    print('요청 실패: {0}'.format(e)) #API Key 오류, 네트워크 단절 등...
except Exception as e:
    print(f'알 수 없는 오류 발생: {e}')

# def callback(indata, outdata, frames, time, status):
#     volume_norm = np.linalg.norm(indata)
#     print("Volume: "+ '='*(int(volume_norm)) + ' '*(79-(int(volume_norm)))+'\r', end='')

#     # indata를 outdata에 넣으면 마이크로 넘어온 데이터가 스피커로 출력한다.
#     outdata[:] = indata

# try:
#     with sd.Stream(callback=callback):
#         input("Press Enter to quit.\n\n")
# except KeyboardInterrupt:
#     print("exit.")