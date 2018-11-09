from flask import render_template, url_for, redirect
from flask_security import login_required
from flask_login import current_user, LoginManager, login_user, logout_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from marketplace import app
from marketplace.models import db, User, Category, Advert, Item


login = LoginManager(app)

categories_names_query = db.session.query(Category).all()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

admin = Admin(app, name='Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())

admin.add_view(MyModelView(Category, db.session))
admin.add_view(MyModelView(Advert, db.session))
admin.add_view(MyModelView(User, db.session))

@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return 'Logged in'

@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'


@app.route('/')
@app.route('/home')
@app.route('/home/')
def home():
    item_list = list()
    num = 0
    '''
        for category in db.session.query(Category).all():
        category_list.append(category.name)
        category_number += 1
        if category_number > 10:
            break
    '''
    #session = db.create_session()
    for item in db.session.query(Item).all():
        num += 1
        item_list.append({'title': item.title, 'description': item.description, 'id': num,
                          'item_id': item.item_id, 'price': item.price})
    db.session.close()

    #return render_template('list.html', category=category_list, advert=advert_list)
    return render_template('home_new.html', items=item_list, title='Все', categories=categories_names_query)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/home/<int:post_id>')
def show_post(post_id):
    item_post_id = db.session.query(Item).filter(Item.id == post_id).first()
    return render_template('card_new.html', item=item_post_id, title='Выбранная оправа')


@app.route('/home/cat_<int:category>')
def show_category(category):
    category_query = db.session.query(Category).filter_by(id=category).first()
    return render_template('home_new.html', items=category_query.items, title=category_query.name, categories=categories_names_query)
