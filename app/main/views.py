from flask import redirect, render_template, url_for, flash
from .. import db
from ..models import Blog, Comments, Subscribe
from ..email import mail_message
from .forms import BlogForm, CommentForm, SubscribedUserForm
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

        flash("Your Subscription is successful")

        return redirect(url_for('main.index'))

    return render_template('index.html', subform = form)



@main.route('/homepage')
def homepage():

    '''
    View root page function that returns the index page and its data
    '''
    blog = Blog.query.all()
    return render_template('homepage.html', blog=blog)




@main.route('/blog/', methods = ["GET","POST"])
def postblog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(title=blog_form.title.data, description=blog_form.description.data,postedby= blog_form.postedby.data, date=blog_form.date.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('.homepage'))

    return render_template('blog.html', blog_form= blog_form)




@main.route('/commentform/', methods = ["GET","POST"])
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(comment=form.comment.data,madeby=form.madeby.data, dateposted=form.dateposted.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.homepage'))

    return render_template('commentform.html',form= form)
