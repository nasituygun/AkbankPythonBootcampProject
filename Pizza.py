from abc import ABC, abstractmethod
import csv
from datetime import datetime


class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class BasePizza(Pizza):
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class KlasikPizza(BasePizza):
    def __init__(self):
        super().__init__("Klasik pizza", 15.0)


class MargaritaPizza(BasePizza):
    def __init__(self):
        super().__init__("Margarita pizza", 18.0)


class TurkPizza(BasePizza):
    def __init__(self):
        super().__init__("Türk pizza", 20.0)


class SadePizza(BasePizza):
    def __init__(self):
        super().__init__("Sade pizza", 10.0)


class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza
        self._topping_cost = 0.0

    def get_description(self):
        return self._pizza.get_description()

    def get_cost(self):
        return self._pizza.get_cost() + self._topping_cost


class Zeytin(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Zeytin sosu"
        self._topping_cost = 3.0


class Mantar(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Mantar sosu"
        self._topping_cost = 2.5


class KeciPeyniri(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Keçi peyniri sosu"
        self._topping_cost = 4.0


class Et(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Et sosu"
        self._topping_cost = 5.5


class Sogan(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Soğan sosu"
        self._topping_cost = 2.0


class Misir(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Mısır sosu"
        self._topping_cost = 2.0



def print_menu():
    with open("Menu.txt", "r", encoding="utf-8") as file:
        print(file.read())



def get_topping(topping_choice):
    toppings = {
        11: Zeytin,
        12: Mantar,
        13: KeciPeyniri,
        14: Et,
        15: Sogan,
        16: Misir,
    }
    return toppings.get(topping_choice)


def main():
    print_menu()

    while True:
        try:
            pizza_choice = int(input("Lütfen bir pizza seçeneği seçin (1-4): "))
            if pizza_choice < 1 or pizza_choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
    pizza = None

    if pizza_choice == 1:
        pizza = KlasikPizza()
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = SadePizza()

    while True:
        try:
            topping_choice = int(input("Lütfen bir sos seçeneği seçin (11-16) veya 0'e basarak seçimi tamamlayın: "))
            if topping_choice < 0 or topping_choice > 16:
                raise ValueError
            elif topping_choice == 0:
                break
            topping = get_topping(topping_choice)(pizza)
            pizza = topping
        except ValueError:
            print("Geçersiz bir sos seçeneği girdiniz. Lütfen 0-16 arasında bir sayı girin.")

    print("\nSeçtiğiniz pizza: ", pizza.get_description())
    print("Toplam ücret: ", pizza.get_cost())

    with open("Orders_Database.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        isim = input("Lütfen isminizi giriniz: ")
        tc = input("Lütfen TC kimlik numaranızı giriniz: ")
        kredi_kartı = input("Lütfen kredi kartı numaranızı giriniz: ")
        kredi_kartı_sifre = input("Lütfen kredi kartı şifrenizi giriniz: ")

        writer.writerow([isim, tc, kredi_kartı, kredi_kartı_sifre, pizza.get_description(), pizza.get_cost(),
                         datetime.now().strftime("%d-%m-%Y %H:%M")])

    print("Siparişiniz alındı. Teşekkür ederiz.")

if __name__ == "__main__":
    main()