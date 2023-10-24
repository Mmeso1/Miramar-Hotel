from flask import Blueprint, render_template


user = Blueprint("user", __name__) 

# LOGIN ROUTE (VIEW)
@user.route("/")
def landing_page():
    return render_template("user/landing.html")
