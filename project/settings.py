# імпортуємо модуль flask
import flask 
# імпортуємо модулыі flask_sqlalchemy та flask_migrate
import flask_sqlalchemy, flask_migrate
# імпортуємо модуль os 
import os
# створюємо головний додаток
shop = flask.Flask(
    import_name= "settings",
    instance_path=   os.path.abspath(__file__ + "/.."),
    template_folder= "project/templates"
)
# підключаємо базу даних
shop.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
DATABASE  = flask_sqlalchemy.SQLAlchemy(app=shop)
MIGRATE = flask_migrate.Migrate(app=shop , db= DATABASE)