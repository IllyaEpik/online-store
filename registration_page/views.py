# імпортуємо flask
import flask
# імпортуємо з models клас User
from .models import User
# імпортуємо з settings базу даних
from project.settings import DATABASE
# створюємо функцію render_reg_page
def render_reg_page():
    code  = False
        
    if flask.request.method == "POST":
        print(flask.request.form)
    
        if flask.request.form['password'] == flask.request.form['Password_confirmation']:
            

            user = User(
                login = flask.request.form['login'],
                email = flask.request.form['email'],
                password = flask.request.form['password'],
                is_admin = False
            )

            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                code = "--> authorization"
            except Exception as error:
                return error
    # вертаємо код сторінки
    return flask.render_template(
        template_name_or_list= "reg.html",
        code =  code
    )