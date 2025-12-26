# 컴퓨터의 자원인 CPU, RAM, 네트워크의 사용량을 확인하는 프로그램
# 간단한 GUI를 이용해서 CPU, RAM 사용량을 5초마다 표시하는 프로그램

import psutil
import time 
import tkinter as tk
from tkinter import ttk


def update_resource_usage():
    # 자원 사용량 가져오기
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory()
    
    # 라벨 업데이트
    cpu_label.config(text=f"CPU 사용량: {cpu_percent}%")
    ram_label.config(text=f"RAM 사용량: {ram_info.percent}%")
    
    # 5초 후에 다시 업데이트
    root.after(5000, update_resource_usage)

# GUI 설정
root = tk.Tk()  
root.title("컴퓨터 자원 모니터링")
root.geometry("300x100")
cpu_label = ttk.Label(root, text="CPU 사용량: ")
cpu_label.pack(pady=10)
ram_label = ttk.Label(root, text="RAM 사용량: ")
ram_label.pack(pady=10)
# 자원 사용량 업데이트 시작
update_resource_usage()
# GUI 실행  
root.mainloop()
