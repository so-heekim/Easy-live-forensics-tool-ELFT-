import tkinter as tk
from tkinter import ttk

# 첫 번째 화면: 메인 메뉴
def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Button(root, text="임의제출 확인서 작성", command=show_consent_form).pack(pady=10)
    tk.Button(root, text="화면 녹화", command=show_screen_recording).pack(pady=10)
    tk.Button(root, text="분석 시간 설정", command=show_analysis_time_setting).pack(pady=10)
    tk.Button(root, text="무결성 검증", command=show_integrity_verification).pack(pady=10)

# 두 번째 화면: 임의제출 확인서 작성
def show_consent_form():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="임의제출 확인서 작성", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(root, text="뒤로가기", command=show_main_menu).pack(pady=10)

# 세 번째 화면: 화면 녹화
def show_screen_recording():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="화면 녹화", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text="녹화 시작").pack(pady=5)
    tk.Button(root, text="녹화 시작", command=start_recording).pack(pady=10)
    tk.Button(root, text="뒤로가기", command=show_main_menu).pack(pady=10)

# 네 번째 화면: 분석 시간 설정
def show_analysis_time_setting():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="분석 시간 설정", font=("Helvetica", 16)).pack(pady=10)
    
    tk.Label(root, text="시작 시간").pack(pady=5)
    entry_start_time = tk.Entry(root)
    entry_start_time.pack(pady=5)
    
    tk.Label(root, text="종료 시간").pack(pady=5)
    entry_end_time = tk.Entry(root)
    entry_end_time.pack(pady=5)
    
    tk.Button(root, text="확인", command=lambda: confirm_analysis_time(entry_start_time.get(), entry_end_time.get())).pack(pady=10)
    tk.Button(root, text="뒤로가기", command=show_main_menu).pack(pady=10)

# 다섯 번째 화면: 무결성 검증
def show_integrity_verification():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="무결성 검증", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(root, text="뒤로가기", command=show_main_menu).pack(pady=10)

# 임의제출 확인서 작성 기능 (더미)
def start_recording():
    pass

# 분석 시간 설정 확인 기능 (더미)
def confirm_analysis_time(start_time, end_time):
    pass

def start_ui():
    global root
    root = tk.Tk()
    root.title("Forensic Tool")
    root.geometry("400x300")
    show_main_menu()
    root.mainloop()
