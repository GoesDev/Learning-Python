"""9.14 – Dados: O módulo random contém funções que geram números aleatórios
de várias maneiras. A função randint() devolve um inteiro no intervalo
especificado por você. O código a seguir devolve um número entre 1 e 6: from
random import randint x = randint(1, 6)
Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
Escreva um método chamado roll_die() que exiba um número aleatório entre
1 e o número de lados do dado. Crie um dado de seis dados e lance-o dez
vezes.
Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez
vezes."""

from random import randint


class Die():

    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


my_dice = Die(10)
my_dice.roll_die()
