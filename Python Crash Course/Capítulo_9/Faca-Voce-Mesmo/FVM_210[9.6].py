"""9.6 Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer
versão da classe funcionará; basta escolher aquela de que você mais gosta.
Adicione um atributo chamado flavors que armazene uma lista de sabores de
sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
IceCreamStand e chame esse método."""

from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, number_served=0):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = [
            'chocolate',
            'coco',
            'strawberry',
            'lemon'
        ]

    def descibre_flavors(self):
        print(f"Ice creams flavors: {self.flavors}")


sorveteria = IceCreamStand('sorveteria', 'sorvetes')
sorveteria.descibre_flavors()
