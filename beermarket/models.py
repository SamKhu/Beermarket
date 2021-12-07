from beermarket import db

class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    user_name=db.Column(db.String(length=30), nullable=False, unique=True)
    email=db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash=db.Column(db.String(length=60), nullable=False)
    ordered_item_user= db.relationship('Item', backref='ordered_item_user', lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False, unique=True)
    type_beer = db.Column(db.String(length=30), nullable=False)
    barcode = db.Column(db.String(length=100), nullable=False, unique=True)
    vol = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=2000), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Позиция {self.name}'
