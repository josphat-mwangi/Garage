from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    name = TextAreaField("write the name of Garage ")
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Submit')
