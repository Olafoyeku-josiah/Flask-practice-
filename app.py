from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db=SQLAlchemy(app)

class Todo(db.Model):
    id= db.column(db.Integer, primary_key=True)
    content=db.column(db.String(200), nullable=False)
    collected=db.column(db.Integer, default=0)
    date_created=db.column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<task %r>'  %self.id


@app.route('/')
def index():
    return render_template('index.html')




if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)