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
while True:
    choice = input(menu)
    match choice:
        case "1":
            nome = input("Insira o nome do produto:")
            qtd_produto = input("Insira a quantidade:")
            preco_unitario = input("Insira o preco unitário:")
            prod.adiciona_produto(nome, qtd_produto, preco_unitario)
            print("Produto adicionado!")
            
        case "2":
            print("Lista de produtos:\n", prod.get_all_produtos())
            
        case "3":
            id = input("Insira o id do produto:")
            print("Produto:", prod.get_produto_by_id(id))
        
        case "4":
            nome = input("Insira o nome do produto:")
            print("Produto:", prod.get_produto_by_name(nome))
            
        case "5":
            id = input("Insira o id do produto:")
            nome = input("Insira o nome do produto:")
            qtd_produto = input("Insira a quantidade:")
            preco_unitario = input("Insira o preco unitário:")
            
            prod.update_produto(id, nome, qtd_produto, preco_unitario)
            print("Produto atualzado!")
    break