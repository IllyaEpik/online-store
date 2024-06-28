# імпортуємо flask
import flask
# імпортуємо flask_login
import flask_login
# створюємо функцію render_contacts_page
def render_contacts_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" ")) # python + flask get
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    # возвращаемо код html сторінки
    return flask.render_template(template_name_or_list="contacts.html",name=flask_login.current_user.login,count=count)