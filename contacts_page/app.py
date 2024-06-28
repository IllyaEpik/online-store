# імпортуємо модуль flask
import flask 
# створюємо blueprint для contacts_page
contacts= flask.Blueprint(
    name="contacts",
    import_name="app",
    template_folder= "contacts_page/templates",
    static_folder="contacts_page/static",
    static_url_path="/contacts/"
)