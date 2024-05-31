from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
from werkzeug.utils import secure_filename
from blueprints.posts.routes import posts_bp
from blueprints.utilities.date_time import datetime_local #, convert_str_to_date
from blueprints.events import events

data = {
    'title': "Northside Chapel",
    'address': "2811 Carey Smith Blvd, Bay City, Texas 77411",
    'date_time': datetime_local()}

current_user = {
    'is_authenticated': True,
    'name': "William"
}

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
# app.config is a dictionary that can be accessed anywhere in the program
# You can also add items to this dictionary

app.register_blueprint(posts_bp, url_prefix="/posts")
# app.register_blueprint()

@app.route("/")
@app.route('/home')
def home():
    print(app.config)
    return render_template('home.html', data=data, current_user=current_user)


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        message = ""
        f = request.files['file']
        fpath = Path('static/images/' + secure_filename(f.filename))  #.absolute()
        if not fpath.exists():
            f.save(fpath)
            message = f"File Saved! ({f.filename})"
        else:
            message = f'File already exists!! ({f.filename})'
            print('*'*45, message)   
        file = {'name': fpath}

        # return render_template("success.html", name = fpath) 
        # instead, do a flash message and go back to input page
        return render_template("upload_file.html", file=file, message=message)
    return render_template('upload_file.html')


@app.route('/dragndrop', methods=['POST', 'GET'])
def dragndrop():
    if request.method == 'POST':
        print("request received" + "*"*30)
        files = request.files.getlist('file')
        for file in files:
            fpath =  Path('static/images/uploads/' + secure_filename(file.filename))  #.absolute()
            file.save(fpath)
        return "success"
    return render_template('dragndrop.html')


if __name__== '__main__':
    app.run(debug=True)

