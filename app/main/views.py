from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile,CommentForm
from .. models import User,Post,Comment
from ..email import mail_message
from .. import db


@main.route('/')
def index():
    posts = Post.query.all()
    title = "post"
    return render_template('index.html',posts=posts, title = title)

@main.route('/new/post', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_post = Post(title = form.title.data, content = form.post.data, user=current_user)
        new_post.save_post()
        post = Post.query.filter_by(title=new_post.title).first()
        return redirect(url_for('main.index'))
    
    return render_template('new_blog.html',form = form) 

@main.route('/article/<int:id>', methods = ['GET', 'POST'])
def post(id):

    post = Post.query.filter_by(id=id).first()
    title = post.title
    form = CommentForm()
    comments = Comment.get_comments(id)

    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data, user=current_user, post=post)
        if new_comment.comment:
            new_comment.save_comment()
        return redirect(request.referrer)

    return render_template('blog.html', title=title, post=post)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    return render_template('user.html', user=user, posts=posts)



