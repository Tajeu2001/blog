from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile,CommentForm,SubscriberForm
from .. models import User,Blog,Comment,Subscriber
from ..email import mail_message
from .. import db


@main.route('/')
def index():
    subscriber_form=SubscriberForm()
    blogs = Blog.query.all()
    title = "blog"
    return render_template('index.html',blogs=blogs,subscriber_form=subscriber_form, title = title)

@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.blog.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('blog.html',form = form ,blog=blog) 



@main.route('/', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,title = subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Hey Welcome To My Personal Blog ","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
    subscriber = Blog.query.all()
    beauty = Blog.query.all()
    return render_template('index.html',subscriber=subscriber,subscriber_form=subscriber_form,beauty=beauty) 

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    return render_template('user.html', user=user, posts=posts)


@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    """ 
    Function to post comments 
    """
    
    form = CommentForm()
    title = 'post comment'
    blog  = Blog.query.filter_by(id=id).first()

    if Blog is None:
        abort(404)

    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion = opinion, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comment()

    return render_template('comment.html', comment_form = form, title = title)
