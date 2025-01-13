from models.shoe_model import Shoe

class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def get_all_shoes(self):
        return self.shoes

    def find_shoes_by_gender(self, gender):
        return [shoe for shoe in self.shoes if shoe.gender == gender]
