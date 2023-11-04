from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.config.variables import EMAIL_PASSWORD
from email_validator import validate_email, EmailNotValidError
import smtplib
from email.mime.text import MIMEText


def validate_guest_email( email_address):
    try:
        valid = validate_email(email_address)
        return True
    except EmailNotValidError as e:
        return False

user = Blueprint("user", __name__) 

# LOGIN ROUTE (VIEW)
@user.route("/")
@user.route("/home")
def landing_page():
    return render_template("user/index.html")

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

@user.route("/contact_us", methods=['POST', 'GET'])
def contact_us():
    page="Contact"
    error = None  # Initialize the error variable
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        email_message = f'''Thank you {name} for reaching out to us! We have received your enquiry and wil get back to you shortly.
        
                
        - signed - MGT,
        Hotel Miariamar SG'''
        
        # Check for empty fields
        if not name or not email or not message:
            error = "All fields are required*"
            return render_template("user/contact_us.html", page_name=page,  error=error, name=name, email=email, message=message) 

        
        # Check for invalid email format
        if not error and not validate_guest_email(email):
            error = "Invalid email format*"
            return render_template("user/contact_us.html", page_name=page,  error=error, name=name, email=email, message=message)  

        
        if not error:
            fromx = 'testingweb3phoenix@gmail.com'
            to  = email
            msg = MIMEText(email_message)
            msg['Subject'] = "Enquiry - Miraiamar Hotel SG"
            msg['From'] = fromx
            msg['To'] = to

            try:
                # Creating connection using context manager
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: 
                    smtp_server.login("testingweb3phoenix@gmail.com", EMAIL_PASSWORD)
                    smtp_server.sendmail(fromx, to, msg.as_string())
                    success_sent = 'Email sent successfully!, Google might some times sort this mails to spam, kindly check that too'
                    return render_template("user/contact_us.html", page_name=page, success_sent=success_sent)
            except Exception as e:
                error = f"An error occurred while sending the email: {str(e)}"

    return render_template("user/contact_us.html", page_name=page, error=error)