import telebot
try:
    from .modules.sqlite import get_data, edit_data, delete_data, add_data
except:
    from modules.sqlite import get_data, edit_data, delete_data, add_data
import threading
import os

user_button = telebot.types.InlineKeyboardButton(text= "GET USERS", callback_data="GET")
product_button1= telebot.types.InlineKeyboardButton(text= "GET PRODUCTS", callback_data="PRODUCT")
product_button2= telebot.types.InlineKeyboardButton(text= "ADD PRODUCT", callback_data="ADD")
cart_button = telebot.types.InlineKeyboardButton(text= "GET USER", callback_data="cart")
# inline_button4 = telebot.types.InlineKeyboardButton(text= "GET ADMIN", callback_data="ADMIN")
user_keyboard=telebot.types.InlineKeyboardMarkup([[user_button]])
product_keyboard= telebot.types.InlineKeyboardMarkup([[product_button1,product_button2]])
cart_keyboard = telebot.types.InlineKeyboardMarkup([[cart_button]])

bot = telebot.TeleBot('6669027800:AAH0Cj4rJmqArmz5RAsVd0fMfS9uX-XrIFA')
stage = {}
# list_moderators = [{"id": 2036291862, "name": "Illya"}]
list_id={
    "users":4,
    "cart":9,
    "products":11
}
global_id = -1002210480484
@bot.message_handler(["start"])
def start(message: telebot.types.Message):
    # is_moderator = False
    id  = message.chat.id
    thread_id= message.message_thread_id
    print(id)
    # bot.send_message(chat_id=global_id , text= f"{thread_id}" )
    # bot.send_message(chat_id=global_id , text= f"use",message_thread_id=4)
    # bot.send_message(chat_id=global_id , text= f"pro",message_thread_id=11)    
    # bot.send_message(chat_id=global_id , text= f"cart",message_thread_id=9)
    if id == global_id:
        if thread_id==list_id["users"]:
            bot.send_message(chat_id=id , text= "Привет користувач" , reply_markup=user_keyboard, message_thread_id=thread_id)
        elif thread_id==list_id["products"]:
            bot.send_message(chat_id=id , text= "Привет користувач" , reply_markup=product_keyboard, message_thread_id=thread_id)
    # for moderator in list_moderators:
    #     if moderator["id"]== id:
    #         is_moderator = True
    #         break  
    # if is_moderator:

    #     bot.send_message(chat_id=id , text= "Привет користувач " , reply_markup=inline_keyboard)
    # else:
    #     bot.send_message(chat_id=id , text="Hello" )
    # bot.send_message(chat_id=message.chat.id, text="Bomjour", reply_markup= inline_keyboard)
# @bot.register_next_step_handler()
# def next(message: telebot.types.Message):
#     bot.send_message(chat_id=message.chat.id, text="Hello")
# @bot.callback_query_handler(lambda call: True if call.data == "1" else False)
# def callbacks(callback: telebot.types.CallbackQuery):
#     id  = callback.message.chat.id
#     is_moderator = False
#     for moderator in list_moderators:
#         if moderator["id"]== id:
#             is_moderator = True
#             break  
    
#     print(callback.message.chat.id)
@bot.callback_query_handler(lambda call: True if "DELETE" in call.data and not "P" in call.data  else False)
def delete(callback: telebot.types.CallbackQuery):
    # data - DELETE_2
    id = callback.data.split("_")[-1]
    delete_data(id=id)
    bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
@bot.callback_query_handler(lambda call: True if call.data == "GET" else False)
def callbacks(callback: telebot.types.CallbackQuery):
    for count in range(len(get_data("id"))):
        inline_button1=telebot.types.InlineKeyboardButton(text= "DELETE USER", callback_data= f"DELETE_{get_data('id')[count][0]}")
        inline_keyboard1 =  telebot.types.InlineKeyboardMarkup([[inline_button1]])
        if get_data('is_admin')[count][0] == 1:
            inline_button2=telebot.types.InlineKeyboardButton(text= "REMOVE ADMIN", callback_data=f"REMOVE_{get_data('id')[count][0]}")
            inline_keyboard1 =  telebot.types.InlineKeyboardMarkup([[inline_button1, inline_button2]])
        else:
            inline_button4 = telebot.types.InlineKeyboardButton(text= "GET ADMIN", callback_data=f"GET_{get_data('id')[count][0]}")
            inline_keyboard1 =  telebot.types.InlineKeyboardMarkup([[inline_button1, inline_button4]])
        text = f"ID: {get_data('id')[count][0]}\n"
        text+= f"Login: {get_data('login')[count][0]}\n"
        text+= f"Password: {get_data('password')[count][0]}\n"
        text += f"Is_admin: {bool(get_data('is_admin')[count][0])}\n"
        bot.send_message(chat_id=callback.message.chat.id, text=text, reply_markup=inline_keyboard1,message_thread_id=list_id["users"])


@bot.callback_query_handler(lambda call: True if "GET" in call.data and call.data!= "GET"  or "REMOVE" in call.data else False)
def admin(callback: telebot.types.CallbackQuery):
    id = int(callback.data.split("_")[-1])
    value =int( get_data('is_admin')[id-1][0])
    edit = lambda: f"REMOVE_{id}" if not value else f"GET_{id}"
    edit2 = lambda: "REMOVE ADMIN" if not value else "GET ADMIN"
    inline_keyboard2 = callback.message.reply_markup.keyboard
    inline_keyboard2[0][1].text = edit2()

    inline_keyboard2 = telebot.types.InlineKeyboardMarkup(inline_keyboard2)
    text = callback.message.text
    text = text.split("min: ")
    text[-1] = str(not value)
    text = "min: ".join(text)
    bot.edit_message_text(text,chat_id=callback.message.chat.id,message_id= callback.message.message_id, reply_markup= inline_keyboard2) 
    edit_data(id=id, data= not value)
@bot.callback_query_handler(lambda call: True if call.data=="PRODUCT" else False)
def product(callback: telebot.types.CallbackQuery):
    for count in range(len(get_data("id","product"))):

        product1=get_data("*","product")[count]
        print(product1,product1[0])
        text=f"name: {product1[1]}\n"
        text+=f"count: {product1[3]}\n"
        text+=f"price: {product1[4]}\n"
        text+=f"discount: {product1[5]}\n\n"
        text+=f"description: {product1[2]}\n"
        product_button3= telebot.types.InlineKeyboardButton(text= "DELETE PRODUCT", callback_data=f"DELETE_PRODUCT_{product1[0]}")
        product_get_keyboard= telebot.types.InlineKeyboardMarkup([[product_button3]])
        # path = 
        with open(os.path.abspath(__file__ + f"/../../shop_page/static/image/{product1[1]}.png"), "rb") as file:
            bot.send_photo(global_id,file,text,reply_markup=product_get_keyboard, message_thread_id=list_id["products"])
        # bot.send_message(chat_id=global_id, message_thread_id=list_id["products"],text=text,reply_markup=product_get_keyboard)
def add_production(message:telebot.types.Message):
    id = bot.get_me().id
    old_data=stage[id]
    try:
        
        stage[id]["messages"].append(message.message_id)
        if stage[id]["name"] == None:
            stage[id]["name"] = message.text
            stage[id]["messages"].append(bot.send_message(message.chat.id,"Укажіть ціну продукту", message_thread_id=list_id["products"]).message_id)
        elif stage[id]["price"] == None:
            stage[id]["price"] = int(message.text)
            stage[id]["messages"].append(bot.send_message(message.chat.id,"Укажіть скидку продукту", message_thread_id=list_id["products"]).message_id)
        elif stage[id]["discount"] == None:
            stage[id]["discount"] = int(message.text)
            stage[id]["messages"].append(bot.send_message(message.chat.id,"Укажіть кількість продукту", message_thread_id=list_id["products"]).message_id)
        elif stage[id]["count"] == None :
            stage[id]["count"] = int(message.text)
            stage[id]["messages"].append(bot.send_message(message.chat.id,"Укажіть опис продукту", message_thread_id=list_id["products"]).message_id)
        elif stage[id]["description"] == None:
            stage[id]["description"] = message.text
            stage[id]["messages"].append(bot.send_message(message.chat.id,"Укажіть фото продукту",message_thread_id=list_id["products"]).message_id)
        else:
            stage[id]["image"] = message.photo[-1].file_id
            file=bot.get_file(stage[id]["image"])
            download_file=bot.download_file(file.file_path)
            path = os.path.abspath(__file__+f"/../../shop_page/static/image/{stage[id]['name']}.png")
            with open(path,"wb") as save_file:
                save_file.write(download_file)
            add_data(values=(
                stage[id]["name"],
                stage[id]["description"],
                stage[id]["count"],
                stage[id]["price"],
                stage[id]["discount"],
                "256 Гб",
                "512 Гб",
                "1 Тб"
            ))
            text="Продукт успішно добавлений до бази данних, продукт:\n"
            text+=f"name: {stage[id]['name']}\n"
            text+=f"count: {stage[id]['count']}\n"
            text+=f"price: {stage[id]['price']}\n"
            text+=f"discount: {stage[id]['discount']}\n"
            text+=f"description: {stage[id]['description']}\n"
            # bot.send_message(message.chat.id,)
            for message1 in stage[id]["messages"]:
                try:
                    bot.delete_message(message.chat.id,message1)
                except:
                    pass
            bot.send_photo(message.chat.id,stage[id]["image"],text,message_thread_id=list_id["products"])
        bot.register_next_step_handler(message=message, callback=add_production)
    except Exception as error:
        print(stage[id],error)
        stage[id]["messages"].append(bot.send_message(message.chat.id,"Виникла помилка можливо ви неправильно вказали данні",message_thread_id=list_id["products"]).message_id)
        bot.register_next_step_handler(message=message, callback=add_production)
        stage[id]["price"]=None
        stage[id]["count"]=None
        stage[id]["discount"]=None
@bot.callback_query_handler(lambda call: True if call.data=="ADD" else False)
def add_product(callback: telebot.types.CallbackQuery):
    id = bot.get_me().id
   
    stage[id]={
        "name":None,
        "price":None,            
        "discount":None,
        "count":None,
        "description":None,
        "messages":[]
        }
    stage[id]["messages"].append(bot.send_message(global_id,"Укажіть ім'я продукту",message_thread_id=list_id["products"]).message_id)
    def ok(ok):
        print('ok')
    bot.register_next_step_handler(message=callback.message,callback=add_production)
@bot.callback_query_handler(lambda call: True if "DELETE_PRODUCT" in call.data else False)
def delete_product(callback: telebot.types.CallbackQuery):
    print(callback.data)
    id = callback.data.split("_")[-1]
    delete_data(id=id,table="product")
    bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
@bot.callback_query_handler(lambda call: True if "cart" in call.data else False)
def get_user(callback: telebot.types.CallbackQuery):
    print(callback.from_user.username)
    
    edit_data('message_id',bot.send_message(callback.from_user.id,callback.message.text).message_id,callback.data.split('_')[-1],table='Cart')
    edit_data('chat_id',callback.from_user.id,callback.data.split('_')[-1],table='Cart')
    bot.delete_message(chat_id=callback.message.chat.id, message_id= callback.message.message_id)
# bot.infinity_polling()

threading.Thread(target=lambda: bot.infinity_polling(skip_pending=True)).start()