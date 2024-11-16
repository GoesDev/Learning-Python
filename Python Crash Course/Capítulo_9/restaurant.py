"""9.1 Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e
cuisine_type. Crie um método chamado describe_restaurant() que mostre
essas duas informações, e um método de nome open_restaurant() que exiba
uma mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os
dois atributos individualmente e, em seguida, chame os dois métodos.
"""


class Restaurant():

    def __init__(self, name, cuisine_type, number_served=0):

        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def descibre_restaurant(self):
        print(f"Restaurant's name: {self.name}")
        print(f"Resaurant's cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


my_restaurant = Restaurant('Bar do Giba', 'Boteco')
print(my_restaurant.number_served)
my_restaurant.set_number_served(15)
my_restaurant.increment_number_served(15)
print(my_restaurant.number_served)
