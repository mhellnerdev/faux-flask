from fauxflask import app


@app.route("/")
def index():
    return "Interior Crocodile Alligator"


@app.route("/about")
def about():
    return "I drive a chevrolet movie theater"
