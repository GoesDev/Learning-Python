# 7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
# os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
# finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
# mostre uma mensagem para cada pedido, por exemplo, Preparei seu
# sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
# para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
# prontos, mostre uma mensagem que liste cada sanduíche preparado.

sandwich_orders = ['americano', 'bauru', 'misto quente']
finished_sandwiches = []

for sandwich in sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print(f"Iremos preparar seu {prepared_sandwich.title()}")
    finished_sandwiches.append(prepared_sandwich)

for sandwich in finished_sandwiches:
    print(f"Seu {sandwich.title()} está pronto.")
