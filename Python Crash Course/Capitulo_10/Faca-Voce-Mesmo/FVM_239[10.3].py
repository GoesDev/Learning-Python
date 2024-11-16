"""10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt."""

name = input('Inform your name: ')
file_name = 'Python Crash Course/Capitulo_10/guest.txt'
with open(file_name, 'a') as file_object:
    file_object.write(name.title())
