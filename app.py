from turtle import title
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    title = "Merchandise"
    return render_template("index.html", title=title)

@app.route('/Templates/Atlanta Hawks')
def Atlanta_Hawks():
    title="Atlanta Hawks"
    return render_template("Templates/Atlanta Hawks.html", title=title)

@app.route('/Templates/Boston Celtics')
def Boston_Celtics():
    title="Boston Celtics"
    return render_template("Templates/Boston Celtics.html", title=title)

@app.route('/Templates/Chicago Bulls')
def Chicago_Bulls():
    title="Chicago Bulls"
    return render_template("Templates/Chicago Bulls.html", title=title)

@app.route('/Templates/Golden State')
def Golden_State():
    title="Golden State"
    return render_template("Templates/Golden State.html", title=title)

@app.route('/Templates/L.A.Lakers')
def LA_Lakers():
    title="L.A.Lakers"
    return render_template("Templates/L.A.Lakers.html", title=title)