import produto as prod

menu = """
1 - Adicionar produto
2 - Listar todos os produtos
3 - Listar produto por id
4 - Listar produto por nome
5 - Atualizar produto
6 - Deletar produto
S - Sair
Escolha:
"""
flag = True

while flag:
    choice = input(menu).lower()
    match choice:
        case "1":
            nome = input("Insira o nome do produto: ")
            qtd_produto = input("Insira a quantidade: ")
            preco_unitario = input("Insira o preco unitário: ")
            prod.adiciona_produto(nome, qtd_produto, preco_unitario)
            print("Produto adicionado!")
            
        case "2":
            header = f"Lista de produtos:\n{'Nome'.ljust(11)}|{' Preco'.ljust(12)}|{' Quantidade'.ljust(12)}| Total\n"
            line =  "-" * len(header) + "\n"
            print(header + line + prod.get_all_produtos_string())
            
        case "3":
            id = input("Insira o id do produto: ")
            header = f"\n{'Nome'.ljust(11)}|{' Preco'.ljust(12)}|{' Quantidade'.ljust(12)}| Total\n"
            line =  "-" * len(header) + "\n"
            print("Produto:\n" + header + line + prod.get_produto_by_id(id))
        
        case "4":
            nome = input("Insira o nome do produto: ")
            print("Produto:", prod.get_produto_by_name(nome))
            
        case "5":
            id = input("Insira o id do produto: ")
            nome = input("Insira o nome do produto: ")
            qtd_produto = input("Insira a quantidade: ")
            preco_unitario = input("Insira o preco unitário: ")
            
            prod.update_produto(id, nome, qtd_produto, preco_unitario)
            print("Produto atualzado!")
            
        case "6":
            id = input("Insira o id do produto: ")
            prod.delete_produto(id)
            print("Produto deletado!")
        
        case "s":
            flag = False