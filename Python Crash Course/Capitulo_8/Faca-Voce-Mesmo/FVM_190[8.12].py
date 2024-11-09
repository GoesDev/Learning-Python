"""8.12 Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez."""


def make_sandwich(*toppings):
    """Lets make a sandwich!"""
    print('\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print('-- ' + topping)


make_sandwich('pão', 'carne', 'queijo')
make_sandwich('pão', 'carne', 'queijo', 'alface', 'tomate')
make_sandwich('pão', 'carne vegana', 'queijo de bufala', 'alface')
