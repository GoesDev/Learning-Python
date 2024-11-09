# 7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
# quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
# oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
# contrário, informe que sua mesa está pronta.

number = int(input("Quantas pessoas estão em seu grupo? "))

if number > 8:
    print("Vocês deverão aguardar uma mesa.")
else:
    print("A mesa de vocês está pronta.")
