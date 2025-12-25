import socket
import requests

# 내부 IP 가져오기
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("내부 IP: "+ ip_address)

# 외부 IP 가져오기
response = requests.get('https://api.ipify.org')
external_ip = response.text
print("외부 IP: "+ external_ip)