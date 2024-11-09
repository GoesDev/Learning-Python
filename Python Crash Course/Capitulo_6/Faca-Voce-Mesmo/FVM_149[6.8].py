# 6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
# dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
# o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
# chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
# fizer isso, apresente tudo que você sabe sobre cada animal de estimação.

turif = {
    'name': 'Turif',
    'type': 'Hamster',
    'owner': 'Joana'
}

simba = {
    'name': 'Simba',
    'type': 'Dog',
    'owner': 'Duda'
}

pets = [turif, simba]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print("***")
