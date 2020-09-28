from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,ValidationError
from  ..models import Subscriber


class BlogForm(FlaskForm):
    category=TextAreaField('Post your Blog', validators = [Required()])
    title = TextAreaField('Your name',validators = [Required()])
    content = TextAreaField('blog',validators = [Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')


class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    title = StringField('Entre Your Name' ,validators=[Required()])
    submit = SubmitField('Subscribe')    

    def validate_email(self,data_field):
                if Subscriber.query.filter_by(email =data_field.data).first():
                    raise ValidationError('There is an account with that email')    


# class ContentForm(FlaskForm):
#    content = TextAreaField('YOUR PITCH')
#    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
   comment = TextAreaField('WRITE COMMENT')
   submit = SubmitField('SUBMIT')




