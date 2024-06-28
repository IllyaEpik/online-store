# імпортуємо flask
import flask 
# імпортуємо flask_login
import flask_login
# ствоюємо функцію render_home_page
def render_home_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" ")) # python + flask get
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    code=False
    if flask_login.current_user.is_authenticated:
        code=flask_login.current_user.login
    print(code)
    # возвращаемо код html сторінки
    return flask.render_template(
        template_name_or_list= "home.html", 
        code=code,
        count=count
    )