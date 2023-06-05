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

for person, value in favorite_places.items():
    print(f"{person} favorite places are: {value[0], value[1], value[2]}")
