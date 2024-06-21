import flask
from .models import Product

def show_shop_page():
  return flask.render_template(template_name_or_list="shop.html", products = Product.query.all())