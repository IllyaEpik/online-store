import flask
import flask_login
from registration_page.models import Cart, Product
import os

import pandas
from project.settings import DATABASE
def render_basket_page():
    send=False
    if flask.request.method == "POST":
        try:
            import telegram_bot
            text=f"До вас звернувся користувач сайту:\n"
            text+= f"ім'я: {flask.request.form['name']}\n"
            text+= f"призвище: {flask.request.form['surname']}\n"
            text+= f"номер телефону: {flask.request.form['phone']}\n"
            text+= f"електрона пошта: {flask.request.form['email']}\n"
            text+= f"місто отримувача: {flask.request.form['city']}\n"
            text+= f"Відділення нової почти: {flask.request.form['post']}\n"
            text+= f"додаткові побажання: {flask.request.form['add']}\n"
            # name=flask.request.form["name"] {flask.request.form['name']} {flask.request.form['surname']}
            # surname=flask.request.form["surname"]
            phone=flask.request.form["phone"]
            email=flask.request.form["email"]
            city=flask.request.form["city"]
            post=flask.request.form["post"]
            add=flask.request.form["add"]
            telegram_bot.bot.send_message(
                telegram_bot.global_id,
                text=text,
                message_thread_id=telegram_bot.list_id["cart"],
                reply_markup=telegram_bot.cart_keyboard
                )
            send=True
            cart = Cart(
                user_id = flask_login.current_user,
                list_products = flask.request.cookies.get('products')
            )
        except:
            pass
        
    try:
        count =  flask.request.cookies.get('products').split(" ") # python + flask get
    except:
        count = "0"
    # if flask.request.method == "POST":
        # count = str(int(count) + 1)
    list_count = {}
    if len(list(Product.query.all())) == 0:
        path_excel=os.path.abspath(__file__ + "/../../shop_page/static/xlsx/Product.xlsx")
        read_excel = pandas.read_excel(io=path_excel,header=None,names=["name", "description","count","price", "discount"])
        for row in read_excel.iterrows():
            row_excel = row[1]
            product  = Product(
                name= row_excel["name"],
                description =row_excel["description"],
                count = row_excel["count"],
                price = row_excel["price"],
                discount = row_excel["discount"]
            )
            
            DATABASE.session.add(product)
        DATABASE.session.commit()
    for product1 in Product.query.all():
        # print(product1.id)
        list_count[str(product1.id)] = str(count.count(str(product1.id)))
        print(type(product1.id))
    # products = {
        
    # }
    
    # print(count.count("1"))
    # print(cookie_get)
    # print(User.query.count(),User.query.all(),type(User.query.all()))
    # for product in User.query.all():
    # if count == None:
    #     count = '0'
    
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="basket.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                              cookie = list_count,
                              count = len(count),
                              send = send
                            #   count = count
                              ))
    return cookie