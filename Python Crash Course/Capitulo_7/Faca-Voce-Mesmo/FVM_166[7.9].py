# 7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
# que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
# Acrescente um código próximo ao início de seu programa para exibir uma
# mensagem informando que a lanchonete está sem pastrami e, então, use um
# laço while para remover todas as ocorrências de 'pastrami' e
# sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
# finished_sandwiches.

sandwich_orders = ['bauru', 'pastrami', 'misto quente', 'americano', 'bauru']
finished_sandwiches = []

print("Estamos sem Pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print(f"Iremos preparar seu {prepared_sandwich.title()}")
    finished_sandwiches.append(prepared_sandwich)

for sandwich in finished_sandwiches:
    print(f"Seu {sandwich.title()} está pronto.")
