import re

text = "Udemy - uma plataforma com muitos cursos"

match = re.search(r'muitos cursos', text)

print(f'Indice inicial: {match.start()}')
print(f'Indice final: {match.end()}')

site = "https://udemy.com"

match = re.search(r'\.', site)

print(match)

pattern = "[a-m]" #Quais os caracteres de a-m que tem no texto

result = re.findall(pattern, text)