# імпортуємо flask_login
import flask_login
# імпортуємо shop з settings та User з models який знаходиться в registration_page
from .settings import shop
from registration_page.models import User
# указуємо ключ голоного додатку
shop.secret_key = "KEY"
# створюємо екзимпляр классу LoginManager
login_manager = flask_login.LoginManager(app = shop)
# робимо завантаження юзера
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)