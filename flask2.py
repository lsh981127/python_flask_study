from flask import Flask
app = Flask(__name__)

@app.route('/hello/')
def hello_ice():
    return '2017112197 이승훈<br>\
           Hello ICE Students!'

if __name__ == '__main__':
    app.run(debug=True)