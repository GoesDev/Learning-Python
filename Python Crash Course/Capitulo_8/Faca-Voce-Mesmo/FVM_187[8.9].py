"""8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista."""


def show_magicians(magicians):
    for magic in magicians:
        print("O próximo mágico a se apresentar é: " + magic.title())


magicians = ['júlio', 'goes', 'cesar']
show_magicians(magicians)
