# 3.6 Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados
# para o jantar.
# > Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
#   uma instrução print no final do seu programa  informando às pessoas que
#   você encontrou uma mesa de jantar maior.
# > Utilize insert() para adicionar um novo convidado no início de sua lista.
# > Utilize insert() para adicionar um novo convidado no meio de sua lista.
# > Utilize append() para adicionar um novo convidado no final de sua lista.
# > Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
#   que está em sua lista.

names = ['Goes', 'Duda', 'Muwdur']


def convidar():
    for name in names:
        print(f'{name}, quero te convidar para jantar!')


convidar()

print("Encontrei uma mesa de jantar maior! Poderei convidar mais pessoas!")
print("---")

names.insert(0, "Maria")
names.insert(2, "Júlio")
names.append("Cesar")

convidar()
