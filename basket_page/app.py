# імпортуємо модуль flask
import flask 
# створюємо blueprint для basket_page
basket= flask.Blueprint(
    name="basket",
    import_name="app",
    template_folder= "basket_page/templates",
    static_folder="basket_page/static",
    static_url_path="/basket/"
)