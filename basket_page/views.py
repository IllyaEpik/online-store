# імпортуємо flask
import flask
# імпортуємо flask_login
import flask_login
# імпортуємо class Product Cart User з models
from registration_page.models import Cart, Product, User
# імпортуємо Message з flask_mail
from flask_mail import Message
# імпортуємо mail, ADMINISTRATION_ADRESS,DATABASE з mail_config
from project.mail_config import mail, ADMINISTRATION_ADRESS,DATABASE
# ствоюємо функцію render_basket_page
def render_basket_page():
    send=False
    print(2132113)
    if flask.request.method == "POST":
        print(flask.request.form)
        if flask.request.form.get('name'):
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
                
                cart = Cart(
                    id = len(Cart.query.all()),
                    user_id = flask_login.current_user.id,
                    list_products = flask.request.cookies.get('products'),
                    chat_id = telegram_bot.global_id,
                    message_id = telegram_bot.bot.send_message(
                        telegram_bot.global_id,
                        text=text,
                        message_thread_id=telegram_bot.list_id["cart"],
                        reply_markup=telegram_bot.telebot.types.InlineKeyboardMarkup([[telegram_bot.telebot.types.InlineKeyboardButton(text='get user',callback_data=f'cart_{len(Cart.query.all())}')]])
                        ).message_id
                )
                DATABASE.session.add(cart)
                DATABASE.session.commit()
                send = True
            except Exception as error :
                print(error)
            try:
                text=f"До вас звернувся користувач сайту:\n"
                text+= f"ім'я: {flask.request.form['name']}\n"
                text+= f"призвище: {flask.request.form['surname']}\n"
                text+= f"номер телефону: {flask.request.form['phone']}\n"
                text+= f"електрона пошта: {flask.request.form['email']}\n"
                text+= f"місто отримувача: {flask.request.form['city']}\n"
                text+= f"Відділення нової почти: {flask.request.form['post']}\n"
                text+= f"додаткові побажання: {flask.request.form['add']}\n"
                message = Message(
                    "Message Order",
                    sender= ADMINISTRATION_ADRESS, 
                    recipients= ['epi99k@gmail.com'], 
                    body= text
                )
                mail.send(message)
                send = True
            except Exception as error:
                print(error)
        else:
            try:
                import telegram_bot
                carts = Cart.query.all()
                for cart1 in carts:
                    if cart1.user_id == flask_login.current_user.id:
                        message = Message(
                            "Message Order",
                            sender= ADMINISTRATION_ADRESS, 
                            recipients= ['epi99k@gmail.com'], 
                            body= f'користувач {flask_login.current_user.login} скасував замовлення'
                        )
                        mail.send(message)
                        send = False
                        telegram_bot.bot.delete_message(chat_id=cart1.chat_id,message_id=cart1.message_id)
                        DATABASE.session.delete(cart1)
                        DATABASE.session.commit()
            except Exception as error:
                print(error)
    try:
        count =  flask.request.cookies.get('products').split(" ") 
    except:
        count = "0"
    print(Cart.query.all())
    for cart1 in Cart.query.all():
        if cart1.user_id == flask_login.current_user.id:
            send = True
    list_count = {}
    for product1 in Product.query.all():
        list_count[str(product1.id)] = str(count.count(str(product1.id)))
        print(type(product1.id))
    # возвращаемо код html сторінки
    cookie = flask.make_response(
        flask.render_template(template_name_or_list="basket.html",
                              name=flask_login.current_user.login, 
                              products = Product.query.all(),
                              cookie = list_count,
                              count = len(count),
                              send = send
                              ))
    return cookie