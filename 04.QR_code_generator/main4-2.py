import qrcode
import os

# QR 코드에 넣을 데이터
data = "Hello, world!"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장
file_path = os.path.join("04.QR_code_generator","qrcode.png")
img.save(file_path)