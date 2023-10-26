from flask import Blueprint, render_template


user = Blueprint("user", __name__) 

# LOGIN ROUTE (VIEW)
@user.route("/")
def landing_page():
    return render_template("user/landing.html")

@user.route("/register")
def register_page():
    return render_template("register.html")

@user.route("/login")
def login_page():
    return render_template("login.html")

@user.route("/rooms")
def rooms_page():
    page="Rooms"
    return render_template("user/rooms.html", page_name=page)