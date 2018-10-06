from flask import Flask, render_template
from avito_db_entities import Category, Advert
import avito_db as db

app = Flask(__name__)


@app.route('/list')
def c_list():
    category_number = 0
    category_list = list()
    advert_list = list()
    for category in db.session.query(Category).all():
        category_list.append(category.name)
        category_number += 1
        if category_number > 10:
            break
    for advert in db.session.query(Advert).all():
        advert_list.append({'title': advert.title, 'description': advert.description})
    return render_template('list.html', category=category_list, advert=advert_list)


if __name__ == '__main__':
    app.run()
