import requests

# IP 주소 가져오기
response = requests.get('https://api.ipify.org')
external_ip = response.text
print("외부 IP: "+ external_ip)