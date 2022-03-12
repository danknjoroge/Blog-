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



