# 6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
# 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
# apresente o nome de cada pessoa, juntamente com seus números favoritos.
person_numbers = {
    'duda': ['1', '2'],
    'goes': ['25', '3'],
    'turif': ['3', '6']
}

for i in person_numbers:
    print(i.title(), person_numbers[i][0], person_numbers[i][1])
