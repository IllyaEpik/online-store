# імпортуємо модуль flask
import flask 
# створюємо blueprint для shop_page
shop= flask.Blueprint(
    name="shop",
    import_name="app",
    template_folder= "shop_page/templates",
    static_folder="shop_page/static",
    static_url_path="/shop/"
)