from project.settings import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f"name: {self.name}"