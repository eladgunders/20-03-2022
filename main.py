from flask import Flask, redirect, render_template, request, url_for, session


pw = '12345678'


app = Flask(__name__)
app.secret_key = 'not protected'

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for("user"))
        return render_template('login.html')
    if request.method == 'POST':
        if request.form['txt_password'] == pw:
            user = request.form['txt_name']
            session['user'] = user
            return redirect(url_for("user"))
        else:
            return redirect(url_for("login_failed"))

@app.route("/login_failed", methods=['GET', 'POST'])
def login_failed():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for("user"))
        return render_template('login_failed.html')
    if request.method == 'POST':
        if request.form['txt_password'] == pw:
            user = request.form['txt_name']
            session['user'] = user
            return redirect(url_for("user"))
        else:
            return render_template('login_failed.html')

@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        return f'<h1>Hello {user}!</h1><p><a href="http://127.0.0.1:5000/logout"><button>Log Out</button></a></p>'   
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for("login"))

 
if __name__ == '__main__':
    app.run(debug=True)