import pyttsx3

# 한글 TTS 엔진 설정
engine = pyttsx3.init()
engine.setProperty('rate', 150) # 말하는 속도 설정

# 텍스트를 읽어주는 함수 정의
def speak(text) :
    engine.say(text)
    engine.runAndWait()

# 텍스트를 입력받아 TTS로 변환
text = "안녕하세요! 챗GPT로 만드는 파이썬 작품들 입니다."
speak(text)
