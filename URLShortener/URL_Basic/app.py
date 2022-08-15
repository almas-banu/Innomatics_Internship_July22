import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string
import random

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

class Urls(db.Model):
    __tablename__ = 'URLs'
    id = db.Column(db.Integer,primary_key = True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(3))

    def __init__(self, long, short):
        self.long = long
        self.short = short



@app.before_first_request
def create_tables():
    db.create_all()


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_l = random.choices(letters, k=4)
        rand_l = "".join(rand_l)
        short_url = Urls.query.filter_by(short=rand_l).first()
        if not short_url:
            return rand_l

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["in_1"]
        found_url = Urls.query.filter_by(long=url_received).first()
        if found_url:
            return render_template("home.html", url=found_url.short,long=url_received)
        else:
            short_url = shorten_url()
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return render_template("home.html",url=short_url,long=url_received)
    else:
        return render_template("home.html")


@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>Url doesnt exist<h1>'

@app.route('/history')
def history():
    urls = Urls.query.all()
    return render_template("history.html", urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
