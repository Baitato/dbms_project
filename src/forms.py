from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField,StringField,PasswordField

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()], render_kw={"placeholder": "Enter the title"})
    content = PageDownField(validators=[DataRequired()], render_kw={"placeholder": "What's on your mind?"})
    tags = StringField('Tags', validators=[DataRequired()], render_kw={"placeholder": "Enter tags separated by commas"})
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = PageDownField("Enter the Content",validators=[DataRequired()],render_kw={"placeholder": "Enter the Comment"})
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Your Username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Your Password"})
    submit = SubmitField('Login')