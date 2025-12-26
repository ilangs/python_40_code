# 컴퓨터의 자원인 CPU, RAM, 네트워크의 사용량을 확인하는 프로그램
# CPU, RAM, 네트워크의 사용량을 5초마다 출력

import psutil
import time


def print_resource_usage():
    # 자원 사용량 가져오기
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory()
    network_info = psutil.net_io_counters()
    
    # 출력
    print(f"CPU 사용량: {cpu_percent}%")
    print(f"RAM 사용량: {ram_info.percent}%")
    print(f"네트워크 사용량: {network_info.bytes_sent} bytes sent, {network_info.bytes_recv} bytes received")

while True:
    print_resource_usage()
    time.sleep(5)   # 5초 대기