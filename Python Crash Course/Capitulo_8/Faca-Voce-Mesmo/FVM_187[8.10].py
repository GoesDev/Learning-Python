"""8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada."""


def make_great(magicians, great_magician):
    while magicians:
        current_magic = magicians.pop()
        great_magician.append("great" + " " + current_magic)


def show_magicians(magicians):
    for magic in magicians:
        print("O próximo mágico a se apresentar é: " + magic.title())


magicians = ['júlio', 'goes', 'cesar']
great_magician = []

make_great(magicians, great_magician)
show_magicians(great_magician)
