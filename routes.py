from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import current_user
from models import db, User, tweets
from forms import SignupForm, LoginForm,tweetform

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/tweeter'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    print("-----------------")
    print(session)
    return redirect(url_for('home'))
    

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.username.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data 
        return redirect(url_for('home'))
      else:
        return redirect(url_for('home'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  print("****************")
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/home", methods=["GET", "POST"])
def home():
 
  form = tweetform()
  newtweet = tweets(form.body.data, form.timestamp.data)
  print(newtweet)
  db.session.add(newtweet)
  db.session.commit()
  if form.validate_on_submit():
       
        return redirect(url_for('home'))  
  
  #posts = tweets.query.order_by(tweets.timestamp.desc()).all()
  tweet = tweets.query.all()

  return render_template('home.html', tweet=tweet, form=form)





if __name__ == "__main__":
  app.run(debug=True)