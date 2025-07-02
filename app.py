from flask import Flask, request, render_template, redirect, url_for
from forms import LoginForm, SignupForm
from config import Config
from mongoDB import insert_tester, find_tester
import os

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        register = form.register.data
        
        if register == Config.TESTER_REGIST:
            insert_tester(username, password)
            return redirect(url_for('login'))
        else:
            return render_template('signup.html', form=form, show_alert=True)
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if find_tester(username, password): # username == 'ServerTest' password == 'password4Tester'
            return redirect(url_for('database'))

    return render_template('login.html', form=form, agian=True if request.method == 'POST' else False)
    
@app.route('/database')
def database():
    return render_template('database.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 读取 Render 提供的端口
    app.run(host='0.0.0.0', port=port)
