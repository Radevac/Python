from flask import Blueprint, jsonify, request
from controllers.shoe_controller import ShoeController
from models.shoe_model import Shoe

shoe_views = Blueprint('shoe_views', __name__)
controller = ShoeController()

@shoe_views.route('/shoes', methods=['POST'])
def add_shoe():
    data = request.json
    shoe = Shoe(
        gender=data['gender'],
        type=data['type'],
        color=data['color'],
        price=data['price'],
        manufacturer=data['manufacturer'],
        size=data['size']
    )
    controller.add_shoe(shoe)
    return jsonify({"message": "Shoe added successfully"}), 201

@shoe_views.route('/shoes', methods=['GET'])
def get_all_shoes():
    shoes = controller.get_all_shoes()
    return jsonify([shoe.to_dict() for shoe in shoes]), 200

@shoe_views.route('/shoes/<gender>', methods=['GET'])
def get_shoes_by_gender(gender):
    shoes = controller.find_shoes_by_gender(gender)
    return jsonify([shoe.to_dict() for shoe in shoes]), 200
