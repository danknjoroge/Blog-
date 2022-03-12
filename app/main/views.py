from flask import redirect, render_template, url_for
from .. import db
from ..models import Subscribe
from ..email import mail_message
from .forms import SubscribedUserForm
from . import main
from flask_login import login_required


# Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     return render_template('index.html')


@main.route('/', methods = ["GET","POST"])
def index():
    form = SubscribedUserForm()
    if form.validate_on_submit():
        subscribe = Subscribe(email = form.email.data, username = form.username.data)
        db.session.add(subscribe)
        db.session.commit()
        mail_message("Welcome to bloglist","email/subscribe",subscribe.email,user=subscribe)
        return redirect(url_for('main.index'))

    return render_template('index.html', subform = form)