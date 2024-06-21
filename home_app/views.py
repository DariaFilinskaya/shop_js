import flask
from shop_app.models import Product
from project.settings import db
import os

def show_home_page():
  if flask.request.method == "POST":
    product = Product(
      name = flask.request.form['name']
    )
    db.session.add(product)
    db.session.commit()

    image = flask.request.files['image']
    image.save(os.path.abspath(__file__ + f"/../../shop_app/static/images/{product.name}.png"))
  return flask.render_template(template_name_or_list="home.html", products = Product.query.all())