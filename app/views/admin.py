from flask import Blueprint, render_template
from app.views.decorators import admin_required

admin = Blueprint("admin", __name__) 

@admin.route("/")
@admin.route("/home")
@admin_required
def home_page():
    return render_template("admin/index.html", page="Dashboard")

@admin.route("/contact")
def contact_page():
    return render_template("admin/contacts.html", page="Contact")

@admin.route("/profile")
def profile_page():
    return render_template("admin/app-profile.html", page="Profile")

@admin.route("/message")
def message_page():
    return render_template("admin/message.html", page="Message")

@admin.route("/calendar")
def calendar_page():
    return render_template("admin/app-calender.html", page="Calendar")

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

