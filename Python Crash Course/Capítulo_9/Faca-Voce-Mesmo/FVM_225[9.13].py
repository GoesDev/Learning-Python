"""9.13 – Reescrevendo o programa com OrderedDict: Comece com o Exercício
6.4 (página 155), em que usamos um dicionário-padrão para representar um
glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
que a ordem da saída coincida com a ordem em que os pares chave-valor
foram adicionados ao dicionário.
"""
from collections import OrderedDict

glossario = OrderedDict()
glossario = {
    'python': 'linguagem de programação',
    'visual studio code': 'editor de texto',
    'ciência de dados': 'ramo de atuação de um cientista de dados',
    'django': 'framework web',
    'flask': 'microframework web',
    'pandas': 'biblioteca para trabalhar com dados'
}

for key, value in glossario.items():
    print(f"Termo: {key.title()} | Significado: {value.capitalize()}")
