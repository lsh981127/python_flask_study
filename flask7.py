from flask import Flask, render_template
app = Flask(__name__)

@app.route('/class/<classname>')
def hello_class(classname):
    return render_template('class.html', name = classname)

if __name__ = '__main__':
    app.run(debug=True)
    