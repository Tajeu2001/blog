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
        post = Post(title = form.title.data, content = form.post.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('post.html',form = form ,post=post) 




@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    
    return render_template('user.html', user=user, posts=posts)


# @main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
# @login_required
# def post_comment(id):
#     """ 
#     Function to post comments 
#     """
    
#     form = CommentForm()
#     title = 'post comment'
#     post  = Post.query.filter_by(id=id).first()

#     if Post is None:
#         abort(404)

#     if form.validate_on_submit():
#         opinion = form.opinion.data
#         new_comment = Comments(opinion = opinion, user_id = current_user.id, pitches_id = pitches.id)
#         new_comment.save_comment()

#     return render_template('comment.html', comment_form = form, title = title)
