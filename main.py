# OOP

class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: ${self.price}")

    @staticmethod
    def from_input():
        print("Введіть інформацію про автомобіль:")
        model = input("Модель: ")
        year = int(input("Рік випуску: "))
        manufacturer = input("Виробник: ")
        engine_volume = float(input("Об'єм двигуна (л): "))
        color = input("Колір: ")
        price = float(input("Ціна ($): "))
        return Car(model, year, manufacturer, engine_volume, color, price)

    def update_price(self, new_price):
        self.price = new_price
        print(f"Ціна оновлена до: ${self.price}")

    def repaint(self, new_color):
        self.color = new_color
        print(f"Колір оновлено до: {self.color}")

#car = Car("Hyundai Sonata", 2020, "Hyundai", 2.0, "Білий", 25000)

car = Car.from_input()

car.display_info()

car.update_price(18500)

car.repaint("білий перлапутр")

car.display_info()

#########

class Book:
    def __init__(self, name, year, publisher, genre, author, price ):
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

book = Book.from_input()

book.display_info()

book.update_price(15.99)

book.display_info()

book1 = Book("Гаррі Поттер і Філософський камінь", 1997, "Bloomsbury", "Фентезі", "Дж. К. Ролінґ", 20.00)
book2 = Book("Володар перснів: Братство персня", 1954, "Allen & Unwin", "Фентезі", "Дж. Р. Р. Толкін", 25.00)

result = book1.compare_price(book2)
print(result)

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
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

stadium = Stadium.from_input()

stadium.display_info()

stadium.update_capacity(60000)

if stadium.is_large_stadium():
    print(f"{stadium.name} є великим стадіоном.")
else:
    print(f"{stadium.name} не є великим стадіоном.")








