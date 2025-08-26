import re

text = "Udemy - uma plataforma com muitos cursos"

match = re.search(r'muitos cursos', text)

print(f'Indice inicial: {match.start()}')
print(f'Indice final: {match.end()}')

site = "https://udemy.com"

match = re.search(r'\.', site)

print(match)

pattern = "[g-m]" #Quais os caracteres de a-m que tem no texto

result = re.findall(pattern, text)

print(result)

rule = r'^A'

phrases = ["A casa esta suja", "O dia está claro"]

for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde {f}")
    else:
        print(f"Não corresponde: {f}")