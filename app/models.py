from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))


    def __repr__(self):
        return f'User{self.username}'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date = db.Column(db.Date)

    def __repr__(self):
        return f'Blog{self.title}'