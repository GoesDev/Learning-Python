"""8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico."""


def make_great(magicians, great_magician):
    while magicians:
        current_magic = magicians.pop()
        great_magician.append("great" + " " + current_magic)


def show_magicians(magicians):
    for magic in magicians:
        print("O próximo mágico a se apresentar é: " + magic.title())


magicians = ['júlio', 'goes', 'cesar']
great_magician = []

make_great(magicians[:], great_magician)
show_magicians(great_magician)
print(magicians)
