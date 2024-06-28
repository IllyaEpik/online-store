import flask
from .models import User
from project.settings import DATABASE
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
    return flask.render_template(
        template_name_or_list= "reg.html",
        code =  code
    )