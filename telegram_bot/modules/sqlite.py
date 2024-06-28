import sqlite3
import os
path = os.path.abspath(__file__ + "/../../../project/data.db")
def get_data(columns = "id", table = "user"):
    db = sqlite3.connect(database=path)
    cursor = db.cursor()
    cursor.execute(f"SELECT {columns} FROM {table}")
    return cursor.fetchall()
def edit_data(name_data = "is_admin",data = 1 ,id = 1,table = "user"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    cursor.execute(f"UPDATE {table} SET {name_data} = {data} WHERE id = {id}")
    db.commit()
    db.close()
def add_data(columns = '(name,description,count,price,discount,capacity1,capacity2,capacity3)', values = ('ok','ok',1,1,1,1,1,1), table = "product"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    text = '('
    for count in range(len(values)-1):
        text+= '?,'
    text+='?)'
    cursor.execute(f"INSERT INTO {table} {columns} VALUES {text}", values)
    db.commit()
    db.close()
# add_data()
def counter():
    for count in range(len(get_data())):
        id = get_data()[count][0]
        edit_data(
            name_data="id",
            data= count+1,
            id=id
        )
    # db.commit()
def delete_data(id = 2, table = "user"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id = {id}')
    db.commit()
    db.close()
def add_column(name_column,type_column,name_table="user"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    try:
        cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
        db.commit()
        db.close()
        return "execute"
    except:
        print("Error column")
        return "Error"
# def add()
# def create_tables():
#     db = sqlite3.connect(database= path)
#     cursor = db.cursor()
#     cursor.execute(f"CREATE TABLE IF NOT EXISTS user (INTEGER PRIMARY KEY,id)")
#     # ,login,email,password,is_admin
#     add_column('login','TEXT')
#     add_column('email','TEXT')
#     add_column('password','TEXT')
#     add_column("is_admin","INTEGER")
#     cursor.execute(f"CREATE TABLE IF NOT EXISTS product (INTEGER PRIMARY KEY,id)")
#     add_column('name','TEXT','product')
#     add_column('description','TEXT','product')
#     add_column('count','INTEGER','product')
#     add_column('discount','INTEGER','product')
#     add_column('price','INTEGER','product')
#     add_column('capacity1','TEXT','product')
#     add_column('capacity2','TEXT','product')
#     add_column('capacity3','TEXT','product')
#     # ,name,description,count,price,discount,
#     cursor.execute(f"CREATE TABLE IF NOT EXISTS cart ()")
#     add_column('user_id','INTEGER','cart')
#     add_column('list_products','TEXT','cart')
#     add_column('message_id','INTEGER','cart')
#     add_column('chat_id','INTEGER','cart')
#     db.commit()
#     db.close()
# create_tables()
print(get_data(columns="id",table="product"))
