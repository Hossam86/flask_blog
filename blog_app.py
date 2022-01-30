from flask import Flask, render_template, request, make_response
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
from wtforms.validators import DataRequired
# Initlization application instance
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
# Routes and viewfunctions

# config
app.config['SECRET_KEY']='bd778a7ba38c685220464a94'

# Forms
class NameForm(FlaskForm):
    name= StringField(label="Name",validators=[DataRequired(),])
    submit=SubmitField(label="Submit")

# application root url
@app.route('/',methods=['POST', 'GET'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template("index.html", current_time=datetime.utcnow(), form=form, name=name)

# dynamics routing
@app.route('/user/<name>')
def profile_page(name):
    return render_template('user.html', name=name)

# the request- repoponse cycle
# application and request context
  
@app.route('/client')
def client_agent():
    user_agent= request.headers["User-Agent"]
    response=make_response("this document carries cookie")
    response.set_cookie('answer','42')
    return response

@app.errorhandler(404)
def page_not_found (e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
