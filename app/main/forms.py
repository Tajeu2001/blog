from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,ValidationError


class BlogForm(FlaskForm):
    title = TextAreaField('Your name',validators = [Required()])
    content = TextAreaField('post',validators = [Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')



