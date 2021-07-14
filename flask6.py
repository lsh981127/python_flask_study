from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/<stdName>')
def hello(stdName):
    return '2017112197 이승훈<br>\
           Welcome %s!' %stdName

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        student = request.form['nm']
        return redirect(url_for('hello',stdName = student))
    else:
        student = request.args.get('nm')
        return redirect(url_for('hello', stdName = userName))

if __name__ == '__main__':
    app.run(debug=True)