from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = None
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = request.form.to_dict()
        new_book = Book(title=book['title'], author=book['author'], rating=book['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    
    else:
        return render_template("add.html")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_update = db.get_or_404(Book, book_id)
        book_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    
    book_selected = db.get_or_404(Book, request.args.get('id'))
    return render_template("edit.html", book=book_selected)


@app.route("/delete", methods=['GET'])
def delete():
    book_selected = db.get_or_404(Book, request.args.get('id'))
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()

