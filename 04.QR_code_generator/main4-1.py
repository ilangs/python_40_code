import qrcode

# QR 코드에 넣을 데이터
data = "https://dirt-cheddar-57f.notion.site/4-Team_project_-2d32114b6f5c801198deeb8dea1a4466?source=copy_link"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장
img.save("qr_proj.png")