from application import app, db
from application.models import Tasks
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    return render_template('index.html', title="Home", all_tasks=all_tasks)

@app.route('/create')
def create():
    new_task = Tasks(desc="New Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Added task {new_task.id} to database"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks":[]}
    for task in all_tasks:
        tasks_dict["tasks"].append({"description": task.desc, "completed": task.completed})
    
    return tasks_dict

@app.route('/update/<int:id>/<new_desc>')
def update(id, new_desc):
    task = Tasks.query.get(id)
    task.desc = new_desc
    db.session.commit()
    return f"Task {id} updated to {new_desc}"

@app.route('/delete/<int:id>')
def delete(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} has been deleted."

@app.route('/complete/<int:id>')
def completed(id):
    task = Tasks.query.get(id)
    task.completed = True
    db.session.commit()
    return f"Task {id} has been updated to completed."

@app.route('/incomplete/<int:id>')
def incompleted(id):
    task = Tasks.query.get(id)
    task.completed = False
    db.session.commit()
    return f"Task {id} has been updated to incomplete."