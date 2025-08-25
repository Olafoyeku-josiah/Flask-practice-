from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db=SQLAlchemy(app)

class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    collected=db.Column(db.Integer, default=0)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    with app.app_context():
        db.create_all()

    def __repr__(self):
        return '<task %r>'  %self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=="POST":
        current_task=request.form['content']
        new_task=Todo(content=current_task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue with adding a task "
    else: 
        tasks= Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting that tasks"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method=="POST":
        task.content=request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue updating the tasks"
    else:
        return render_template('index.html', tasks=task)

if __name__=="__main__":
    app.run(debug=True)