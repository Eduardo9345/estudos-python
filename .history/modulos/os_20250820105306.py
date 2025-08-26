import os

# os.system('ver')

# os.system('systeminfo')

# os.system('cls')

# os.system('shutdown /s')
# os.system('shutdown /a')

def shutdown_one_hour():
    os.system("shutdown /s /t 3600")

def shutdown_half_an_hour():
    os.system("shutdown /s /t 1800")

def shutdown_now():
    os.system("shutdown /s /t 0")

def cancel_shutdown():
    os.system("shutdown /a")

def open_google():
    os.system("start https://google.com")

def open_chrome():
    os.system("start chrome")

def open_suap():
    os.system("start https://suap.ifpb.edu.br/")

def open_notepad():
    os.system("notepad")

def open_calc():
    os.system("calc")

# shutdown_one_hour()

# shutdown_half_an_hour()

#cancel_shutdown()

open_calc()