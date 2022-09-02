from turtle import title


app = Flask(__name__)


@app.route('/')
def index():
    title = "Merchandise"
    return render_template("index.html", title=title)

@app.route('/Atlanta Hawks')
def Atlanta_Hawks():
    title="Atlanta Hawks"
    return render_template("Atlanta Hawks.html", title=title)

@app.route('/Boston Celtics')
def Boston_Celtics():
    title="Boston Celtics"
    return render_template("Boston Celtics.html", title=title)

@app.route('/Chicago Bulls')
def Chicago_Bulls():
    title="Chicago Bulls"
    return render_template("Chicago Bulls.html", title=title)

@app.route('/Golden State')
def Golden_State():
    title="Golden State"
    return render_template("Golden State.html", title=title)

@app.route('/L.A.Lakers')
def LA_Lakers():
    title="L.A.Lakers"
    return render_template("L.A.Lakers.html", title=title)