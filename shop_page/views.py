# імпортуємо flask
import flask
# імпортуємо flask_login
import flask_login
# імпортуємо os
import os
# імпортуємо DATABASE з project
from project.settings import DATABASE
# імпортуємо class Product з models
from registration_page.models import Product
dict_types={
    "IMG":"IMG",
    "NAME":"TEXT",
    "PRICE":"INT",
    "DISCOUNT": "INT"
}
# створюємо функцію render_shop_page
def render_shop_page():
    mod = False
    type1 = None
    id = None
    if flask.request.method == "POST":
        try:
            flask.request.form["send"].split(";")[1]
            print('heloo2323')
            type1 = flask.request.form["send"].split(";")[1]

            if type1 == "IMG":
                id = int(flask.request.form["send"].split(";")[0])
                path= os.path.abspath(__file__ + "/../static/image/"+ Product.query.all()[id-1].name+ ".png") 

                img = flask.request.files.get('data')
                if img.filename != "":
                    try:
                        os.remove(path)
                    except:
                        pass
                    img.save(path)
                os.rename
            elif dict_types[type1] == "TEXT" or dict_types[type1] == "INT":
                next = True
                text = flask.request.form['data']
                if dict_types[type1] == "INT":
                    try:
                        int(text)
                    except:
                        next = False
                if text != "" and next:
                    id = flask.request.form["send"].split(";")[0]
                    if type1 == "NAME":
                        path1 = os.path.abspath(__file__ + "/../static/image/"+Product.query.get(id).name+ ".png")
                        path2 = os.path.abspath(__file__ + "/../static/image/"+text+ ".png")
                        Product.query.get(id).name = text
                        os.rename(path1,path2)
                    if type1 == "PRICE":
                        Product.query.get(id).price = text
                    if type1 == "DISCOUNT":
                        Product.query.get(id).discount = text
                        DATABASE.session.commit()
                        DATABASE.session.commit()
        except Exception as Error:
            print(Error)
            try:
                print('hello')
                id =flask.request.form['delete']
                product = Product.query.get(id)
                DATABASE.session.delete(product)
                DATABASE.session.commit()
                os.remove(os.path.abspath(__file__ + "/../static/image/"+product.name+ ".png"))
            except:
                try:
                    flask.request.form['add_product']
                    product =  Product(
                        name= flask.request.form["name"],
                        description =flask.request.form["description"],
                        count = flask.request.form["count"],
                        price = flask.request.form["price"],
                        discount = flask.request.form["discount"],
                        capacity1 = "256 Гб",
                        capacity2 = "512 Гб",
                        capacity3 = "1 Тб"
                    )
                    next = True
                    for product_data in Product.query.all():
                        if product.name == product_data.name:
                            next = False
                    if next:
                        flask.request.files["image"].save(os.path.abspath(__file__ + "/../static/image/"+product.name+ ".png"))
                        DATABASE.session.add(product)
                        DATABASE.session.commit()
                except:
                    
                    
                    pass
            mod = True
    try:
        count =  len(flask.request.cookies.get('products').split(" "))
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    DATABASE.session.commit()
    admin=flask_login.current_user.is_admin
    # возвращаемо код html сторінки
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="shop.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                              count = count,
                              int = int,
                              admin =admin,
                              type = type1,
                              mod = mod,
                              id = id
                              ))
    
    return cookie