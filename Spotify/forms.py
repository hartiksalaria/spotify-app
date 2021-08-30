from wtforms import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class SongLink(Form):
    song_link = StringField("song_link", validators=[Required()])
    submit = SubmitField("submit")