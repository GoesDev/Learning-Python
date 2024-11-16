"""10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
acrescente uma linha que registre a visita do usuário em um arquivo chamado
guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
arquivo.
"""

file_name = 'Python Crash Course/Capitulo_10/guest_book.txt'
cond = 0

while cond < 3:
    name = input("Hello! Whats is your name: ")
    with open(file_name, 'a') as file_object:
        file_object.write(name.title() + ".\n")
    cond += 1
