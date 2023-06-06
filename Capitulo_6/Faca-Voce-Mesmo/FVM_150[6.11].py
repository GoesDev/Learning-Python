# 6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
# cidades como chaves em seu dicionário. Crie um dicionário com informações
# sobre cada cidade e inclua o país em que a cidade está localizada, a
# população aproximada e um fato sobre essa cidade. As chaves do dicionário
# de cada cidade devem ser algo como country, population e fact. Apresente o
# nome de cada cidade e todas as informações que você armazenou sobre ela.

cities = {
    'kadoan': {
        'country': 'sacro império humani',
        'population': '800',
        'fact': 'é conhecida como o começo da vida de um aventureiro'
    },
    'kollyhan': {
        'country': 'sacro império humani',
        'population': '50000',
        'fact': 'chamada também de capital branca'
    },
    'cyril': {
        'country': 'sacro império humani',
        'population': '3000',
        'fact': 'chamada também de cidade prateada'
    }
}

for key in cities.keys():
    print(f"\t{key.title()}")
    for new_key, new_value in cities[key].items():
        print(f"{new_key.title()}: {new_value}")
    print("***" * 10)
