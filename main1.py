from flask import *
# from werkzeug import secure_filename
from aim import *
from t_c import *
from flask_sqlalchemy import *
from forms import RegistrationForm, LoginForm,Post_form
from flask_login import LoginManager,UserMixin,login_user,current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.app_context().push()
login_manager =LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)
    image_file =db.Column(db.String(20),default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    # post = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String(120),nullable=False)
    rate= db.Column(db.Integer,nullable=False)
   # bookid = db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"User('{self.booktitle}','{self.rate}')"



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/index.html', methods=['GET', 'POST'])
def againhome():
    return render_template('index.html')


@app.route('/top.html', methods=['GET', 'POST'])
def top():
    a = topbook()
    return render_template('top.html', dic=a)


@app.route('/collab.html', methods=['GET', 'POST'])
def collabs():
    if request.method == 'POST':
        bookName = request.form['bookName']
        try:
            number = int(request.form['number'])
        except:
            return render_template('collab.html',a="Enter valid information")


        if type(recommendBook(bookName,number))==dict:
                collaborative= recommendBook(bookName, number)
                # print("yenar pic")
                return render_template('collre.html', dic=collaborative)

        if type(recommendBook(bookName,number)) ==str:
            collaborative = recommendBook(bookName, number)
            # print("error yenar")
            return render_template('collab.html', a=collaborative)
    # print("same page")
    return render_template('collab.html')




@app.route('/geners.html', methods=['GET', 'POST'])
def genre():
    if request.method=='POST':
        genre=request.form['genre']
        if genre=='fiction':
            dic=category_fiction()
            return render_template('g_result.html', dic=dic)
        if genre=='comics':
            dic=category_Comics()
            return render_template('g_result.html', dic=dic)
        if genre=='drama':
            dic=category_drama()
            return render_template('g_result.html', dic=dic)
        if genre=='romantic':
            dic=category_romantic()
            return render_template('g_result.html', dic=dic)
        if genre=='horror':
            dic=category_horror()
            return render_template('g_result.html', dic=dic)
        if genre=='crime':
            dic=category_crime()
            return render_template('g_result.html', dic=dic)
        if genre=='mystery':
            dic=category_mystery()
            return render_template('g_result.html', dic=dic)
        if genre=='education':
            dic=category_education()
            return render_template('g_result.html', dic=dic)
        if genre=='sports':
            dic=category_sports()
            return render_template('g_result.html', dic=dic)
        if genre=='family':
            dic=category_family()
            return render_template('g_result.html', dic=dic)
        if genre=='food':
            dic=category_food()
            return render_template('g_result.html', dic=dic)
        if genre=='technology':
            dic=category_technology()
            return render_template('g_result.html', dic=dic)
        if genre=='medical':
            dic=category_medical()
            return render_template('g_result.html', dic=dic)
        if genre=='fantasy':
            dic=category_fantasy()
            return render_template('g_result.html', dic=dic)
    return render_template('geners.html')


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=form.password.data
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been create !','successfully')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            return redirect(url_for('top'))
        else:
             flash('login unsuccessful.Please check email and password','danger')
    return render_template('login.html', form=form)

@app.route('/profile.html', methods=['GET', 'POST'])
def profile():
    form = Post_form()
    if form.validate_on_submit():
        detail = Post(booktitle=form.book_name.data, rate=form.rating.data,user_id=form.userid.data)
        db.session.add(detail)
        db.session.commit()
        flash('Data has been submitted !', 'success')
        return redirect(url_for('profile'))
    return  render_template('profile.html',form=form)

@app.route('/about.html', methods=['GET', 'POST'])
def about():


    return  render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
