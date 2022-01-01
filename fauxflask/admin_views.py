from fauxflask import app

from flask import render_template


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/index.html")


@app.route("/admin/profile")
def admin_profile():
    return "Admin Profile"
