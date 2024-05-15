# 8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
#  camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
#  uma camiseta grande e outra média com a mensagem default, e uma camiseta
#  de qualquer tamanho com uma mensagem diferente.

def make_shirt(text="Eu Amo Python", size='G'):
    print("\nO texto a ser utilizado na estampa é: " + text + ".")
    print("O tamanho da camiseta é: " + size + ".")


make_shirt()
make_shirt(size='P')
make_shirt(text="Texto Diferente", size="XL")
