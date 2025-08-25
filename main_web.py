from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


main_web=Flask(__name__)
main_web.config['SQLALCHEMY_DATABASE_URL']='sqlite:///test.db'

db=SQLAlchemy(main_web)

class Todo(db.model):
    id= db.column(db.integer,primary_key=True)
    content=db.column(db.string(200), nullable=False)
    collected=db.column(db.integer, default=0)
    date_created=db.column(db.integer, default=datetime.utcnow)

    def __repr__(self):
        return '<task %r>'  %self.id


@main_web.route('/')
def index():
    return render_template('index.html')




if __name__=="__main_web__":
    with main_web.app_context():
        db.create_all()
    main_web.run(debug=True)