# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
# em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador
# ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o
# jogador ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o
# jogador ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja
# exibida para a cor apropriada do alienígena.

def alien_color(color):
    if color == 'green':
        print("Você acaba de ganhar 5 pontos!")
    elif color == 'yellow':
        print("Você acaba de ganhar 10 pontos!")
    elif color == 'red':
        print("Você acaba de ganhar 15 pontos!")


alien_color('green')
alien_color('red')
alien_color('yellow')
