import flask
import flask_login
from registration_page.models import User, Product
import os
import pandas
from project.settings import DATABASE
def render_basket_page():
    try:
        count =  len(flask.request.cookies.get('products').split(" ")) # python + flask get
    except:
        count = "0"
    # if flask.request.method == "POST":
        # count = str(int(count) + 1)
    if len(list(Product.query.all())) == 0:
        path_excel=os.path.abspath(__file__ + "/../../shop_page/static/xlsx/Product.xlsx")
        read_excel = pandas.read_excel(io=path_excel,header=None,names=["name", "description","count","price"])
        for row in read_excel.iterrows():
            row_excel = row[1]
            product  = Product(
                name= row_excel["name"],
                description =row_excel["description"],
                count = row_excel["count"],
                price = row_excel["price"] 
            )
            DATABASE.session.add(product)
        DATABASE.session.commit()
                   
    # products = {
        
    # }
    
    # print(cookie_get)
    print(User.query.count(),User.query.all(),type(User.query.all()))
    # for product in User.query.all():
    # if count == None:
    #     count = '0'
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="basket.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                            #   count = count
                              ))
    return cookie