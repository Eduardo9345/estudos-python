import re

text = "Udemy - uma plataforma com muitos cursos"

match = re.search(r'muitos cursos', text)

print(f'Indice inicial: {match.start()}')
print(f'Indice final: {match.end()}')
print(f'Indice final: {match}')