import os


def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o telefone:\n")

    contact = f"Nome: {name} \nEndereco: {address} \nTelefone: {phone}\n"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)