from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar contatos")
        print("2. Listar Contatos")
        print("3. Remover contatos")
        print("4. Sair")

        choice = input("Escolha a opção (1 - 4):\n")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            delete_contacts()

        else:
            break