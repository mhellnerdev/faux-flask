from fauxflask import app

from flask import render_template, request, redirect


@app.route("/")
def index():

    print(app.config["SECRET_KEY"])

    return render_template("public/index.html")


@app.route("/jinja")
def jinja():

    my_name = 'Mark'

    age = 39

    langs = ["Python", "Javascript", "HTML", "Bootstrap", "Bash", "C#", ]

    friends = {
        "Tom": 30,
        "Amy": 60,
        "Tony": 56,
        "Clarissa": 23

    }

    colors = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def pull(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote(
        name='Flask Jija',
        description='Template Design',
        url='https://github.com/mhellnerdev/faux-flask',
    )

    def repeat(x, qty):
        return x * qty

    return render_template("public/jinja.html", my_name=my_name, age=age, langs=langs, friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, repeat=repeat, my_remote=my_remote)


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)
        
        return redirect(request.url)


    return render_template("public/sign_up.html")
