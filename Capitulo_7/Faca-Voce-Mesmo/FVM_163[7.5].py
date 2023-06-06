# 7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
# de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
# ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
# dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
# informe-lhes o preço do ingresso do cinema.
active = True

while active:
    age = int(input("(digite '0' para sair)\nDigite sua idade: "))
    if age < 3 and age > 0:
        print("Seu igresso é gratuito!")
    elif age >= 3 and age < 12:
        print("Seu ingresso custa 10 dolares!")
    elif age >= 12:
        print("Seu ingresso custa 15 dolares!")
    elif age == 0:
        active = False
