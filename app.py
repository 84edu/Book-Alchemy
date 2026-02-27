from docutils.nodes import authors
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from data_models import db, Author, Book
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('APP_KEY')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == "POST":
        name = request.form["name"]
        birthdate_string = request.form["birthdate"]
        birthdate = datetime.strptime(birthdate_string, "%Y-%m-%d").date()

        date_of_death_string = request.form["date_of_death"]
        date_of_death = None
        if date_of_death_string:
            date_of_death = datetime.strptime(date_of_death_string,
                                              "%Y-%m-%d").date()

        new_author = Author(
            name=name,
            birth_date=birthdate,
            date_of_death=date_of_death
        )

        db.session.add(new_author)
        db.session.commit()

        flash(f"Author {name} added successfully!")
        return redirect(url_for("add_author"))

    return render_template("add_author.html")


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == "GET":
        authors = Author.query.all()
        return render_template("add_book.html", authors=authors)

    if request.method == "POST":
        title = request.form["title"]
        isbn = request.form["isbn"]
        publication_year = request.form["publication_year"]

        author_id = int(request.form["author"])

        new_book = Book(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            author_id=author_id
        )

        db.session.add(new_book)
        db.session.commit()

        flash(f"Book {title} added successfully!")

        return redirect(url_for("add_book"))


@app.route('/')
def home():
    sort_by = request.args.get('sort', 'title')

    if sort_by == 'name':
        books = Book.query.join(Author).order_by(Author.name).all()
    elif sort_by == 'year':
        books = Book.query.order_by(Book.publication_year).all()
    else:
        books = Book.query.order_by(Book.title).all()

    return render_template("home.html", books=books, current_sort=sort_by)


if __name__ == "__main__":
    app.run(debug=True)
