import qrcode
import os

# QR 코드 생성 함수
def create_qrcode(data,file_name) :
    # QR 코드 생성
    img = qrcode.make(data)
    # 이미지 파일로 저장
    qr_file_path = os.path.join("04.QR_code_generator",f"qr_{file_name}.png")
    img.save(qr_file_path)

# QR 코드에 넣을 데이터
data_file_path = os.path.join("04.QR_code_generator","hello.txt")

# txt 파일에서 data 읽어오기
with open(data_file_path,"r") as f:
    # 전체 내용을 하나의 QR 코드로 만드는 경우
    data =f.read()
    # 파일 이름 추출
    base_name = os.path.basename(data_file_path)
    file_name = os.path.splitext(base_name)[0]
    # 함수 호출 QR 코드 생성
    create_qrcode(data,file_name)
    
    # 각 문자열을 개별 QR 코드로 만드는 경우 
    # for line in f:
    #     data = line.strip()
    #     # 함수 호출 QR 코드 생성
    #     create_qrcode(data)
    