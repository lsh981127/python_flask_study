from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/setcookie', methods =['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['username']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('username',user)

    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('username')
    return '<h1> welcomd' +name+ '!</h1>'

if __name__ == '__main__':
    app.run(debug = True)