# імпортуємо flask_mail
import flask_mail
# імпортуємо з settings shop та базу даних
from .settings import shop,DATABASE
# вказуемо пошту адміністратора
ADMINISTRATION_ADRESS = "artemvaschenko83@gmail.com"
# вказуємо пароль від пошти адміністратора
ADMINISTRATION_PASSWORD = "sncj nczy toqt atlm"

# налаштовуємо mail головного додатку
shop.config["MAIL_SERVER"] = 'smtp.gmail.com'
shop.config["MAIL_PORT"] = 587
shop.config["MAIL_USE_TLS"] = True
shop.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
shop.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
# создаємо єкземпляр классу Mail
mail = flask_mail.Mail(app=shop)