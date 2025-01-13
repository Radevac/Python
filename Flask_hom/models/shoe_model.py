class Shoe:
    def __init__(self, gender, type, color, price, manufacturer, size):
        self.gender = gender
        self.type = type
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def to_dict(self):
        return {
            "gender": self.gender,
            "type": self.type,
            "color": self.color,
            "price": self.price,
            "manufacturer": self.manufacturer,
            "size": self.size
        }
