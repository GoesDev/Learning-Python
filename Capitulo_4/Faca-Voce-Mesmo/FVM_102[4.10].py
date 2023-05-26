# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
# acrescente várias linhas no final do programa que façam o seguinte:• Exiba a
# mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
# exibir os três primeiros itens da lista desse programa.
# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para
# exibir três itens do meio da lista.

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'bread']
print(f'Os três primeiros itens da lista são: {my_foods[:3]}')
print(f'Os três itens do meio da lista são: {my_foods[1:4]}')
print(f'Os três últimos itens da lista são: {my_foods[-3:]}')
