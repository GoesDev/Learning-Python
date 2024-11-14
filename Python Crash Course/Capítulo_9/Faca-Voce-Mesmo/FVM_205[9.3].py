"""9.3 Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada
ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário."""


class User():

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def descibre(self):
        print(f"User's first name: {self.first_name.title()}")
        print(f"User's last name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()}!")


goes = User('julio', 'cesar')
goes.descibre()
goes.greet_user()
