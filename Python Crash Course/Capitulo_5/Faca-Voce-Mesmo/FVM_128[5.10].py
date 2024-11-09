# 5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
# que simule o modo como os sites garantem que todos tenham um nome de
# usuário único.
# • Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
# • Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
# que um ou dois dos novos usuários também estejam na lista current_users.
# • Percorra a lista new_users com um laço para ver se cada novo nome de
# usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando
# que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi
# usado, apresente uma mensagem dizendo que o nome do usuário está
# disponível.
# • Certifique-se de que sua comparação não levará em conta as diferenças
# entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
# ser aceito.

current_users = ['Munthar', 'Extôpos', 'Maene', 'Turif', 'Muwdur']
new_users = ['Galgudir', 'Kamys', 'Noafha', 'Welka', 'Muwdur']

for user in new_users:
    if user.title() in current_users:
        print(f'{user.title()} já está em uso, por favor tente outro nome.')
    else:
        print(f'{user.title()} é um nome válido.')
