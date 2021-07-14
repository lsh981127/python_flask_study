from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

app.secret_key = 'software_engineering'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '<p>2017112197 이승훈</p> Logged in as ' + username + '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"
    return "<p>2017112197 이승훈 </p> You are not logged in <br><a href = '/login'></b>" + \
        "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <p>2017112197 이승훈</p>
    <form action = "" method = "post">
        <p><input type = text name = username></p>
        <p><input type = submit value = Login></p>
    </form>
    '''

@app.route('/logout')
def logout():      #username session에 있으면 없애는것
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)
