# 4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos
# básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
# • Use um laço for para exibir cada prato oferecido pelo restaurante.
# • Tente modificar um dos itens e cerifique-se de que Python rejeita a
# mudança.
# • O restaurante muda seu cardápio, substituindo dois dos itens com pratos
# diferentes. Acrescente um bloco de código que reescreva a tupla e, em
# seguida, use um laço for para exibir cada um dos itens do cardápio
# revisado.

foods = ('arroz', 'feijão', 'salada', 'batata frita', 'farofa')

for food in foods:
    print(food.title())

print('---')
# foods[1] = 'Queijo'

new_foods = ('arroz', 'feijão', 'sobremesa', 'batata frita', 'batata palha')

foods = new_foods

for food in foods:
    print(food.title())
