from fauxflask import app


@app.route("/")
def index():
    return "Interior Crocodile Alligator"


@app.route("/about")
def about():
    return "<h1 style='color: green'>I drive a chevrolet movie theater</h1>"
