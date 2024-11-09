# 6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
# três nomes para usar como chaves do dicionário e armazene de um a três
# lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
# interessante, peça a alguns amigos que nomeiem alguns de seus lugares
# favoritos. Percorra o dicionário com um laço e apresente o nome de cada
# pessoa e seus lugares favoritos.

favorite_places = {
    'Turif': ['gaiola', 'chão do quarto', 'eduarda'],
    'Goes': ['casa', 'parque', 'cinema'],
    'Duda': ['casa', 'mercado', 'cinema']
}

for person in favorite_places:
    print(f"{person} favorite places are:")
    print(f"\t{favorite_places[person][0].title()}")
    print(f"\t{favorite_places[person][1].title()}")
    print(f"\t{favorite_places[person][2].title()}")
