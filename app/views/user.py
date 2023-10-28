from flask import Blueprint, render_template


user = Blueprint("user", __name__) 

# LOGIN ROUTE (VIEW)
@user.route("/")
@user.route("/home")
def landing_page():
    return render_template("user/landing.html")

@user.route("/register")
def register_page():
    return render_template("register.html")

@user.route("/login")
def login_page():
    return render_template("login.html")

@user.route("/nearbyplaces")
def nearbyplaces():
    page="Nearbyplaces"
    return render_template("user/nearbyplaces.html", page_name=page)


@user.route("/rooms")
def rooms_page():
    page="Rooms"
    return render_template("user/rooms.html", page_name=page)

@user.route("/room-details")
def room_deets():
    return render_template("user/room_details.html")

@user.route("/contact_us")
def contact_us():
    page="Contact"
    return render_template("user/contact_us.html", page_name=page)