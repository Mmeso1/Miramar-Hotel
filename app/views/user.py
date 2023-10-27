from flask import Blueprint, render_template


user = Blueprint("user", __name__) 

# LOGIN ROUTE (VIEW)
@user.route("/")
def landing_page():
    return render_template("user/landing.html")

@user.route("/error_404") 
def error_404():
    return render_template('error_404.html')

@user.route("/error_500") 
def error_500():
    return render_template('error_500.html')

@user.route("/register")
def register_page():
    return render_template("register.html")

@user.route("/login")
def login_page():
    return render_template("login.html")

@user.route("/nearbyplaces")
def nearbyplaces():
    return render_template("nearbyplaces.html")


@user.route("/rooms")
def rooms_page():
    page="Rooms"
    return render_template("user/rooms.html", page_name=page)@user.route("/rooms")

@user.route("/contact_us")
def contact_us():
    page="Contact"
    return render_template("contact_us.html", page_name=page)