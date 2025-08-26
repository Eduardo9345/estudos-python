name = input("Digite o nome do filme:\n")
year_launch = int(input("Digite o ano de lançamento do filme:\n"))
note_movie = float(input("Digite a nota do filme:\n"))

print("Dados filmes")
print("=" * 25)
print("Nome do filme:", name)
print("Ano de lancamento:", year_launch)
print("Nota do filme:", note_movie)

print("Nome do filme:", name, "\nAno lancamento:", year_launch, "\nNota do filme:", note_movie)

print(f"Nome do filme: {name}\n"
      f"Ano de lancamento: {year_launch}\n"
      f"Nota do filme: {note_movie}\n")