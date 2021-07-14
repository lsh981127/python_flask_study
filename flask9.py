from flask import Flask, render_template
app = Flask(__name__)

@app.route('/score')
def score():
    dict = { 'SH' : 80, 'WS' : 90, 'UH' : 100}
    return render_template('score.html', result = dict)

if __name__ = '__main__':
    app.run(debug = True)