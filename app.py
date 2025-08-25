from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///test.db'

db=SQLAlchemy(app)

class Todo(db.model):
    id= db.column(db.integer,primary_key=True)
    content=db.column(db.string(200), nullable=False)
    collected=db.column(db.integer, default=0)
    date_created=db.column(db.integer, default=datetime.utcnow)

    def __repr__(self):
        return '<task %r>'  %self.id


@app.route('/')
def index():
    return render_template('index.html')




if __name__=="__main_web__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)