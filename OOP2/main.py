# OOP2

# class Car:
#     def __init__(self, model="Unknown", year=0, manufacturer="Unknown", engine_volume=0.0, color="Unknown", price=0.0):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_volume = engine_volume
#         self.color = color
#         self.price = price
#
#     def display_info(self):
#         print(f"Модель: {self.model}")
#         print(f"Рік випуску: {self.year}")
#         print(f"Виробник: {self.manufacturer}")
#         print(f"Об'єм двигуна: {self.engine_volume} л")
#         print(f"Колір: {self.color}")
#         print(f"Ціна: ${self.price}")
#
#     @staticmethod
#     def from_input():
#         print("Введіть інформацію про автомобіль:")
#         model = input("Модель: ")
#         year = int(input("Рік випуску: "))
#         manufacturer = input("Виробник: ")
#         engine_volume = float(input("Об'єм двигуна (л): "))
#         color = input("Колір: ")
#         price = float(input("Ціна ($): "))
#         return Car(model, year, manufacturer, engine_volume, color, price)
#
#     def update_price(self, new_price):
#         self.price = new_price
#         print(f"Ціна оновлена до: ${self.price}")
#
#     def repaint(self, new_color):
#         self.color = new_color
#         print(f"Колір оновлено до: {self.color}")
#
#     def __str__(self):
#         return f"{self.manufacturer} {self.model} ({self.year}), Ціна: ${self.price}"
#
#     def __eq__(self, other):
#         return isinstance(other, Car) and self.model == other.model and self.year == other.year
#
#
# # Створення об'єктів поза межами класу
# car1 = Car("Hyundai Sonata", 2020, "Hyundai", 2.0, "Білий", 25000)
# car2 = Car("Toyota Corolla", 2020, "Toyota", 1.8, "Чорний", 20000)
# car3 = Car("Hyundai Sonata", 2020, "Hyundai", 2.0, "Сірий", 24000)
#
# #__str__
# print(car1)
# print(car2)
#
# # __eq__
# print(car1 == car2)
# print(car1 == car3)

#####

class Book:
    def __init__(self, name="Unknown", year=0, publisher="Unknown", genre="Unknown", author="Unknown", price=0.0):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Назва книги: {self.name}")
        print(f"Рік видання: {self.year}")
        print(f"Видавництво: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: ${self.price}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Ціна оновлена до: ${self.price}")

    @staticmethod
    def from_input():
        print("Введіть інформацію про книгу:")
        name = input("Назва книги: ")
        year = int(input("Рік видання: "))
        publisher = input("Видавництво: ")
        genre = input("Жанр: ")
        author = input("Автор: ")
        price = float(input("Ціна ($): "))
        return Book(name, year, publisher, genre, author, price)

    def compare_price(self, other_book):
        if self.price > other_book.price:
            return f"{self.name} дорожча за {other_book.name}."
        elif self.price < other_book.price:
            return f"{self.name} дешевша за {other_book.name}."
        else:
            return f"{self.name} і {other_book.name} мають однакову ціну."

    def __str__(self):
        return f"\"{self.name}\" by {self.author}, Ціна: ${self.price}"

    def __eq__(self, other):
        return isinstance(other, Book) and self.name == other.name and self.author == other.author


book1 = Book("Гаррі Поттер і Філософський камінь", 1997, "Bloomsbury", "Фентезі", "Дж. К. Ролінґ", 20.00)
book2 = Book("Володар перснів: Братство персня", 1954, "Allen & Unwin", "Фентезі", "Дж. Р. Р. Толкін", 25.00)
book3 = Book("Гаррі Поттер і Філософський камінь", 1997, "Bloomsbury", "Фентезі", "Дж. К. Ролінґ", 22.00)

#  __str__
print(book1)
print(book2)

#  __eq__
print(book1 == book2)
print(book1 == book3)

#####

class Stadium:
    def __init__(self, name="Unknown", opening_date="Unknown", country="Unknown", city="Unknown", capacity=0):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} глядачів")

    @staticmethod
    def from_input():
        print("Введіть інформацію про стадіон:")
        name = input("Назва стадіону: ")
        opening_date = input("Дата відкриття (дд.мм.рррр): ")
        country = input("Країна: ")
        city = input("Місто: ")
        capacity = int(input("Місткість (кількість місць): "))
        return Stadium(name, opening_date, country, city, capacity)

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"Місткість оновлена до: {self.capacity} глядачів")

    def is_large_stadium(self):
        return self.capacity > 50000

    def __str__(self):
        return f"Стадіон {self.name}, {self.city}, Місткість: {self.capacity} глядачів"

    def __eq__(self, other):
        return isinstance(other, Stadium) and self.name == other.name and self.city == other.city


stadium1 = Stadium("Camp Nou", "24.09.1957", "Іспанія", "Барселона", 99354)
stadium2 = Stadium("Santiago Bernabéu", "14.12.1947", "Іспанія", "Мадрид", 81044)
stadium3 = Stadium("Camp Nou", "24.09.1957", "Іспанія", "Барселона", 100000)

#  __str__
print(stadium1)
print(stadium2)

# __eq__
print(stadium1 == stadium2)
print(stadium1 == stadium3)




