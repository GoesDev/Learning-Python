# 8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
#  tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
#  A função deve exibir uma frase que mostre o tamanho da camiseta e a
#  mensagem estampada.
#  Chame a função uma vez usando argumentos posicionais para criar uma
#  camiseta. Chame a função uma segunda vez usando argumentos nomeados.

def make_shirt(text, size='G'):
    print("\nO texto a ser utilizado na estampa é: " + text + ".")
    print("O tamanho da camiseta é: " + size + ".")


make_shirt(text="Hello World", size='P')
make_shirt(text="Mais uma camiseta saindo!")
