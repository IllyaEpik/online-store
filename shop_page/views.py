import flask
import flask_login
import os
from project.settings import DATABASE
from registration_page.models import User, Product
from .app import shop
dict_types={
    "IMG":"IMG",
    "NAME":"TEXT",
    "PRICE":"INT",
    "DISCOUNT": "INT"
}
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
                

                print(flask.request.form["send"])

                # print(os.path.abspath(__file__+"/../static/image"))
                print(path)
                img = flask.request.files.get('data')
                print(img.filename, 11)
                if img.filename != "":
                    try:
                        os.remove(path)
                    except:
                        pass
                    img.save(path)
                print(img, type(img))
                # image = Image.open(img)
                # print(image, type(image))
                # image.show()
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
                    # list_products = Product.query.all()
                    # for product in Product.query.all():
                    #     Product.query.filter_by(id = product.id).delete()
                    # print(124)
                    # for product_data in list_products:
                    #     name = product_data.name
                    #     count = product_data.count
                    #     price = product_data.price
                    #     discount = product_data.discount
                    #     print(name,price,discount, count)
                    #     if product_data.id == int(id):
                    #         if type1 == "NAME":

                    #             name = text
                    #         elif type1 == "PRICE":
                    #             price = flask.request.form['data']
                    #         elif type1 == "DISCOUNT":
                    #             discount = flask.request.form['data']
                            
                    #         # print(123)
                    #     # print(126)
                    #     product  = Product(
                    #         name= name ,
                    #         description =product_data.description,
                    #         count = count,
                    #         price = price,
                    #         discount = discount
                    #     )
                    #     DATABASE.session.add(product)
                    # print(125)
                    DATABASE.session.commit()
            # elif dict_types[type1] == "INT":
            #     try:

            #     except:
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
                        print(product)
                except:
                    
                    
                    pass
            mod = True
    try:
        count =  len(flask.request.cookies.get('products').split(" "))
        if flask.request.cookies.get('products').split(" ")[0]== "":
            count = "0"
    except:
        count = "0"
    # if flask.request.method == "POST":
        # count = str(int(count) + 1)
    print(Product)
    # if len(Product.query.all()) == 0:
    #     path_excel=os.path.abspath(__file__ + "/../static/xlsx/Product.xlsx")
    #     read_excel = pandas.read_excel(io=path_excel,header=None,names=["name", "description","count","price","discount"])
    #     for row in read_excel.iterrows():
    #         row_excel = row[1]
    #         product  = Product(
    #             name= row_excel["name"],
    #             description =row_excel["description"],
    #             count = row_excel["count"],
    #             price = row_excel["price"],
    #             discount = row_excel["discount"],
    #             capacity1 = "256 Гб",
    #             capacity2 = "512 Гб",
    #             capacity3 = "1 Тб"
    #         )
    #         DATABASE.session.add(product)
    #     DATABASE.session.commit()
            
    # products = {
        
    # }
    
    # print(cookie_get)
    print(User.query.count(),User.query.all(),type(User.query.all()))
    # for product in User.query.all():
    # if count == None:
    #     count = '0'
    # list_admins=["Illya","Mykola Skrypnik"]
    print()
    admin=flask_login.current_user.is_admin
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
    # cookie.set_cookie("all", count)
    
    return cookie