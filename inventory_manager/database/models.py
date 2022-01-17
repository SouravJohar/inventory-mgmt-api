from datetime import datetime

from database import db


class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, default="")

    category = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, category, quantity, price, description=None):
        self.name = name
        self.category = category

        if quantity < 0:
            quantity = 0

        if price < 0:
            price = 0

        if description is None:
            description = ""

        self.quantity = quantity
        self.price = price
        self.description = description

    def __repr__(self):
        return "[self.name, self.category, self.quantity, self.price, self.description]"

    def to_list(self):
        return [self.name, self.category, self.quantity, self.price, self.description]

    def get_headers(self):
        return ["name", "category", "quantity", "price", "description"]
