from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']     #객체에서 파일 가져와서 원하는 위치에 저장
        f.save(secure_filename(f.filename))
        return 'file uploades successfully'
if __name__ = '__main__':
    app.run(debug = True)
    
