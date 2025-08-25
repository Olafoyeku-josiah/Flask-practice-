from flask import flask, render_template, url_for
from flask import sqlAlchemy


app=flask(__name__)

@app.route('/')
def index():
    return render_template()




if __name__=="__main_web__":
    app.run(debug=True)