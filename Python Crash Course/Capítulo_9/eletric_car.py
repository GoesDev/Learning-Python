from car import Car


class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Exibe uma frase sobre a distância que o carro é capaz de
        percorrer com essa bateria"""
        if self.battery_size == 70:
            miles_range = 240
        elif self.battery_size == 85:
            miles_range = 270

        message = "This car can go approximately " + str(miles_range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos"""

    def __init__(self, make, model, year) -> None:
        """Inicializa os atributos da classe-pai"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Carros elétricos não tem tanques de gasolina."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
