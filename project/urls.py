import home_app, shop_app

from .settings import project_log

home_app.home.add_url_rule(rule="/", view_func= home_app.show_home_page, methods = ['GET', 'POST'])
project_log.register_blueprint(blueprint= home_app.home)

shop_app.shop.add_url_rule(rule="/shop/", view_func= shop_app.show_shop_page, methods = ['GET', 'POST'])
project_log.register_blueprint(blueprint= shop_app.shop)