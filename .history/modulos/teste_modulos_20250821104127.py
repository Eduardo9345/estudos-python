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
9 - Sair
Escolha:"""))
    if(escolha == 9):
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

    os.system('cls')