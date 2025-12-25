from gtts import gTTS
from playsound3 import playsound

# 텍스트 입력
text = input('음성으로 변환할 텍스트를 입력하세요: ')

# 한국어로 음성을 출력하도록 설정
tts = gTTS(text, lang='ko')

# 음성을 mp3 파일로 저장
tts.save('output.mp3')

# 저장한 mp3 파일 재생
playsound('output.mp3')
