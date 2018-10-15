from flask import Flask, render_template
from avito_db_entities import Category, Advert
import avito_db as db

app = Flask(__name__)


@app.route('/list')
def c_list():
    category_number = 0
    category_list = list()
    advert_list = list()
    num = 0
    for category in db.session.query(Category).all():
        category_list.append(category.name)
        category_number += 1
        if category_number > 10:
            break
    for advert in db.session.query(Advert).all():
        num += 1
        advert_list.append({'title': advert.title, 'description': advert.description, 'id': num})
    db.session.close()
    return render_template('list.html', category=category_list, advert=advert_list)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    advert_item = dict()
    num = 0
    for advert in db.session.query(Advert).all():
            num += 1
            if num == post_id:
                advert_item = {'title': advert.title, 'description': advert.description, 'id': num}
    db.session.close()
    return render_template('card.html', advert=advert_item)


if __name__ == '__main__':
    app.run()
