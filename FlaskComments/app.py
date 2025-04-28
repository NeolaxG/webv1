from flask import Flask, render_template, request, redirect, url_for
from model import db, User
from flask_login import login_user, LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwer1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_users.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    try:
        with open('comments.txt', 'r') as file:
            comments_list = [line.strip()
                             for line in file.readlines()]
    except FileNotFoundError:
        comments_list = []
    return render_template('home.html', title='Home page', comments = comments_list)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/comments', methods=['GET'])
def comments():
    return render_template('comments.html')

@app.route('/add_comments', methods=['POST'])
def add_comments():
    comment = request.form['comments']
    try:
        with open('comments.txt', 'a') as file:
            file.write(comment + '\n')
        return f'Ваш комментарий успешно сохранен. Комментарий: {comment}'
    except Exception as e:
        return f'Ошибка записи комментария {e}'

@app.route('/user/<username>')
def user_profile(username):
    return f'Username: {username}'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
