# імпортуємо модуль flask
import flask
# створюємо blueprint для regitration_page
reg =  flask.Blueprint(
    name="reg",
    import_name="app",
    template_folder="registration_page/templates",
    static_folder= "registration_page/static",
    static_url_path=  '/reg/'
)