from flask import Blueprint, render_template, request, redirect, url_for, flash,  session 
import os
from flask import current_app
from ..config.database import db
from werkzeug.utils import secure_filename
from app.models import Room, User, Bookings
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
    if 'registration_success' in session and session['registration_success']:
        flash("User registered successfully!", "success")
        session['registration_success'] = False
    elif 'login_success' in session and session['login_success']:
        flash("User login successful", "success")
        session['login_success'] = False
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
    rooms= Room.query.all()
    return render_template("user/rooms.html", page_name=page, rooms=rooms)

@user.route("/room-details/<int:room_id>")
def room_deets(room_id):
    room = Room.query.get(room_id)
    
    if not room:
        # Handle the case where the room with the given ID doesn't exist
        flash("Room not found", "error")
        return redirect(url_for("user.room_page"))
    
    return render_template("user/room_details.html", room=room, room_id=room_id)


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

@user.route("/profile")
def profile_page():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    bookings = Bookings.Booking.query.filter_by(user_id=user_id).all() if user_id else []
    return render_template("user/profile.html", user=user,bookings=bookings)


# Delete booking
@user.route("/cancel-booking/<int:booking_id>", methods=["GET", "POST"])
def cancel_booking(booking_id):
    booking = Bookings.Booking.query.get(booking_id)
    
    # Check if the booking exists and belongs to the logged-in user
    if booking and booking.user_id == session["user_id"]:
        # Delete the booking from the database
        db.session.delete(booking)
        db.session.commit()
        flash("Booking successfully cancelled", "success")
        return redirect(url_for("user.profile_page"))
    else:
        flash("Booking not found or you don't have permission to cancel it", "error")
        return redirect(url_for("user.profile_page"))
    
# So that the user can upload images to their profile
@user.route("/upload_image", methods=["POST"])
def upload_image():
    profile_img = request.files.get("img")

    if profile_img:
        # Ensure the folder exists before saving the image
        upload_path = os.path.join(current_app.root_path, 'static', 'user_uploads')
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        # Get the current user
        user = User.query.get(session.get('user_id'))

        # Remove the old profile image if it exists
        if user.image:
            old_image_path = os.path.join(current_app.root_path, 'static', user.image)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        # Generate a unique filename for the new image
        image_filename = secure_filename(profile_img.filename)
        image_path = os.path.join('user_uploads', image_filename)

        # Save the new image
        profile_img.save(os.path.join(upload_path, image_filename))

        # Update the user's image field in the database with the relative path to the saved image
        user.image = os.path.join('../../static/user_uploads', image_filename)
        flash("Image updated successfully", "success")
        db.session.commit()

    else:
        flash("Error", "error")
    return redirect(url_for('user.profile_page'))

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

# For the user to update their profile details    # 
@user.route("/update_profile", methods=["POST"])
def update_profile():
    username = request.form.get("username")
    email = request.form.get("email")

   # Additional checks can be added here
    if not username or not email:
        flash("Please provide both username and email", "error")
        return redirect(url_for("user.profile_page"))

    # Get the user from the database (assuming you have a User model)
    user = User.query.filter_by(id=session["user_id"]).first()

    if not user:
        flash("User not found", "error")
        return redirect(url_for("user.profile_page"))

    # Update user information
    user.username = username
    user.email = email
    # Commit changes to the database
    db.session.commit()

    flash("Profile updated successfully", "success")
    return redirect(url_for("user.profile_page"))
