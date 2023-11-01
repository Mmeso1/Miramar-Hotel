from flask import Blueprint, render_template

admin = Blueprint("admin", __name__) 

@admin.route("/")
@admin.route("/home")
def home_page():
    return render_template("admin/index.html", page="Dashboard")

@admin.route("/contact")
def contact_page():
    return render_template("admin/contacts.html", page="Contact")

@admin.route("/profile")
def profile_page():
    return render_template("admin/app-profile.html", page="Profile")

@admin.route("email-compose")
def email_compose():
    return render_template("admin/email-compose.html", page="Email Compose")


@admin.route("/gallery")
def price_page():
    return render_template("admin/uc-lightgallery.html", page="Gallery") #ecom-product-grid.html

@admin.route("/room")
def room_page():
    return render_template("admin/ecom-product-list.html", page="Rooms")

@admin.route("/order")
def order_page():
    return render_template("admin/ecom-product-order.html", page="Booking Requests")

@admin.route("/customer")
def customer_page():
    return render_template("admin/ecom-customers.html", page="Customers")

