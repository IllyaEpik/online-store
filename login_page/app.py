# імпортуємо модуль flask
import flask
# створюємо blueprint для login_page
login =  flask.Blueprint(
    name="login",
    import_name="app",
    template_folder="login_page/templates",
    static_folder= "login_page/static",
    static_url_path=  '/login/'
)