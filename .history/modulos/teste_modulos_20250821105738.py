from os_modulos import *
import os

flag = True

while flag:
    escolha = int(input("""
1 - Abrir o Whatsapp
2 - Abrir o Suap
3 - Abrir o Google
4 - Abrir o Classroom
5 - Abrir o Notion
6 - Abrir o Spotfy
7 - Abrir a Udemy
8 - Abrir o Bloco de Notas
9 - Abrir o ChatGPT
10 - Abrir o Discord
11 - Desligar (em 30 minutos)
12 - Desligar (em 1 hora)
13 - Desligar agora
14 - Cancelar desligamento
15 - Sair
Escolha:"""))
    if(escolha == 15):
        flag = False
        print("Saindo...")

    elif(escolha == 1):
        open_whatsapp()

    elif(escolha == 2):
        open_suap()

    elif(escolha == 3):
        open_google()

    elif(escolha == 4):
        open_classroom()

    elif(escolha == 5):
        open_notion()

    elif(escolha == 6):
        open_spotfy()

    elif(escolha == 7):
        open_udemy()

    elif(escolha == 8):
        open_notepad()
        
    elif(escolha == 9):
        open_gpt()

    elif(escolha == 10):
        open_discord()

    elif(escolha == 10):
        shutdown_half_an_hour()

    elif(escolha == 11):
        shutdown_one_hour()

    elif(escolha == 12):
        shutdown_now()

    elif(escolha == 13):
        cancel_shutdown()

    os.system('cls')