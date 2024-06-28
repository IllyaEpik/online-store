import basket_page.app
import basket_page.views
from registration_page import reg,render_reg_page
from home_page import home,render_home_page
from login_page import login,render_login_page
import shop_page, shop_page.app, shop_page.views
from .settings import shop
import basket_page
import contacts_page, contacts_page.app, contacts_page.views
home.add_url_rule(rule="/",view_func= render_home_page, methods = ['GET', 'POST'])
login.add_url_rule(rule= "/login/",view_func=render_login_page, methods=["GET","POST"])
reg.add_url_rule(rule="/reg/",view_func=render_reg_page, methods=["GET","POST"] )
basket_page.app.basket.add_url_rule(rule="/basket/",view_func=basket_page.views.render_basket_page,methods = ["GET","POST"] )
shop_page.app.shop.add_url_rule(rule="/shop/",view_func= shop_page.views.render_shop_page, methods = ['GET', 'POST'])
contacts_page.app.contacts.add_url_rule(rule="/contacts/",view_func=contacts_page.views.render_contacts_page,methods = ["GET","POST"] )

shop.register_blueprint(blueprint=shop_page.app.shop)
shop.register_blueprint(blueprint= basket_page.app.basket)
shop.register_blueprint(blueprint= contacts_page.app.contacts)
shop.register_blueprint(blueprint= home)
shop.register_blueprint(blueprint= reg)
shop.register_blueprint(blueprint= login)
