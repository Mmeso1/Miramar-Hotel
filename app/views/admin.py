from flask import Blueprint, request, render_template, redirect, url_for
from flask_mail import Message
#  I want to t use it here but keep getting import errors
 # error like this. all tried importing create_app() but got a circular import error. 
 # 
 # Traceback (most recent call last):                                  \Miramar-Hotel> 
#   File "C:\Users\DELL\Desktop\programming\sem4-eproject-Hotel-Miriamar-SG\Miramar-Hotel\main.py", line 5, in <module>
#     app = create_app()
#           ^^^^^^^^^^^^
#   File "C:\Users\DELL\Desktop\programming\sem4-eproject-Hotel-Miriamar-SG\Miramar-Hotel\app\__init__.py", line 22, in create_app        
#     from .views.admin import admin
#   File "C:\Users\DELL\Desktop\programming\sem4-eproject-Hotel-Miriamar-SG\Miramar-Hotel\app\views\admin.py", line 3, in <module>        
#     from app import mail
# ImportError: cannot import name 'mail' from 'app' (C:\Users\DELL\Desktop\programming\sem4-eproject-Hotel-Miriamar-SG\Miramar-Hotel\app\__init__.py)
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

@admin.route("email-compose", methods=['POST'])
def email_compose(): 
    #this is the page that i want to send an email
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        message_body = request.form.get('message_body')

        message = Message(subject, recipients=[recipient])
        message.body = message_body

        mail.send(message)
        return redirect(url_for('admin.email_compose'))  # Redirect back to the email compose page
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

