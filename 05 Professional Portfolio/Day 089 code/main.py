from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Optional
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b' # Change this for production
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    due_date: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[int] = mapped_column(Integer, nullable=False)

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()])
    description = TextAreaField('Task Description', validators=[Optional()])
    due_date = DateField("Task Due Date", validators=[Optional()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    result = db.session.execute(db.select(Task))
    all_tasks = result.scalars().all()
    db.session.commit()
    return render_template("index.html", tasks=all_tasks)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            name = form.name.data,
            description = form.description.data,
            due_date = str(form.due_date.data),
            completed = 0
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template('add.html', form=form)

@app.route('/delete')
def delete_task():
    task_id = request.args.get("id")
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/change')
def change_task():
    task_id = request.args.get("id")
    task = db.get_or_404(Task, task_id)
    task.completed = int(not bool(task.completed))
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/edit', methods=['GET', 'POST'])
def edit_task():
    task_id = request.args.get("id")
    task = db.get_or_404(Task, task_id)
    form = TaskForm()
    
    if form.validate_on_submit():
        task.name = form.name.data
        task.description = form.description.data
        task.due_date = str(form.due_date.data)
        db.session.commit()
        return redirect(url_for("home"))
    
    form.name.data = task.name
    form.description.data = task.description
    if task.due_date != "None":
        form.due_date.data = datetime.strptime(task.due_date, "%Y-%m-%d").date()
        
    return render_template('edit.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
