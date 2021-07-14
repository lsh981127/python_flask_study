from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/dongguk')
def hello_dongguk():
    return 'hello dongguk univ'

@app.route('/student/<stdname')
def hello_student(stdname):
    return 'hello %s' %stdname

@app.route('/user/<username>')
def hello_user(username):
    if username == 'dongguk':
        return redirect(url_for('hello_dongguk'))
    else:
        return redirect(url_for('hello_student', stdname = username))

if __name__ = '__main__':
    app.run(debug=True)