from flask import Blueprint, render_template
from app.views.decorators import admin_required

admin = Blueprint("admin", __name__) 

@admin.route("/")
@admin.route("/home")
@admin_required
def home_page():
    flash('Welcome', 'message')
    return render_template("admin/index.html", page="Dashboard")

@admin.route("/contact")
def contact_page():
    return render_template("admin/contacts.html", page="Contact")

@admin.route("/profile")
def profile_page():
    return render_template("admin/app-profile.html", page="Profile")


@admin.route("/email-compose", methods=['POST', 'GET'])
def email_compose():
    error = None  # Initialize the error variable
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        message_body = request.form.get('message_body')

        
        # Check for empty fields
        if not recipient or not subject or not message_body:
            error = "All fields are required*"
            return render_template("admin/email-compose.html", page="Email Compose", error=error, recipient=recipient, subject=subject, message_body=message_body) 

        
        # Check for invalid email format
        if not error and not validate_guest_email(recipient):
            error = "Invalid email format*"
            return render_template("admin/email-compose.html", page="Email Compose", error=error, recipient=recipient, subject=subject, message_body=message_body) 

        
        if not error:
            fromx = 'testingweb3phoenix@gmail.com'
            to  = recipient
            msg = MIMEText(message_body)
            msg['Subject'] = subject
            msg['From'] = fromx
            msg['To'] = to

            try:
                # Creating connection using context manager
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: 
                    smtp_server.login("testingweb3phoenix@gmail.com", EMAIL_PASSWORD)
                    smtp_server.sendmail(fromx, to, msg.as_string())
                    success_sent = 'Email sent successfully!, Google might ome times sort this mails to spam, kindly check that too'
                    return render_template("admin/email-compose.html", page="Email Compose", success_sent=success_sent)
            except Exception as e:
                error = f"An error occurred while sending the email: {str(e)}"
    
    return render_template("admin/email-compose.html", page="Email Compose", error=error)

        

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

