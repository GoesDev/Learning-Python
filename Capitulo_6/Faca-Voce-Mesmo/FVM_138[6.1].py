# 6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
# que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
# cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
# age e city. Mostre cada informação armazenada em seu dicionário.

person = {
    'first_name': 'júlio',
    'last_name': 'goes',
    'age': '24',
    'city': 'carapicuíba'
}

for i in person:
    print(f"{i.title()}: {person[i].title()}")
