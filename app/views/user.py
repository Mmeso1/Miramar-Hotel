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
