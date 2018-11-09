from datetime import datetime
from flask_login import UserMixin
from marketplace import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), nullable=True)
    created_on = db.Column(db.DateTime, nullable=True)
    login = db.Column(db.String(100) , unique=True)
    email = db.Column(db.String(100) , unique=True)
    password = db.Column(db.String(255))

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return "\nUsers(user_id='{self.user_id}',\n" \
               "\t\t name='{self.name}')\n"\
               "\t\t phone='{self.phone}')\n".format(self=self)

class Category(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    href = db.Column(db.String, nullable=True, unique=True)

    def __repr__(self):
        return "\nCategory(name='{self.name}',\n" \
               "\t\t href='{self.href}')".format(self=self)


class Advert(db.Model):
    advert_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    href = db.Column(db.String(255), nullable=True, unique=True)
    description = db.Column(db.String(255))
    '''
    mark = db.Column(db.String(100))
    model = db.Column(db.String(100))
    country = db.Column(db.String(100))
    material = db.Column(db.String(100))
    temple_length = db.Column(db.Integer)
    lens_width = db.Column(db.Integer)
    bridge = db.Column(db.Integer)
    purchase_price = db.Column(db.Integer)
    sale_price = db.Column(db.Integer)
    status = db.Column(db.String(100))

    #price = Column(Integer)
    #category_id = Column(Integer, ForeignKey('categories.id'))
    #user_id = Column(Integer, ForeignKey('users.user_id'))
    '''
    def __repr__(self):
        return "\nAdvert(advert_id='{self.advert_id}',\n" \
               "\t\t title='{self.title}')\n"\
               "\t\t href='{self.href}')\n"\
               "\t\t href='{self.mark}')\n"\
               "\t\t href='{self.model}')\n"\
               "\t\t href='{self.country}')\n"\
               "\t\t href='{self.material}')\n"\
               "\t\t href='{self.temple_length}')\n"\
               "\t\t href='{self.lens_width}')\n"\
               "\t\t href='{self.bridge}')\n"\
               "\t\t href='{self.purchase_price}')\n"\
               "\t\t href='{self.sale_price}')\n"\
               "\t\t href='{self.status}')\n".format(self=self)

