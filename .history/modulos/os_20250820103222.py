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

shutdown_one_hour()    