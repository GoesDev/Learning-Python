# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
# crie uma lista contendo esses itens e então utilize cada função apresentada
# neste capítulo pelo menos uma vez.

idiomas = ['Zahôri', 'Drakmôr', 'Garôth', 'Karô', 'Maôno']

print(f'Idiomas em ordem alfabética: {sorted(idiomas)}')
print(f'Idiomas em ordem alfabética inversa: {sorted(idiomas, reverse=True)}')
idiomas.append('Humô')
print(f'Novo idioma adicionado: {idiomas}')
idiomas.insert(0, 'Sôli')
print(f'Novo idioma adicionado: {idiomas}')
print(f'No momento temos {len(idiomas)} idiomas.')
