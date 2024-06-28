from project.settings import DATABASE
import flask_login
class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    login= DATABASE.Column(DATABASE.String(55))
    email= DATABASE.Column(DATABASE.String(255))
    password =  DATABASE.Column(DATABASE.String(255))
    is_admin = DATABASE.Column(DATABASE.Boolean, nullable = False)
    def __repr__(self) -> str:
        return f"login - {self.login}"
    
class Product(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(60))
    description = DATABASE.Column(DATABASE.Text)
    count = DATABASE.Column(DATABASE.Integer)
    price = DATABASE.Column(DATABASE.Integer)
    discount = DATABASE.Column(DATABASE.Integer)
    capacity1 = DATABASE.Column(DATABASE.String(10), nullable = False)
    capacity2 = DATABASE.Column(DATABASE.String(10), nullable = False)
    capacity3 = DATABASE.Column(DATABASE.String(10), nullable = False)
    def __repr__(self) -> str:
        return f"id - {self.id}"
class Cart(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    user_id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    list_products = DATABASE.Column(DATABASE.Text)
    message_id = DATABASE.Column(DATABASE.Integer)
    chat_id = DATABASE.Column(DATABASE.Integer)
    def __repr__(self) -> str:
        return f"id - {self.id}"