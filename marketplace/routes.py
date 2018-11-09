from flask import render_template, url_for, redirect
from flask_security import login_required
from flask_login import current_user, LoginManager, login_user, logout_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from marketplace import app
from marketplace.models import db, User, Category, Advert


login = LoginManager(app)


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
def home():
    advert_list = list()
    num = 0
    '''
        for category in db.session.query(Category).all():
        category_list.append(category.name)
        category_number += 1
        if category_number > 10:
            break
    '''
    #session = db.create_session()
    for advert in db.session.query(Advert).all():
        num += 1
        advert_list.append({'title': advert.title, 'description': advert.description, 'id': num})
    db.session.close()

    #return render_template('list.html', category=category_list, advert=advert_list)
    return render_template('home_new.html', advert=advert_list)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/home/<int:post_id>')
def show_post(post_id):
    advert_item = dict()
    num = 0
    for advert in db.session.query(Advert).all():
        num += 1
        if num == post_id:
            advert_item = {'title': advert.title, 'description': advert.description, 'id': num}
    return render_template('card.html', advert=advert_item, title='Объявление №{}'.format(post_id))
