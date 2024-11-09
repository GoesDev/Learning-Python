# 6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
# (página 147). Crie dois novos dicionários que representem pessoas diferentes
# armazene os três dicionários em uma lista chamada people. Percorra sua lista
# de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
# você sabe sobre cada pessoa.


def newPerson():
    first_name = input("What is your name? ")
    last_name = input("What is your last name? ")
    age = input("How old are your? ")
    city = input("Where city are you from? ")

    person = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city
    }

    return person

# # people = []

# for i in range(3):
#     person = newPerson()
#     people.append(person)

# print(people)
