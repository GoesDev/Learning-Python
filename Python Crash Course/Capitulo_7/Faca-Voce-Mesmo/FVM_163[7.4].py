# 7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
# fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
# fornecido. À medida que cada ingrediente é especificado, apresente uma
# mensagem informando que você acrescentará esse ingrediente à pizza.

active = True

while active:
    print("Digite 'quit' para sair")
    ingrediente = input("Digite um ingrediente a ser adicionado à pizza: ")
    if ingrediente == 'quit':
        active = False
    else:
        print(f"{ingrediente} será adicionado à pizza!")
