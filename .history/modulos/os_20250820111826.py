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

def open_unturned():
    os.system("start steam://rungameid/304930")

def open_stardew():
    os.system("start steam://rungameid/413150")

def open_vscode():
    os.system("start code")

def open_whatsapp():
    os.system("start WhatsAppDesktop_cv1g1gvanyjgm")

# shutdown_one_hour()

# shutdown_half_an_hour()

#cancel_shutdown()

open_whatsapp()