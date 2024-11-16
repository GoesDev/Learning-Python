"""9.3 Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada
ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário."""


class User():

    def __init__(self, first_name, last_name, login_attempts=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def descibre(self):
        print(f"User's first name: {self.first_name.title()}")
        print(f"User's last name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


goes = User('julio', 'cesar')
goes.descibre()
goes.greet_user()
goes.increment_login_attempts()
goes.increment_login_attempts()
goes.increment_login_attempts()
goes.increment_login_attempts()
print(goes.login_attempts)
goes.reset_login_attempts()
print(goes.login_attempts)
