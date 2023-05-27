# 5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então,
# escreva uma série de instruções if independentes que verifiquem se
# determinadas frutas estão em sua lista.
# • Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
# • Escreva cinco instruções if. Cada instrução deve verificar se uma
# determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
# frase, por exemplo, Você realmente gosta de bananas!

favorite_fruits = ['Manga', 'Laranja', 'Morango']


def fruits(fruit):
    if fruit in favorite_fruits:
        print(f"Você realmente gosta de {fruit}")
    else:
        print(f"Você não gosta tanto de {fruit}")


fruits("Laranja")
fruits("Limão")
fruits("Manga")
fruits("Abacaxi")
fruits("Morango")
