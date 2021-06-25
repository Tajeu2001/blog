from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,ValidationError


class BlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators = [Required()])
    post = TextAreaField('Content',validators = [Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Enter your comment:')
    submit = SubmitField('Comment')



