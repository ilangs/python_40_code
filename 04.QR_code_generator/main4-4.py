# txt 파일을 읽어서 QR 코드를 생성하는 프로그램 (copilot 버전)
# txt 파일이 있는 동일 경로에 QR 코드를 이미지 파일로 저장
# QR 파일명은 qr_<file_name>.png 로 저장

import qrcode
import os

def generate_qr_from_txt(file_path):
    # 파일 이름과 확장자 분리
    file_name, _ = os.path.splitext(os.path.basename(file_path))    # 언패킹 방식 (file_name, ext)
    # file_name = os.path.splitext(os.path.basename(file_path))[0]  # 인덱싱 방식 [0]
    
    # txt 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    
    # 1. qrcode.make(data) (간편 방식)
    # 가장 빠르고 쉬운 방법으로, 라이브러리가 상황에 맞춰 최적의 설정을 자동으로 결정합니다.
    # 특징: 복잡한 설정 없이 데이터만 넣으면 즉시 이미지를 반환합니다.
    # 장점: 코드가 매우 짧고 간결합니다. 일반적인 QR 코드를 만들 때 가장 많이 사용됩니다.
    # 단점: QR 코드의 크기, 테두리 두께, 복구 능력(오류 정정) 등을 세밀하게 조절할 수 없습니다.
    
    # 2. qrcode.QRCode(...) (상세 설정 방식)
    # QR 코드의 외형과 성능을 직접 설계하는 방식입니다. 인스턴스(qr)를 먼저 만들고 데이터를 나중에 넣습니다.
    # version: QR 코드의 격자 크기(1~40)를 결정합니다. 1은 가장 작고(21x21), 숫자가 커질수록 더 많은 데이터를 담을 수 있습니다.
    # error_correction: QR 코드가 일부 오염되거나 훼손되어도 읽을 수 있게 하는 오류 정정 수준입니다. L(7%) < M(15%) < Q(25%) < H(30%) 순으로 복구 능력이 좋아지지만, 대신 격자가 더 복잡해집니다.
    # box_size: QR 코드의 각 점(픽셀) 크기를 조절합니다. 숫자가 클수록 생성되는 이미지 파일이 커집니다.
    # border: QR 코드 주변의 하얀색 테두리 두께를 설정합니다. (최소 4 권장)
    # fit=True: 입력한 데이터 양에 비해 version을 너무 작게 설정했을 때, 자동으로 버전을 높여서 크기를 맞춰줍니다.

    
    # 이미지 생성
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 이미지 파일명 설정
    qr_file_name = f"qr_{file_name}.png"
    
    # 이미지 저장
    img.save(qr_file_name)
    print(f"QR 코드가 '{qr_file_name}'로 저장되었습니다.")

# 예시 사용
if __name__ == "__main__":
    txt_file_path = "hello.txt"  # 여기에 읽을 txt 파일 경로를 입력
    generate_qr_from_txt(txt_file_path) 
    