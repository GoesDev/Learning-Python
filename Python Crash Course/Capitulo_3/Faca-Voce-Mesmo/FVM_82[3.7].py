# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
# dois convidados.
# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas
# pessoas para o jantar.
# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
# que apenas dois nomes permaneçam em sua lista. Sempre que remover um
# nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
# saiba que você sente muito por não poder convidá-la para o jantar.
# • Apresente uma mensagem para cada uma das duas pessoas que continuam
# na lista, permitindo que elas saibam que ainda estão convidadas.
# • Utilize del para remover os dois últimos nomes de sua lista, de modo que
# você tenha uma lista vazia. Mostre sua lista para garantir que você
# realmente tem uma lista vazia no final de seu programa.

names = ['Goes', 'Duda', 'Muwdur']


def convidar():
    for name in names:
        print(f'{name}, quero te convidar para jantar!')


names.insert(0, "Maria")
names.insert(2, "Júlio")
names.append("Cesar")

convidar()

print("---")
print("Infelizmente só terei espaço para duas pessoas!")

while len(names) > 2:
    removido = names.pop()
    print(f"Eu sinto muito {removido}, mas estarei te removendo da lista!")

print("---")
for name in names:
    print(f"Olá {name}, você ainda fará parte da festa!")

del names[0]
del names[0]

print(names)
