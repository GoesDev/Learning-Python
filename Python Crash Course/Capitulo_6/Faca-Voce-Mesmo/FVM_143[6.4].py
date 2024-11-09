# 6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
# um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
# sequência de instruções print por um laço que percorra as chaves e os valores
# do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
# cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
# essas palavras e significados novos deverão ser automaticamente incluídos na
# saída.

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
