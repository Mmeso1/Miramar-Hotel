import os
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask import current_app
from ..config.database import db
from werkzeug.utils import secure_filename
from app.models import User


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
    return render_template("user/rooms.html", page_name=page)

@user.route("/room-details")
def room_deets():
    return render_template("user/room_details.html")

@user.route("/contact_us")
def contact_us():
    page="Contact"
    return render_template("user/contact_us.html", page_name=page)

@user.route("/profile")
def profile_page():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    return render_template("user/profile.html", user=user)

# So tha the user can upload images to their profile
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