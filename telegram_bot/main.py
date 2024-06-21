import telebot
from .modules.sqlite import get_data, edit_data, delete_data
import threading

user_button = telebot.types.InlineKeyboardButton(text= "GET USERS", callback_data="GET")
product_button1= telebot.types.InlineKeyboardButton(text= "GET PRODUCTS", callback_data="PRODUCT")
product_button2= telebot.types.InlineKeyboardButton(text= "ADD PRODUCT", callback_data="ADD")
product_button3= telebot.types.InlineKeyboardButton(text= "DELETE PRODUCT", callback_data="DELETE_PRODUCT")
# inline_button4 = telebot.types.InlineKeyboardButton(text= "GET ADMIN", callback_data="ADMIN")
user_keyboard=telebot.types.InlineKeyboardMarkup([[user_button]])
product_keyboard= telebot.types.InlineKeyboardMarkup([[product_button1,product_button2]])
product_get_keyboard= telebot.types.InlineKeyboardMarkup([[product_button3]])
bot = telebot.TeleBot('6669027800:AAH0Cj4rJmqArmz5RAsVd0fMfS9uX-XrIFA')
# list_moderators = [{"id": 2036291862, "name": "Illya"}]
list_id={
    "users":-4288720099,
    "cart":-4212396407,
    "products":-4277182455
}
@bot.message_handler(["start"])
def start(message: telebot.types.Message):
    # is_moderator = False
    id  = message.chat.id
    # print(id)
    if id==list_id["users"]:
        bot.send_message(chat_id=id , text= "Привет користувач" , reply_markup=user_keyboard)
    elif id==list_id["products"]:
        bot.send_message(chat_id=id , text= "Привет користувач" , reply_markup=product_keyboard)

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
@bot.callback_query_handler(lambda call: True if "DELETE" in call.data else False)
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
        bot.send_message(chat_id=callback.message.chat.id, text=text, reply_markup=inline_keyboard1)


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
        print(product1)
        text=f"name: {product1[1]}\n"
        text+=f"count: {product1[3]}\n"
        text+=f"price: {product1[4]}\n"
        text+=f"discount: {product1[5]}\n\n"
        text+=f"description: {product1[2]}\n"
        bot.send_message(chat_id=list_id["products"],text=text,reply_markup=product_get_keyboard)
threading.Thread(target=lambda: bot.infinity_polling(skip_pending=True)).start()
# bot.infinity_polling()